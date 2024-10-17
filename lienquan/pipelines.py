import sqlite3


class SQLitePipeline:
    def open_spider(self, spider):
        self.connection = sqlite3.connect('heroes.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS heroes (
                id INTEGER PRIMARY KEY,
                name TEXT,
                image_url TEXT,
                skins TEXT
            )
        ''')

    def close_spider(self, spider):
        self.connection.commit()
        self.connection.close()

    def process_item(self, item, spider):
        skins = ', '.join(item.get('skins', []))
        self.cursor.execute('''
            INSERT INTO heroes (name, image_url, skins) VALUES (?, ?, ?)
        ''', (item['name'], item['image_url'], skins))
        return item
