# Lienquan Scraper

Welcome to the **Lienquan Scraper** repository! 🦸‍♂️✨ This project is designed to **scrape and store data** about heroes and their skins from the popular game **Liên Quân Mobile**. With this scraper, you can efficiently collect hero data, including images and available skins, and store them in a SQLite database for further analysis or development purposes.

## 🎮 Features

- **Hero Data Scraping**: Collects names, images, and skins of heroes from the game.
- **SQLite Database**: Automatically stores scraped data in a structured SQLite database.

## 🛠️ Installation and Usage

To get started with the Lienquan Scraper, follow these steps:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/JuniperNexus/lienquan-scraper.git
    cd lienquan-scraper
    ```

2. **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the scraper**:

    ```bash
    scrapy crawl heroes
    ```

    This command will initiate the scraping process, and data will be stored in `heroes.db`.

## 🗃️ Database Structure

The database consists of the following tables:

- **heroes**: Stores unique heroes with their names and image URLs.
- **skins**: Stores skin details linked to their respective heroes.

### Database Example

```sql
CREATE TABLE IF NOT EXISTS heroes (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,
    image_url TEXT
);

CREATE TABLE IF NOT EXISTS skins (
    id INTEGER PRIMARY KEY,
    hero_id INTEGER,
    skin_image_url TEXT,
    FOREIGN KEY (hero_id) REFERENCES heroes (id) ON DELETE CASCADE
);
```

## 🤝 Contributing

We welcome contributions! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## 📝 License

This project is licensed under the [MIT License](LICENSE). See the LICENSE file for more details.

## 🙋‍♂️ Contact

For questions, issues, or suggestions, feel free to open an issue or contact me at [juniper.nexus24@gmail.com](mailto:juniper.nexus24@gmail.com).

Thank you for checking out the Lienquan Scraper! Happy scraping! 🌐
