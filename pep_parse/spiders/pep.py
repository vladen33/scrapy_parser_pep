import re

import scrapy

from pep_parse.constants import PEP_DOMAIN
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [PEP_DOMAIN]
    start_urls = [f'https://{domain}/' for domain in allowed_domains]

    def parse(self, response):
        shortlinks = response.xpath(
            '//table[contains(@class, "pep-zero-table")]'
            '/tbody/tr/td[3]/a').xpath('@href')
        for link in shortlinks:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        pep_title = response.css('h1.page-title::text').get()
        result = re.fullmatch(
            r'PEP (?P<number>\d{1,4}) – (?P<name>.*)', pep_title)
        data = {
            'number': result.group('number'),
            'name': result.group('name'),
            'status': response.xpath('//abbr[1]/text()').get()
        }
        yield PepParseItem(data)
