import sqlite3


class SQLitePipeline:
    def open_spider(self, spider):
        self.connection = sqlite3.connect('heroes.db')
        self.cursor = self.connection.cursor()

        # Create heroes table without skins column
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS heroes (
                id INTEGER PRIMARY KEY,
                name TEXT UNIQUE,
                image_url TEXT
            )
        ''')

        # Create skins table with hero_id as a foreign key
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS skins (
                id INTEGER PRIMARY KEY,
                hero_id INTEGER,
                skin_image_url TEXT,
                FOREIGN KEY (hero_id) REFERENCES heroes (id) ON DELETE CASCADE
            )
        ''')

    def close_spider(self, spider):
        self.connection.commit()
        self.connection.close()

    def process_item(self, item, spider):
        # Insert hero and get hero_id
        self.cursor.execute('''
            INSERT OR IGNORE INTO heroes (name, image_url) VALUES (?, ?)
        ''', (item['name'], item['image_url']))

        # Get the hero_id of the inserted or existing hero
        self.cursor.execute(
            'SELECT id FROM heroes WHERE name = ?', (item['name'],))
        hero_id = self.cursor.fetchone()[0]

        # Insert skins for the hero
        for skin in item.get('skins', []):
            self.cursor.execute('''
                INSERT INTO skins (hero_id, skin_image_url) VALUES (?, ?)
            ''', (hero_id, skin))

        return item
