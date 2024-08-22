import scrapy
from scrapy.crawler import CrawlerProcess

class EsgSpider(scrapy.Spider):
    name = "esg_spider"

    def __init__(self, links=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = links or []

    def parse(self, response):
        yield {
            'title': response.css('title::text').get(),
            'url': response.url,
            'content': ' '.join(response.css('p::text').getall()),
        }

def run_scraper(links):
    process = CrawlerProcess(settings={
        "FEEDS": {
            "output/output.csv": {"format": "csv"},
        },
        "LOG_LEVEL": "INFO",
    })
    process.crawl(EsgSpider, links=links)
    process.start()
