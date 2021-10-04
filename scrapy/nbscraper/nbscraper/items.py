# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags

def remove_currency(value):
    value = value.replace("$", "")
    value = value.replace(",", "")
    value = value.replace(".", "").strip()
    return value

def remove_special(string):
    string = string.replace("\n", "")
    string = string.replace("\r", "")
    string = string.replace("\t", "").strip()
    string = "".join(string)
    return string

class NbscraperItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    price = scrapy.Field(input_processor=MapCompose(remove_tags, remove_currency), output_processor=TakeFirst())
    processor = scrapy.Field(input_processor=MapCompose(remove_tags, remove_special), output_processor=TakeFirst())
    ram = scrapy.Field(input_processor=MapCompose(remove_tags, remove_special), output_processor=TakeFirst())
    monitor = scrapy.Field(input_processor=MapCompose(remove_tags, remove_special), output_processor=TakeFirst())
    storage = scrapy.Field(input_processor=MapCompose(remove_tags, remove_special), output_processor=TakeFirst())
    video_card = scrapy.Field(input_processor=MapCompose(remove_tags, remove_special), output_processor=TakeFirst())