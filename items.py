# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class AmazonReviewsScrapingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    image = scrapy.Field()
    price = scrapy.Field()
    exprice = scrapy.Field()
    colours = scrapy.Field()
    noreview = scrapy.Field()
    rating = scrapy.Field()
    techdetails = scrapy.Field()
    pass

"""
 Product Title
 Product Description
 Product Enlarge Image
 Product Price (With Exchange and Without Exchange)
 Product Colours
 # of Reviews
 Star Rating
 Technical Details
 Most Recent 100 Reviews
"""