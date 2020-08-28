import scrapy
import datetime


class Item(scrapy.Spider):
    name = "seo"
    start_urls = [
        'https://www.larepublica.co/'
        # 'https://treble.ai/'
    ]
    custom_settings = {
        'FEED_URI': 'seo.json',
        'FEED_FORMAT': 'json',
        'CONCURRENT_REQUESTS': 24,
        'MEMUSAGE_LIMIT_MB': 2048,
        'MEMUSAGE_NOTIFY_MAIL': ['csgalindos@hotmail.com'],
        'ROBOTSTXT_OBEY': True,
        'USER_AGENT': 'seomaster',
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    def parse(self, response):
        today = datetime.date.today().strftime('%d-%m-%Y')
        titlepage = response.xpath('//title/text()').get()
        htitle = response.xpath('//h1/text()').get()
        meta_description = response.xpath(
            '//meta[contains(@name,"description")]').get()
        meta_keywords = response.xpath(
            '//meta[contains(@name,"keywords")]').getall()
        meta_google = response.xpath(
            '//meta[contains(@property,"og")]').getall()
        meta_facebook = response.xpath(
            '//meta[contains(@property,"fb")]').getall()
        meta_twitter = response.xpath(
            '//meta[contains(@name,"twitter")]').getall()
        img = response.xpath('//img[not(@alt)]').getall()
        imgwoalt = response.xpath('//img[contains(@alt,"")]').getall()
        bottons = response.xpath('//button[not(@href)]/text()').getall()

        yield {
            'date': today,
            'titlepage': titlepage,
            'description': meta_description,
            'keywords': meta_keywords,
            'google': meta_google,
            'facebook': meta_facebook,
            'twitter': meta_twitter,
            'title': htitle,
            'img_without_alt': img,
            'img_with_alt_empty': imgwoalt,
            'bottons_with_links': bottons
        }
