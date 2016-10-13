import scrapy


class SecondSpider(scrapy.Spider):
    name = 'second'
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                'text': quote.css("span.text::text").extract_first(),
                'author': quote.css("span > small.author::text").extract_first(),
                'tags': quote.css("a.tag::text").extract()
            }
