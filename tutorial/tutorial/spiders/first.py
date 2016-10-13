import scrapy


class FirstSpider(scrapy.Spider):
    name = 'first'
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        filename = response.url.split('/')[-2] + '.html'
        with open(filename, 'w') as f:
            f.write(response.text)
        self.log('salvei arquivo {}'.format(filename))
