from app.utils.article_generator import ArticleGenerator
from app.spiders.plant_spider import PlantSpider
from scrapy.crawler import CrawlerProcess
import json
import os

def run_spider():
    """Run the spider and save results"""
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'FEED_FORMAT': 'json',
        'FEED_URI': 'data/plants_test.json',
        'LOG_LEVEL': 'INFO'
    })
    
    process.crawl(PlantSpider)
    process.start()

def test_article_generation():
    """Test article generation with a single plant"""
    # First, create a test plant data
    test_plant = {
        'title': 'King Protea',
        'scientific_name': 'Protea cynaroides',
        'family': 'Proteaceae',
        'description': 'The King Protea is a distinctive flowering plant, with what is possibly the largest flower head in the genus. The species is also known as Giant Protea, Honeypot or King Sugar Bush.',
        'distribution': 'Native to the south-western and southern parts of South Africa in the Western and Eastern Cape provinces.',
        'cultivation': 'Grows in well-drained, acidic soil in an open, sunny position. Requires good air circulation and minimal disturbance to its roots.',
        'uses': 'Popular as cut flowers and as a garden plant. National flower of South Africa.',
        'url': 'http://pza.sanbi.org/protea-cynaroides',
        'images': ['http://pza.sanbi.org/sites/default/files/protea_cynaroides.jpg']
    }

    # Save test data
    os.makedirs('data', exist_ok=True)
    with open('data/test_plant.json', 'w') as f:
        json.dump(test_plant, f)

    # Initialize article generator
    generator = ArticleGenerator()

    try:
        # Generate article
        article = generator.generate_article(test_plant)
        
        # Save generated article
        with open('data/test_article.md', 'w') as f:
            f.write(f"# Generated Article for {article['title']}\n\n")
            f.write(article['content'])
        
        print("\n=== Article Generation Test Results ===")
        print(f"Title: {article['title']}")
        print(f"Scientific Name: {article['scientific_name']}")
        print(f"Content Length: {len(article['content'])} characters")
        print(f"Output saved to: data/test_article.md")
        print("=====================================")
        
        return True
    except Exception as e:
        print(f"Error generating article: {str(e)}")
        return False

if __name__ == '__main__':
    print("Starting article generation test...")
    success = test_article_generation()
    print(f"\nTest {'successful' if success else 'failed'}")