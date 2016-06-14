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
from scrapy.conf import settings



class SpafinderSpider(CrawlSpider):
	name = 'spafinder_bonus'
	allowed_domains = ['yelp.com']
	custom_settings = {'CRAWLERA_PRESERVE_DELAY': True, 'DOWNLOAD_DELAY': 10.0}
	spafinder_start_urls = ["http://www.yelp.com/search?find_desc=spa&find_loc=utah&start=0&cflt=spas"]

	# http://listings.spafinder.com/search?page=10&keywords=spa&location=Arizona%2C+US
	# states = ['Nevada', 'Colorado', 'Utah', 'Arizona']
	# states = ['Colorado']
	# http://www.yelp.com/search?find_desc=spa&cflt=spas&find_loc=utah&start=20
	# states = ['Arizona']
	# for state in states:
	for i in range(10, 170, 10):
		spafinder_start_urls.append('http://www.yelp.com/search?find_desc=spa&cflt=spas&find_loc=utah&start={0}'.format(i))
	start_urls = spafinder_start_urls
	"""
	http://www.yelp.com/biz/elase-medical-spas-salt-lake-city-3?osq=spa
	http://www.yelp.com/biz/sego-lily-spa-bountiful?osq=spa
	"""

	rules = (
		Rule(
			LinkExtractor(
			allow=(r'http\:\/\/www\.yelp\.com\/biz\/\w.+\?osq\=spa', ),  # http://www.yelp.com/biz/elase-medical-spas-salt-lake-city-3?osq=spa
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
		# xpath('//*[@id="wrap"]/div[3]/div/div[1]/div/div[2]/div[1]/h1')
		"""
		<h1 class="biz-page-title embossed-text-white shortenough" itemprop="name">
        Elase Medical Spas
        </h1>
        <meta property="og:title" content="Elase Medical Spas - Salt Lake City - Salt Lake City, UT">
		"""
		# name_data = response.xpath('//div[starts-with(@class, "large-9")]/h1/span/text()').extract()
		# if '- Salt Lake City UT' or '- Salt Lake City' in name_data:
		item['Name'] = response.xpath('//meta[@property="og:title"]/@content').extract()
		# name_data = response.xpath('//h1[starts-with(@class, "biz-page-title embossed-text-white shortenough")]/text()').extract()
		# if name_data:
		# 	item['Name'] = map(unicode.strip, name_data)
		# else:
		# 	item['Name'] = ''

		# if not name_data:
		# 	name_data2 = response.xpath('//*[@id="spafinder"]/head/title/text()').extract()
		# 	name_data2 = str(name_data2).split(' at')
		# 	if "[u'" in name_data2[0]:
		# 		item['Name'] = str(name_data2[0]).replace("[u'", '')
		# else:
		# 	item['Name'] = name_data
		"""
		<li class="map-box-address">
        <strong class="street-address">
        <address itemprop="address" itemscope="" itemtype="http://schema.org/PostalAddress">
        <span itemprop="streetAddress">2236 South 1300 E<br>Ste D-4</span><br><span itemprop="addressLocality">Salt Lake City</span>, <span itemprop="addressRegion">UT</span> <span itemprop="postalCode">84106</span><br><meta content="US" itemprop="addressCountry">
        </address>
        </strong>
		"""

		item['Address'] = response.xpath('//li[starts-with(@class, "map-box-address")]/strong[starts-with(@class, "street-address")]/address/span[@itemprop="streetAddress"]/text()').extract()

		
		# item['City'] = response.xpath('//div[starts-with(@class, "property-overview_address")]//address/span[contains(@class, "locality")]/text()').extract()
		# item['State'] = response.xpath('//div[starts-with(@class, "property-overview_address")]//address/span[starts-with(@class, "region")]/text()').extract()
		# item['Postal_Code'] = response.xpath('//div[starts-with(@class, "property-overview_address")]//address/span[starts-with(@class, "postal-code")]/text()').extract()
		# item['Website'] =
		"""
		<span class="biz-phone" itemprop="telephone">
        (801) 495-2737
        </span>
		"""
		tele_data = response.xpath('//span[starts-with(@class, "biz-phone") and contains(@itemprop, "telephone")]/text()').extract()
		tele = [x for x in [x.strip() for x in tele_data] if x]
		# phone_data1 = response.xpath('//span[starts-with(@class, "biz-phone") and contains(@itemprop="telephone")]/text()').extract()
		if tele:
			item['Phone'] = tele
		else:
			item['Phone'] = ''

		# email_data1 = response.xpath('//div[starts-with(@class, "property-overview_contact")]//div[starts-with(@class, "property-email")]/@data1').extract()
		# email_data2 = response.xpath('//div[starts-with(@class, "property-overview_contact")]//div[starts-with(@class, "property-email")]/@data2').extract()
		"""
		Email:
		""" 
		# email_data1 = response.xpath('//div[starts-with(@class, "property-email")]/@data1').extract()
		# email_data2 = response.xpath('//div[starts-with(@class, "property-email")]/@data2').extract()
		# if "u''" in email_data1[0] and "u''" in email_data2:
		# 	item['Email_Address'] = ''
		# 	# item['Email_Address'] = str(email_data1[0])+'@'+str(email_data2[0])
		# else:
		# 	item['Email_Address'] = str(email_data1[0])+'@'+str(email_data2[0])
			# item['Email_Address'] = ''
		# if not email_data1:
		# 	item['Email_Address'] = ''
		"""
		<div class="biz-website">
        <span class="offscreen">Business website</span>
        <a href="/biz_redir?url=http%3A%2F%2Fwww.elase.com%2Futah&amp;src_bizid=UXRovzSS9MnsDjqELXQlLg&amp;cachebuster=1464254922&amp;s=801d784e85657a99d51cbaac594acd551b15f24ee84f179c84335b569aa38a70" target="_blank">elase.com/utah</a>
        </div>
		"""
		web = response.xpath('//div[starts-with(@class, "biz-website")]/a/text()').extract()
		item['Website'] = web
		# if web:
		# 	match = re.search(r'http\:\/\/w.+', str(web[0]))
		# 	if match:
		# 		item['Website'] = match.group(0)

		# if web:
		# 	web = str(web).split('http://')
		# if not "www." in str(web):
		# 	item['Website'] = "www."+str(web)
		# else:
		# 	item['Website'] = ''

		# item['Website'] = 'http://www.'+str(email_data2[0])
		"""
		Category_String:
		<span class="category-str-list">
        <a href="/search?find_desc=spa&amp;find_loc=utah&amp;cflt=medicalspa">Medical Spas</a>,
        <a href="/search?find_desc=spa&amp;find_loc=utah&amp;cflt=spas">Day Spas</a>,
        <a href="/search?find_desc=spa&amp;find_loc=utah&amp;cflt=hairremoval">Hair Removal</a>
        </span>
		"""
		item['category_informational'] = response.xpath('//span[starts-with(@class, "category-str-list")]/a//text()').extract()
		item['urls'] = response.url
		yield item
