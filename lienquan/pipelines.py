import sqlite3


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

        self.connection.commit()  # Commit skins insertions
        self.items_buffer.clear()  # Clear the buffer after insertion
