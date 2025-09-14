import wikipediaapi
import requests
from bs4 import BeautifulSoup
import json

class PlantDataFetcher:
    def __init__(self):
        self.wiki = wikipediaapi.Wikipedia('SouthAfricanPlantsBlog/1.0 (viincci@github.com)')
    
    def get_wikipedia_data(self, plant_name):
        """
        Fetch plant information from Wikipedia
        """
        page = self.wiki.page(plant_name)
        if not page.exists():
            return None
        
        return {
            'title': page.title,
            'summary': page.summary,
            'url': page.fullurl,
            'references': [ref for ref in page.references],
        }
    
    def search_inaturalist(self, scientific_name):
        """
        Search iNaturalist for plant observations in South Africa
        """
        base_url = "https://api.inaturalist.org/v1/observations"
        params = {
            "taxon_name": scientific_name,
            "place_id": 7017, # South Africa
            "per_page": 5,
            "order": "desc",
            "order_by": "created_at"
        }
        
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            if data['total_results'] > 0:
                return data['results']
        return None

    def get_sanbi_data(self, plant_name):
        """
        Fetch data from South African National Biodiversity Institute (SANBI)
        Using their public website as they don't have a public API
        """
        url = f"http://pza.sanbi.org/search/node/{plant_name}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                # Extract relevant information from SANBI website
                # This is a basic implementation and might need adjustment
                results = soup.find_all('div', class_='search-result')
                if results:
                    return {
                        'url': results[0].find('a')['href'],
                        'description': results[0].find('p').text.strip()
                    }
        except Exception as e:
            print(f"Error fetching SANBI data: {e}")
        return None

    def compile_plant_data(self, plant_name, scientific_name=None):
        """
        Compile data from multiple sources
        """
        data = {
            'title': plant_name,
            'scientific_name': scientific_name,
            'content': '',
            'references': [],
            'image_url': None,
            'source_urls': []
        }
        
        # Get Wikipedia data
        wiki_data = self.get_wikipedia_data(plant_name)
        if wiki_data:
            data['content'] = wiki_data['summary']
            data['references'].extend(wiki_data['references'])
            data['source_urls'].append(wiki_data['url'])
        
        # Get iNaturalist data if scientific name is provided
        if scientific_name:
            inat_data = self.search_inaturalist(scientific_name)
            if inat_data and len(inat_data) > 0:
                # Get the first observation with a photo
                for obs in inat_data:
                    if obs.get('photos') and len(obs['photos']) > 0:
                        data['image_url'] = obs['photos'][0]['url']
                        break
        
        # Get SANBI data
        sanbi_data = self.get_sanbi_data(plant_name)
        if sanbi_data:
            data['content'] += f"\n\nAdditional information from SANBI:\n{sanbi_data['description']}"
            data['source_urls'].append(sanbi_data['url'])
        
        # Convert references and source_urls to JSON strings for storage
        data['references'] = json.dumps(data['references'])
        data['source_urls'] = json.dumps(data['source_urls'])
        
        return data