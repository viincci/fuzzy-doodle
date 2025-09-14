import json
import os
from app.utils.article_generator import ArticleGenerator
from app import db, Post

def main():
    # Load scraped plant data
    with open('data/plants.json', 'r') as f:
        plants = json.load(f)
    
    # Initialize article generator
    generator = ArticleGenerator()
    
    # Generate articles for each plant
    for plant_data in plants:
        try:
            # Check if article already exists
            existing = Post.query.filter_by(
                title=plant_data['title'],
                scientific_name=plant_data['scientific_name']
            ).first()
            
            if existing:
                continue  # Skip if article exists
                
            # Generate article
            article = generator.generate_article(plant_data)
            
            # Create new post
            post = Post(
                title=article['title'],
                scientific_name=article['scientific_name'],
                content=article['content'],
                source_urls=json.dumps([article['source_url']]),
                categories='South African Plants',
                is_ai_generated=True,
                author='MrJBlack'
            )
            
            # Save to database
            db.session.add(post)
            db.session.commit()
            
            print(f"Generated article for {article['title']}")
            
        except Exception as e:
            print(f"Error generating article for {plant_data['title']}: {str(e)}")
            continue

if __name__ == '__main__':
    main()