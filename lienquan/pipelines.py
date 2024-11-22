import os
import sqlite3
import requests
from urllib.parse import urlsplit
from pathlib import Path


class SQLitePipeline:
    def open_spider(self, spider):
        # Use a context manager for the connection
        self.connection = sqlite3.connect('heroes.db')
        self.cursor = self.connection.cursor()

        # Create tables
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS heroes (
                id INTEGER PRIMARY KEY,
                name TEXT UNIQUE,
                image_url TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS skins (
                id INTEGER PRIMARY KEY,
                hero_id INTEGER,
                skin_image_url TEXT,
                FOREIGN KEY (hero_id) REFERENCES heroes (id) ON DELETE CASCADE
            )
        ''')
        self.items_buffer = []  # Buffer for batch insertion

    def close_spider(self, spider):
        # Insert any remaining items in the buffer before closing
        self._bulk_insert()
        self.connection.close()

    def process_item(self, item, spider):
        self.items_buffer.append(item)

        if len(self.items_buffer) >= 100:  # Batch size
            self._bulk_insert()

        return item

    def _bulk_insert(self):
        # Insert heroes
        if not self.items_buffer:
            return

        # Use a set to prevent duplicate names
        hero_names = {item['name']: item['image_url']
                      for item in self.items_buffer}

        for name, image_url in hero_names.items():
            self.cursor.execute('''
                INSERT OR IGNORE INTO heroes (name, image_url) VALUES (?, ?)
            ''', (name, image_url))
            # Download hero image
            self._download_image(image_url, name, 'hero_image')

        self.connection.commit()  # Commit heroes insertions

        # Retrieve hero IDs and insert skins
        for item in self.items_buffer:
            self.cursor.execute(
                'SELECT id FROM heroes WHERE name = ?', (item['name'],))
            hero_id = self.cursor.fetchone()[0]
            for skin in item.get('skins', []):
                self.cursor.execute('''
                    INSERT INTO skins (hero_id, skin_image_url) VALUES (?, ?)
                ''', (hero_id, skin))
                # Download skin image
                self._download_image(skin, item['name'], 'skins')

        self.connection.commit()  # Commit skins insertions
        self.items_buffer.clear()  # Clear the buffer after insertion

    def _download_image(self, url, hero_name, folder_name):
        """Download the image from the URL and save it to the hero's folder."""
        if not url:
            return

        # Create the directory path
        folder_path = Path('heroes') / hero_name / folder_name
        folder_path.mkdir(parents=True, exist_ok=True)

        # Extract the image name from the URL
        image_name = os.path.basename(urlsplit(url).path)

        # Complete image file path
        file_path = folder_path / image_name

        # Skip download if the file already exists
        if file_path.exists():
            print(f"Image already exists, skipping: {file_path}")
            return

        # Download the image and save it
        try:
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                with open(file_path, 'wb') as out_file:
                    out_file.write(response.content)
                print(f"Image downloaded: {file_path}")
            else:
                print(f"Failed to download image: {url}")
        except Exception as e:
            print(f"Error downloading image {url}: {e}")
