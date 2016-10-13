import scrapy


class LoginSpider(scrapy.Spider):
    name = 'login'
    start_urls = ['http://quotes.toscrape.com/login']

    def parse(self, response):
        csrf_token = response.css("input[name=csrf_token]::attr(value)").extract_first()
        yield scrapy.FormRequest(
            'http://quotes.toscrape.com/login',
            formdata={
                'username': 'tantofaz',
                'password': '...',
                'csrf_token': csrf_token
            },
            callback=self.parse_logged_in
        )

    def parse_logged_in(self, response):
        for quote in response.css("div.quote"):
            gr_url = quote.css("span > a:last-child::attr(href)").extract_first()
            if gr_url is not None:
                yield scrapy.Request(gr_url, callback=self.parse_gr)

    def parse_gr(self, response):
        self.log("visitei: {}".format(response.url))
