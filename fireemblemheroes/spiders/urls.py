import scrapy
from scrapy_splash import SplashRequest
from urllib.parse import urljoin

class UrlSpider(scrapy.Spider):
    name = "link"

    def start_requests(self):
        pages = "https://fireemblem.gamepress.gg/heroes"
        yield SplashRequest(url=pages, callback=self.parse, endpoint='render.html', args={'wait': 0.5})

    def parse(self, response):
        heroes = 'https://fireemblem.gamepress.gg/heroes'
        for page in response.selector.xpath('//tbody[@id="hero-sort-table"]/tr'):
            url = page.xpath('.//td/a[1]/@href').extract_first()
            yield {
                'urls': urljoin(heroes, url)
            }

