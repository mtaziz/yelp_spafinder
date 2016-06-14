# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpafinderSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # FIELDS_TO_EXPORT = ['Name', 'Address', 'City', 'State', 'Website', 'Phone', 'Email_Address']
    
    Name = scrapy.Field()
    Address = scrapy.Field()
    City = scrapy.Field()
    State = scrapy.Field()
    Postal_Code = scrapy.Field()
    Website = scrapy.Field()
    Phone = scrapy.Field()
    Email_Address = scrapy.Field()
    urls = scrapy.Field()
    category_informational = scrapy.Field()

    pass
