from transformers import pipeline
from typing import Dict, List
import json

class ArticleGenerator:
    def __init__(self):
        """Initialize the text generation and summarization models"""
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        self.generator = pipeline("text-generation", model="gpt2")

    def _generate_summary(self, text: str, max_length: int = 150) -> str:
        """Generate a summary of the text"""
        return self.summarizer(text, max_length=max_length, min_length=50)[0]['summary_text']

    def _generate_sections(self, context: str) -> str:
        """Generate article sections based on context"""
        prompt = f"Write about this plant: {context}\n\n"
        sections = self.generator(
            prompt,
            max_length=500,
            num_return_sequences=1,
            temperature=0.7
        )[0]['generated_text']
        return sections

    def generate_article(self, plant_data: Dict) -> Dict:
        """Generate a complete article from plant data"""
        # Combine plant information for context
        context = f"{plant_data['title']} ({plant_data['scientific_name']}) " \
                 f"is a plant from the {plant_data['family']} family. " \
                 f"{plant_data['description']}"

        # Generate summary
        summary = self._generate_summary(context)

        # Generate detailed sections
        cultivation = self._generate_sections(f"How to cultivate {plant_data['title']}: {plant_data['cultivation']}")
        uses = self._generate_sections(f"Uses of {plant_data['title']}: {plant_data['uses']}")

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
            'images': plant_data['images'],
            'source_url': plant_data['url'],
            'family': plant_data['family']
        }

        return article