# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Spider
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import SpafinderSpiderItem
from scrapy.selector import Selector
import urlparse
import time
import sys
from twisted.web import http
import logging
import logging.handlers
import re

class SpafinderSpider(CrawlSpider):
	name = 'spafinder'
	allowed_domains = ['spafinder.com']
	"""
	#problematic urls 
	http://www.spafinder.com/Spa/102671-K-Salon-and-Spa
	http://www.spafinder.com/Spa/2406-Remedez-HairSpa
	File "/home/mtaziz/.virtualenvs/scrapydevenv/spider/upwork/spafinder_spider/spafinder_spider/spiders/spafinder.py", line 66, in parse_item_detail
    web = response.xpath('//div[starts-with(@class, "property-overview_contact")]/a/@href').extract()[0]
	"""
	# start_urls = ['http://www.spafinder.com/Spa/102671-K-Salon-and-Spa', 'http://www.spafinder.com/Spa/2406-Remedez-HairSpa', 'http://www.spafinder.com/Spa/112866-RMLA-Arizona']
	# urls = ["newest", "editor-picked", "popular"]
	
	#################################With som problem working fine###############################################################
	# spafinder_start_urls = ["http://listings.spafinder.com/search?keywords=spa&keywords_pr=&location=Arizona%2C+US",
	# 						"http://listings.spafinder.com/search?keywords=spa&keywords_pr=&location=Colorado%2C+US",
	# 						"http://listings.spafinder.com/search?keywords=spa&keywords_pr=&location=Utah%2C+US",
	# 						"http://listings.spafinder.com/search?keywords=spa&keywords_pr=&location=Arizona%2C+US"
	# 						]
## 776 for colorado = 40
#526 arizona = 27 
#nevada 251 = 13
#utah 198 = 12
#
	# spafinder_start_urls = [
	# 						"http://listings.spafinder.com/search?keywords=&keywords_pr=&location=Hawaii%2C+US&spatypes=Day+Spa",
	# 						"http://listings.spafinder.com/search?page=2&location=Hawaii%2C+US&spatypes=Day+Spa"
	# 						# "http://listings.spafinder.com/search?keywords=spas&keywords_pr=&location=Arizona%2C+US",
	# 						# "http://listings.spafinder.com/search?keywords=spas&keywords_pr=&location=Colorado%2C+US",
	# 						# "http://listings.spafinder.com/search?keywords=spas&keywords_pr=&location=Utah%2C+US",
	# 						# "http://listings.spafinder.com/search?keywords=spas&keywords_pr=&location=Arizona%2C+US"
							# ]
	start_urls = [
					"http://listings.spafinder.com/search?keywords=&keywords_pr=&location=Hawaii%2C+US&spatypes=Day+Spa",
					"http://listings.spafinder.com/search?page=2&location=Hawaii%2C+US&spatypes=Day+Spa"
					# "http://listings.spafinder.com/search?keywords=spas&keywords_pr=&location=Arizona%2C+US",
					# "http://listings.spafinder.com/search?keywords=spas&keywords_pr=&location=Colorado%2C+US",
					# "http://listings.spafinder.com/search?keywords=spas&keywords_pr=&location=Utah%2C+US",
					# "http://listings.spafinder.com/search?keywords=spas&keywords_pr=&location=Arizona%2C+US"
					]
	
	#Hawaii
	# http://listings.spafinder.com/search?keywords=&keywords_pr=&location=Hawaii%2C+US&spatypes=Day+Spa
	# http://listings.spafinder.com/search?page=2&location=Hawaii%2C+US&spatypes=Day+Spa
	####################################################################################
	
	# http://listings.spafinder.com/search?page=10&keywords=spa&location=Arizona%2C+US
	# states = ['Nevada', 'Colorado', 'Utah', 'Arizona']
	# states = ['Colorado']
	###############################################
	# states = ['Arizona']
	# for state in states:
	# 	for i in range (1, 30):
	# 		spafinder_start_urls.append('http://listings.spafinder.com/search?page={0}&keywords=spas&location={1}%2C+US'.format(i,state))
	# allowed_domains = ['spafinder.com']
	# start_urls = spafinder_start_urls

	rules = (
		Rule(
			LinkExtractor(
			allow=(r'\/Spa\/\w.+$', ),  # http://www.spafinder.com/Spa/112866-RMLA-Arizona
			# restrict_xpaths=('//div[@id="content"]//ol[contains(@class, "stream")]', ),
			unique=True,
			),
			callback='parse_item_detail',
			),
		)
	##################################################################################################################

	def parse_item_detail(self, response):
	# def parse(self, response):

		item = SpafinderSpiderItem()
		name_data = response.xpath('//div[starts-with(@class, "large-9")]/h1/span/text()').extract()
		item['Name'] = name_data
		if not name_data:
			name_data2 = response.xpath('//*[@id="spafinder"]/head/title/text()').extract()
			name_data2 = str(name_data2).split(' at')
			if "[u'" in name_data2[0]:
				item['Name'] = str(name_data2[0]).replace("[u'", '')
		else:
			item['Name'] = name_data

		item['Address'] = response.xpath('//div[starts-with(@class, "property-overview_address")]//address/span[starts-with(@class, "street-address")]/text()').extract()
		item['City'] = response.xpath('//div[starts-with(@class, "property-overview_address")]//address/span[contains(@class, "locality")]/text()').extract()
		item['State'] = response.xpath('//div[starts-with(@class, "property-overview_address")]//address/span[starts-with(@class, "region")]/text()').extract()
		item['Postal_Code'] = response.xpath('//div[starts-with(@class, "property-overview_address")]//address/span[starts-with(@class, "postal-code")]/text()').extract()
		# item['Website'] =
		phone_data1 = response.xpath('//div[starts-with(@id, "property-phone")]/text()').extract()
		if phone_data1:
			item['Phone'] = phone_data1[0]
		else:
			item['Phone'] = ''

		# email_data1 = response.xpath('//div[starts-with(@class, "property-overview_contact")]//div[starts-with(@class, "property-email")]/@data1').extract()
		# email_data2 = response.xpath('//div[starts-with(@class, "property-overview_contact")]//div[starts-with(@class, "property-email")]/@data2').extract()
		email_data1 = response.xpath('//div[starts-with(@class, "property-email")]/@data1').extract()
		email_data2 = response.xpath('//div[starts-with(@class, "property-email")]/@data2').extract()
		if "u''" in email_data1[0] and "u''" in email_data2:
			item['Email_Address'] = ''
			# item['Email_Address'] = str(email_data1[0])+'@'+str(email_data2[0])
		else:
			item['Email_Address'] = str(email_data1[0])+'@'+str(email_data2[0])
			# item['Email_Address'] = ''
		# if not email_data1:
		# 	item['Email_Address'] = ''
		web = response.xpath('.//div[starts-with(@class, "property-overview_contact")]/a/@href').extract()
		if web:
			match = re.search(r'http\:\/\/w.+', str(web[0]))
			if match:
				item['Website'] = match.group(0)

		# if web:
		# 	web = str(web).split('http://')
		# if not "www." in str(web):
		# 	item['Website'] = "www."+str(web)
		else:
			item['Website'] = ''

		# item['Website'] = 'http://www.'+str(email_data2[0])
		item['urls'] = response.url

		yield item
		
		"""		
		Name = scrapy.Field()
	    Address = scrapy.Field()
	    City = scrapy.Field()
	    State = scrapy.Field()
	    Website = scrapy.Field()
	    Phone = scrapy.Field()
	    Email_Address = scrapy.Field()
	    urls = scrapy.Field()
	    """

# class SpafinderSpider(scrapy.Spider):
#     name = "spafinder"
#     allowed_domains = ["http://www.spafinder.com"]
#     start_urls = (
#         'http://www.http://www.spafinder.com/',
#     )
#     """
#     ########search keyword: spa 
#     http://listings.spafinder.com/search?keywords=spa&keywords_pr=&location=Arizona%2C+US
#     Formation of url: 
#     http://listings.spafinder.com/search?keywords=Facials&keywords_pr=&location=Arizona%2C+US
#     http://www.spafinder.com/Spa/10488-Hand-and-Stone-Massage-and-Facial-Spa-Scottsdale
#     http://listings.spafinder.com/search?page=2&keywords=Facials&location=Arizona%2C+US
#     http://listings.spafinder.com/search?page=3&keywords=Facials&location=Arizona%2C+US
#     """

#     def parse(self, response):
#         pass
