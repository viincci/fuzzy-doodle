import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from datetime import datetime

class PlantSpider(CrawlSpider):
    name = 'plants'
    allowed_domains = ['pza.sanbi.org', 'plantzafrica.com']
    start_urls = ['http://pza.sanbi.org/plants']
    
    rules = (
        Rule(
            LinkExtractor(allow=('plants/[a-z-]+$',)),
            callback='parse_plant'
        ),
    )
    
    def parse_plant(self, response):
        """Parse plant information from PlantZAfrica"""
        plant_data = {
            'url': response.url,
            'scrape_date': datetime.now().isoformat(),
            'title': response.css('h1::text').get(),
            'scientific_name': response.css('.binomial::text').get(),
            'family': response.css('.family::text').get(),
            'description': ' '.join(response.css('.description p::text').getall()),
            'distribution': ' '.join(response.css('.distribution p::text').getall()),
            'cultivation': ' '.join(response.css('.cultivation p::text').getall()),
            'uses': ' '.join(response.css('.uses p::text').getall()),
            'images': response.css('.plant-images img::attr(src)').getall(),
        }
        
        # Clean up the data
        for key, value in plant_data.items():
            if isinstance(value, str):
                plant_data[key] = value.strip()
        
        yield plant_data