import scrapy


class ThirdSpider(scrapy.Spider):
    name = 'third'
    start_urls = [
        'http://quotes.toscrape.com',
    ]

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                'text': quote.css("span.text::text").extract_frst(),
                'author': quote.css("span > small.author::text").extract_first(),
                'tags': quote.css("a.tag::text").extract()
            }

        next_page = response.css("li.next > a::attr(href)").extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
