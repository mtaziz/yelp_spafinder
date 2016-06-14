# -*- coding: utf-8 -*-

# Scrapy settings for spafinder_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

import time, os, sys
from datetime import datetime 
BOT_NAME = 'spafinder_spider'

SPIDER_MODULES = ['spafinder_spider.spiders']
NEWSPIDER_MODULE = 'spafinder_spider.spiders'

# -*- coding: utf-8 -*-

# Scrapy settings for vessels_dispatch_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
DOWNLOADER_MIDDLEWARES = {'scrapy_crawlera.CrawleraMiddleware': 600}
CRAWLERA_ENABLED = True
# please have your Crawlera API
CRAWLERA_PASS = ''
CONCURRENT_REQUESTS = 32
CONCURRENT_REQUESTS_PER_DOMAIN = 32
AUTOTHROTTLE_ENABLED = False
DOWNLOAD_TIMEOUT = 600


# USER_AGENT_LIST = [
# #Firefox
#     "Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",
#     "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
#     #Chrome
#     "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
#     "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1467.0 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1623.0 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.103 Safari/537.36",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.38 Safari/537.36",
#     #IE
#     "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)",
#     "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
#     "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
#     "Mozilla/5.0 (IE 11.0; Windows NT 6.3; Trident/7.0; .NET4.0E; .NET4.0C; rv:11.0) like Gecko",
#     "Mozilla/5.0 (IE 11.0; Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko",
#     #Safari
#     "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",
#     "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_6; it-it) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",
#     "Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-HK) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
#     "Mozilla/5.0 (Windows; U; Windows NT 6.1; sv-SE) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4",
#     "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/536.26.17 (KHTML, like Gecko) Version/6.0.2 Safari/536.26.17",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/6.1.3 Safari/537.75.14",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/600.3.10 (KHTML, like Gecko) Version/8.0.3 Safari/600.3.10",
#     "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"]

###{{{ProxyMiddleware(privoxy)
# HTTP_PROXY = 'https://127.0.0.1:8123' ###Popilo Proxy Config###
# HTTP_PROXY = 'https://127.0.0.1:8118'	###{Privoxy Proxy Config}###
# DOWNLOADER_MIDDLEWARES = {
#      'spafinder_spider.middlewares.RandomUserAgentMiddleware': 400,
#      'spafinder_spider.middlewares.ProxyMiddleware': 410,
#      # 'spafinder_spider.middlewares.SampleMiddleware': 500,
#      'scrapy.downloadermiddleware.useragent.UserAgentMiddleware': None
#     # Disable compression middleware, so the actual HTML pages are cached
# }
###}}}

# ITEM_PIPELINES = {
#                     # 'spafinder_spider.pipelines.GsaadvantageIfEmptyFieldPipeline': 510,
#                     'spafinder_spider.pipelines.TestPipeline': 520
#                     }


###{{{Feed Exporters to force CSV in ordered
FEED_EXPORTERS = {
    'csv': 'spafinder_spider.exporters.CSVGsaadvantageItemExporter'
}

FIELDS_TO_EXPORT = ['Name', 'Address', 'City', 'State', 'Postal_Code', 'Website', 'Phone', 'Email_Address', 'urls', 'category_informational']
# Name	Address	City	State	Website	Phone	Email address

timestmp = datetime.now().strftime('%Y-%b-%d_%H-%M-%S')
FEED_FORMAT = 'csv' # exports to csv
# dateTimeString = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
FEED_URI = "export/Spa_Leads_HawaiiYelp_{0}.csv".format(timestmp) # WHERE to store the export file

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'spafinder_spider.pipelines.DuplicatePipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
#AUTOTHROTTLE_ENABLED=True
# The initial download delay
#AUTOTHROTTLE_START_DELAY=5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY=60
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG=False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings

HTTPCACHE_ENABLED=True
HTTPCACHE_EXPIRATION_SECS=8500000   
HTTPCACHE_DIR='httpcache'

# HTTPCACHE_IGNORE_HTTP_CODES = [301,302]
#HTTPCACHE_IGNORE_HTTP_CODES=[]
#HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'
