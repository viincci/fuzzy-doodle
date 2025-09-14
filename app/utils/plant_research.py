import wikipediaapiimport requests

import jsonfrom bs4 import BeautifulSoup

import reimport wikipediaapi

import json

class PlantResearchAssistant:

    def __init__(self):class PlantResearchAssistant:

        self.wiki = wikipediaapi.Wikipedia(    def __init__(self):

            language='en',        self.wiki = wikipediaapi.Wikipedia('SouthAfricanPlantsBlog/1.0')

            extract_format=wikipediaapi.ExtractFormat.WIKI,        self.sources = []

            user_agent='PlantBlogResearchBot/1.0'

        )    def gather_plant_info(self, plant_name, scientific_name=None, extra_context=None):

        """Gather information about a plant from multiple sources"""

    def _clean_text(self, text):        research_data = {

        """Clean wiki text by removing references and extra whitespace"""            'basic_info': self._get_wiki_info(plant_name),

        # Remove reference tags [1], [2], etc.            'scientific_data': self._get_scientific_info(scientific_name) if scientific_name else None,

        text = re.sub(r'\[\d+\]', '', text)            'conservation': self._get_sanbi_info(plant_name),

        # Remove multiple newlines            'sources': []

        text = re.sub(r'\n\s*\n', '\n\n', text)        }

        return text.strip()        

        # Combine all gathered information

    def generate_article(self, title, scientific_name='', extra_context=None):        content = []

        """        if research_data['basic_info']:

        Generate a plant article using Wikipedia data and additional context            content.append("# " + plant_name)

        """            if scientific_name:

        # Search both common and scientific names                content.append(f"\nScientific Name: *{scientific_name}*")

        page = None            if extra_context:

        search_terms = [title]                content.append(f"\n{extra_context}")

        if scientific_name:            content.append("\n## Overview")

            search_terms.append(scientific_name)            content.append(research_data['basic_info']['summary'])

            search_terms.append(f"{scientific_name} plant")            self.sources.append(research_data['basic_info']['url'])

        

        for term in search_terms:        if research_data['scientific_data']:

            page = self.wiki.page(term)            content.append("\n## Scientific Classification")

            if page.exists():            content.append(research_data['scientific_data'])

                break

                if research_data['conservation']:

        if not page or not page.exists():            content.append("\n## Conservation Status")

            raise ValueError(f"Could not find information about {title}")            content.append(research_data['conservation'])



        # Get basic information        content.append("\n## Sources")

        summary = self._clean_text(page.summary)        for source in self.sources:

                    content.append(f"- {source}")

        # Build article content

        content_parts = []        return {

                    'content': '\n\n'.join(content),

        # Add scientific name if provided            'sources': self.sources

        if scientific_name:        }

            content_parts.append(f"## Scientific Name\n{scientific_name}\n")

            def _get_wiki_info(self, plant_name):

        # Add summary section        """Get information from Wikipedia"""

        content_parts.append(f"## Overview\n{summary}\n")        page = self.wiki.page(plant_name)

                if page.exists():

        # Add conservation status and other context if provided            return {

        if extra_context:                'summary': page.summary,

            content_parts.append(f"## Conservation Information\n{extra_context}\n")                'url': page.fullurl

                    }

        # Add sections from Wikipedia        return None

        for section in page.sections:

            if any(keyword in section.title.lower() for keyword in     def _get_scientific_info(self, scientific_name):

                ['description', 'habitat', 'cultivation', 'uses', 'distribution']):        """Get scientific information about the plant"""

                clean_text = self._clean_text(section.text)        try:

                if clean_text:            # Using GBIF API for scientific classification

                    content_parts.append(f"## {section.title}\n{clean_text}\n")            url = f"https://api.gbif.org/v1/species/match?name={scientific_name}"

                    response = requests.get(url)

        # Add references            if response.status_code == 200:

        sources = [                data = response.json()

            page.fullurl,                if data.get('matchType') != 'NONE':

            "South African National Biodiversity Institute (SANBI)",                    self.sources.append(f"GBIF: https://www.gbif.org/species/{data.get('usageKey')}")

            "PlantZAfrica.com"                    return f"Scientific classification:\n- Kingdom: {data.get('kingdom')}\n- Family: {data.get('family')}\n- Genus: {data.get('genus')}\n- Species: {data.get('species')}"

        ]        except Exception as e:

        content_parts.append("\n## References\n" + "\n".join(f"- {source}" for source in sources))            print(f"Error fetching scientific data: {e}")

                return None

        return {

            'title': title,    def _get_sanbi_info(self, plant_name):

            'scientific_name': scientific_name,        """Get conservation information from SANBI"""

            'content': '\n'.join(content_parts),        try:

            'sources': sources            url = f"http://pza.sanbi.org/search/node/{plant_name}"

        }            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                results = soup.find_all('div', class_='search-result')
                if results:
                    self.sources.append(url)
                    return f"Information from SANBI database available. Visit {url} for detailed conservation status."
        except Exception as e:
            print(f"Error fetching SANBI data: {e}")
        return None

    def generate_article(self, plant_name, scientific_name=None, extra_context=None):
        """Generate a complete article about the plant"""
        research = self.gather_plant_info(plant_name, scientific_name)
        return {
            'title': plant_name,
            'scientific_name': scientific_name,
            'content': research['content'],
            'sources': research['sources'],
            'is_ai_generated': True
        }