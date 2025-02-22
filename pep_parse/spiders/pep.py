import re
from urllib.parse import urljoin

import scrapy
from scrapy import Selector

class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        shortlinks = response.xpath('//table[contains(@class, "pep-zero-table")]/tbody/tr/td[3]/a').xpath('@href')

        counter = 1
        for link in shortlinks:
            counter += 1
            if counter > 5:
                break
            yield response.follow(link, callback=self.parse_pep)
            # print(link)


    def parse_pep(self, response):
        pep_title = response.css('h1.page-title::text').get()
        result = re.fullmatch(r'PEP (?P<number>\d{1,4}) – (?P<name>.*)', pep_title)
        number = result.group('number')
        name = result.group('name')
        status = response.xpath('//abbr[1]/text()').get()

        print('NUMBER = ', result.group('number'))
        print('NAME = ', result.group('name'))
        print('STATUS = ', status)

        # print('>>=='*20, res.groups())




        # yield {'aaa': 'AAAAAA'}


