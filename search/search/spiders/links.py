# import scrapy
# import datetime
# # from variables import *


# class Item(scrapy.Spider):
#     name = "links"
#     start_urls = [
#         'https://www.larepublica.co'
#     ]
#     custom_settings = {
#         'FEED_URI': 'links_seo.json',
#         'FEED_FORMAT': 'json',
#         'CONCURRENT_REQUESTS': 24,
#         'MEMUSAGE_LIMIT_MB': 2048,
#         'MEMUSAGE_NOTIFY_MAIL': ['csgalindos@hotmail.com'],
#         'ROBOTSTXT_OBEY': True,
#         'USER_AGENT': 'seomaster',
#         'FEED_EXPORT_ENCODING': 'utf-8'
#     }

#     def parse(self, response):
#         today = datetime.date.today().strftime('%d-%m-%Y')
#         titlepage = response.xpath(
#             '// a[starts-with(@href, "https://www.larepublica.co")]/@href').getall()

#         yield {
#             'date': today,
#             'titlepage': titlepage,
#         }
