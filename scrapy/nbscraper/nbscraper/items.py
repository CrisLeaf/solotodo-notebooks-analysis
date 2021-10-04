# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags

def remove_currency(value):
    return value.replace(["$", ".", ","], "").strip()

def clean_string(string):
    return string.replace(["\n", "\r", "\t"], "").strip()

class NbscraperItem(scrapy.Item):
    # define the fields for your item here like:
    pass