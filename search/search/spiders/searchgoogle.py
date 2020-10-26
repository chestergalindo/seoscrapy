# import scrapy
# import datetime


# class Item(scrapy.Spider):
#     name = "google"
#     start_urls = [
#         'https://www.larepublica.co'
#         # 'https://www.google.com/search?sxsrf=ALeKk02aann3LsYiwFHFd-LktiXc63Ms3Q%3A1600429042356&source=hp&ei=8ptkX7jCE86p5wKH0pWQBw&q=site%3Ahttps%3A%2F%2Fwww.javeriana.edu.co&oq=site&gs_lcp=CgZwc3ktYWIQAxgAMgQIIxAnMgQIIxAnMgQIIxAnMggIABCxAxCDATIICAAQsQMQgwEyBQgAELEDMggIABCxAxCDATICCAAyBQgAELEDMggIABCxAxCDAVDBN1iBQGD5WmgBcAB4AIABkwGIAd8EkgEDMC41mAEAoAEBqgEHZ3dzLXdpeg&sclient=psy-ab'
#     ]
#     custom_settings = {
#         'FEED_URI': 'seo.json',
#         'FEED_FORMAT': 'json',
#         'CONCURRENT_REQUEST': 24,
#         'MEMUSAGE_LIMIT_MB': 2048,
#         'MEMUSAGE_NOTIFY_MAIL': ['csgalindos@hotmail.com'],
#         'ROBOTSTXT_OBEY': True,
#         'USER_AGENT': 'seomaster',
#         'FEED_EXPORT_ENCODING': 'utf-8'
#     }

#     def parse(self, response):
#         today = datetime.date.today().strftime('%d-%m-%Y')
#         titleingoogle = response.xpath('//h3/text()').getall()
#         link = response.xpath('//('//cite/text()').getall()')

#         yield {
#             'date': today,
#             # 'titles': titleingoogle,
#         }
