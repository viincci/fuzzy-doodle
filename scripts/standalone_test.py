from transformers import pipeline
import json
import os

class ArticleGenerator:
    def __init__(self):
        """Initialize the text generation and summarization models"""
        print("Initializing models...")
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        self.generator = pipeline("text-generation", model="gpt2")
        print("Models initialized!")

    def _generate_summary(self, text: str, max_length: int = 150) -> str:
        """Generate a summary of the text"""
        print("Generating summary...")
        return self.summarizer(text, max_length=max_length, min_length=50)[0]['summary_text']

    def _generate_sections(self, context: str) -> str:
        """Generate article sections based on context"""
        print(f"Generating section for context: {context[:100]}...")
        sections = self.generator(
            context,
            max_length=500,
            num_return_sequences=1,
            temperature=0.7
        )[0]['generated_text']
        return sections

    def generate_article(self, plant_data: dict) -> dict:
        """Generate a complete article from plant data"""
        print(f"Generating article for {plant_data['title']}...")
        
        # Combine plant information for context
        context = f"{plant_data['title']} ({plant_data['scientific_name']}) " \
                 f"is a plant from the {plant_data['family']} family. " \
                 f"{plant_data['description']}"

        # Generate summary
        summary = self._generate_summary(context)
        print("Summary generated!")

        # Generate detailed sections
        print("Generating detailed sections...")
        cultivation = self._generate_sections(f"How to cultivate {plant_data['title']}: {plant_data['cultivation']}")
        uses = self._generate_sections(f"Uses of {plant_data['title']}: {plant_data['uses']}")
        print("Sections generated!")

        # Compile article
        article = {
            'title': plant_data['title'],
            'scientific_name': plant_data['scientific_name'],
            'content': f"""# {plant_data['title']}

## Overview
{summary}

## Description
{plant_data['description']}

## Distribution
{plant_data['distribution']}

## Cultivation
{cultivation}

## Uses and Cultural Significance
{uses}

## References
- PlantZAfrica
- SANBI Database
""",
            'images': plant_data.get('images', []),
            'source_url': plant_data.get('url', ''),
            'family': plant_data['family']
        }

        return article

def test_article_generation():
    """Test article generation with a single plant"""
    # Test plant data
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
        json.dump(test_plant, f, indent=2)
    print("Test data saved to data/test_plant.json")

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