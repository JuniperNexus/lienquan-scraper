# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LienquanItem(scrapy.Item):
    name = scrapy.Field()
    image_url = scrapy.Field()
    skins = scrapy.Field()  # Add skins field for scraping skins
