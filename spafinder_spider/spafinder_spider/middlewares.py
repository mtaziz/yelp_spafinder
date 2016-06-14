import os
import random
from scrapy.conf import settings
from scrapy.item import Item, Field
from scrapy.spiders import SitemapSpider
from scrapy.utils.response import get_base_url
from time import time
from scrapy.http import Response


class RandomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        ua  = random.choice(settings.get('USER_AGENT_LIST'))
        if ua:
            request.headers.setdefault('User-Agent', ua)

class ProxyMiddleware(object):
    def process_request(self, request, spider):
        request.meta['proxy'] = settings.get('HTTP_PROXY')

class SampleMiddleware(object):
    def process_request(self, request, spider):
        request.meta['__start_time'] = time()
        request.meta['__end_time'] = time()
        # this not block middlewares which are has greater number then this
        return None

    def process_spider_input(response, spider):
        if response.status >= 400:
            print('%d\t%s\t0' % (
                response.status, response.url
            ))

    def process_response(self, request, response, spider):
        request.meta['__end_time'] = time()
        return response  # return response coz we should

    def process_exception(self, request, exception, spider):
        request.meta['__end_time'] = time()
        return Response(url=request.url, status=110, request=request)