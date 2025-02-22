from urllib.parse import urljoin

import scrapy
from scrapy import Selector

class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        # shortlinks = response.xpath('//table[contains(@class, "pep-zero-table")]/tbody/tr/td[3]/a').xpath('@href')

        links = [
            urljoin(self.start_urls[0], shortlink.get()) for shortlink in (
                response.xpath('//table[contains(@class, "pep-zero-table")]'
                               '/tbody/tr/td[3]/a').xpath('@href')
            )
        ]


        for link in links:
            print(link)
        # for pep_shortlink in pep_shortlinks:
        #     # print(self.start_urls[0], pep_shortlink.get())
        #     pep_link = urljoin(self.start_urls[0], pep_shortlink.get())
        #     print(pep_link)


