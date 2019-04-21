# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 13:20:56 2019

@author: Apurva
"""

import scrapy
 
# Creating a new class to implement Spide
class AmazonReviewsSpider(scrapy.Spider):
     
    # Spider name
    name = 'amazon_reviews'
     
    # Domain names to scrape
    allowed_domains = ['amazon.in']
     
    # Base URL for the MacBook air reviews
    #myBaseUrl = "https://www.amazon.in/Apple-MacBook-Air-13-3-inch-MQD32HN/product-reviews/B073Q5R6VR/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews&pageNumber="
    myBaseUrl = "https://www.amazon.in/OnePlus-Mirror-Black-128GB-Storage/product-reviews/B07DJD1Y3Q/ref=cm_cr_dp_d_show_all_top?ie=UTF8&reviewerType=all_reviews&pageNumber="
    
    start_urls=[]
    
    # Creating list of urls to be scraped by appending page number a the end of base url
    for i in range(1,50):
        start_urls.append(myBaseUrl+str(i))
    
    # Defining a Scrapy parser
    def parse(self, response):
         items = AmazonItem()
         title = response.xpath('//h1[@id="title"]/span/text()').extract()
         sale_price = response.xpath('//span[contains(@id,"ourprice") or contains(@id,"saleprice")]/text()').extract()
         category = response.xpath('//a[@class="a-link-normal a-color-tertiary"]/text()').extract()
         availability = response.xpath('//div[@id="availability"]//text()').extract()
         items['product_name'] = ''.join(title).strip()
         items['product_sale_price'] = ''.join(sale_price).strip()
         items['product_category'] = ','.join(map(lambda x: x.strip(), category)).strip()
         items['product_availability'] = ''.join(availability).strip()
         yield items
            
        """
            data = response.css('#cm_cr-review_list')
             
            # Collecting product star ratings
            star_rating = data.css('.review-rating')
             
            # Collecting user reviews
            comments = data.css('.review-text')
            count = 0
             
            # Combining the results
            for review in star_rating:
                yield{'stars': ''.join(review.xpath('.//text()').extract()),
                      'comment': ''.join(comments[count].xpath(".//text()").extract())
                     }
                count=count+1
        """
