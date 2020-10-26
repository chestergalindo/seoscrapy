# import scrapy


# class robots(scrapy.Spider):
#     name = "robots"
#     start_urls = [
#         'https://www.platzi.com/robots.txt'
#     ]
#     custom_settings = {
#         'FEED_URI': 'robots.json',
#         'FEED_FOMAT': 'json',
#         'CONCURRENT_REQUESTS': 24,
#         'MEMUSAGE_LIMIT_MB': 2048,
#         'MEMUSAGE_NOTIFY_MAIL': ['csgalindos@hotmail.com'],
#         'ROBOTSRXT_OBEY': True,
#         'USER_AGENT': 'seomaster',
#         'FEED_EXPORT_ENCODING': 'utf-8', }

#     def parse(self, response):
#         body = response.xpath('//pre/text()').getall()

#         yield{
#             'body': body,
#         }
