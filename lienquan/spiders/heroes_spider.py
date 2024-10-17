import scrapy
import re


class HeroesSpider(scrapy.Spider):
    name = "heroes"
    start_urls = ["https://lienquan.garena.vn/hoc-vien/tuong-skin/"]

    def clean_name(self, name):
        """Cleans the hero name by stripping whitespace and normalizing."""
        name = name.strip()  # Remove leading/trailing whitespace
        # Replace multiple spaces/newlines with a single space
        name = re.sub(r'\s+', ' ', name)
        return name

    def parse(self, response):
        self.logger.info(f"Parsing heroes from {response.url}")
        heroes = response.css("div.st-heroes__list a.st-heroes__item")

        for hero in heroes:
            try:
                raw_name = hero.css("h2.st-heroes__item--name::text").get()
                name = self.clean_name(raw_name)
                image_url = hero.css(
                    "div.st-heroes__item--img img::attr(src)").get()
                hero_link = hero.attrib['href']

                yield response.follow(
                    hero_link,
                    self.parse_hero_skins,
                    meta={'name': name, 'image_url': image_url}
                )
            except Exception as e:
                self.logger.error(f"Error parsing hero: {e}")

    def parse_hero_skins(self, response):
        name = response.meta['name']
        image_url = response.meta['image_url']

        # Extract skin items
        skins = response.css(
            "ul.hero__skins--list li a img::attr(src)").getall()

        # Create a dictionary to hold the hero and skin data
        yield {
            'name': name,
            'image_url': image_url,
            'skins': skins
        }
