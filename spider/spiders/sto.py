# -*- coding: utf-8 -*-
import scrapy


class StoSpider(scrapy.Spider):
    name = 'sto'
    allowed_domains = ['stackoverflow.com']
    start_urls = []
    for i in range(6000):
        start_urls.append('https://stackoverflow.com/questions/tagged/javascript?tab=votes&page=' + str(i+1) + '&pagesize=50')

    def parse(self, response):
        for href in response.css('.question-summary h3 a::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_question)

    def parse_question(self, response):
        yield {
            'title': response.css('h1 a::text').extract()[0],
            # 'q_votes': response.css('.js-vote-count::text').extract()[0],
            'code': response.css('div.answer pre code::text').extract()[0],
            'a_votes': response.css('.js-vote-count::text').extract()[1],
            'url': response.url
        }
