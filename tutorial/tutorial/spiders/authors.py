# -*- coding: utf-8 -*-
import scrapy


class AuthorsSpider(scrapy.Spider):
    name = "authors"
    start_urls = [
        'http://quotes.toscrape.com/',
    ]

    def parse(self, response):
        urls = response.css(".quote > span > a::attr(href)").extract()
        # visita as páginas dos autores
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url, callback=self.parse_author)

        # visita a próxima página
        next_page = response.css("li.next > a::attr(href)").extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_author(self, response):
        yield {
            'name': response.css("h3.author-title::text").extract_first().strip(),
            'born_date': response.css("span.author-born-date::text").extract_first()
        }





