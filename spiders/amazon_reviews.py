# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 13:20:56 2019

@author: Apurva
"""

import scrapy
from ..items import AmazonReviewsScrapingItem
 
# Creating a new class to implement Spide
class AmazonReviewsSpider(scrapy.Spider):
     
    # Spider name
    name = 'amazon_reviews'
    start_urls = [
            'https://www.amazon.in/dp/B07DJHY82F/ref=gbph_img_m-5_d182_b23b14bf?smid=A23AODI1X2CEAE&pf_rd_p=a3a8dc53-aeed-4aa1-88bb-72ce9ddad182&pf_rd_s=merchandised-search-5&pf_rd_t=101&pf_rd_i=1389401031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=P3FSQH2KEB3B5QQ1NQD5'
            ]
     
    # Base URL for the MacBook air reviews
    #myBaseUrl = "https://www.amazon.in/Apple-MacBook-Air-13-3-inch-MQD32HN/product-reviews/B073Q5R6VR/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews&pageNumber="
    
    
    # Defining a Scrapy parser
    def parse(self, response):
        items = AmazonReviewsScrapingItem()
        
        name = response.css('#productTitle::text').extract()
        revnio = response.css('#acrCustomerReviewText').css('::text').extract()
        price = response.css('#priceblock_dealprice').css('::text').extract()
        #exprice = response.css('#sopp_feature_div .a-spacing-top-small:nth-child(1) .a-list-item').css('::text').extract()
        exprice = response.css('#maxBuyBackDiscountSection .a-color-price').css('::text').extract()
        imgg = response.css('.imgTagWrapper::attr(src)').extract()
        colours = response.css('#variation_color_name .selection').css('::text').extract()
        rating = response.css('.arp-rating-out-of-text').css('::text').extract()
        description = response.css('.aplus-module-1-description , .aplus-p3 , .aplus-p1 , #productDescription p').css('::text').extract()
        techdet = response.css('.col1 .attrG').css('::text').extract()
        
        items['title']=name
        items['description']=description
        items['image']=imgg
        items['price']=price
        items['exprice']=exprice
        items['colours']=colours
        items['noreview']=revnio
        items['rating']=rating
        items['techdetails']=techdet
        
        yield items
        
        
    
    
        
                              