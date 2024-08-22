import scrapy
from scrapy.crawler import CrawlerProcess

class EsgSpider(scrapy.Spider):
    name = "esg_spider"

    def __init__(self, links=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = links or []

    def parse(self, response):
        title = response.css('title::text').get(default='No title')
        url = response.url
        content = ' '.join(response.css('p::text').getall() or ['No content'])
        
        yield {
            'title': title,
            'url': url,
            'content': content,
        }

def run_scraper(links):
    process = CrawlerProcess(settings={
        "FEEDS": {
            "output/output.csv": {"format": "csv"},
        },
        "LOG_LEVEL": "INFO",
        "LOG_FORMAT": '%(asctime)s [%(name)s] [%(levelname)s] %(message)s',
        "LOG_FILE": "output/scraper.log",
        "RETRY_TIMES": 3,
        "DOWNLOAD_DELAY": 1,
        "CONCURRENT_REQUESTS": 32,
        "ITEM_PIPELINES": {
            'backend.pipelines.DataCleaningPipeline': 300,
        },
        "HTTPCACHE_ENABLED": True,
        "HTTPCACHE_EXPIRATION_SECS": 86400,
        "HTTPCACHE_DIR": 'httpcache',
        "AUTOTHROTTLE_ENABLED": True,
        "AUTOTHROTTLE_START_DELAY": 5,
        "AUTOTHROTTLE_MAX_DELAY": 60,
    })
    process.crawl(EsgSpider, links=links)
    process.start()
