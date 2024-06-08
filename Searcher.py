import os
import requests
from bs4 import BeautifulSoup

def google_search(query, num_results=50):
    api_key = os.environ["GOOGLE_API_KEY"]
    cse_id = os.environ["GOOGLE_CSE_ID"]
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={cse_id}&num=50"
    response = requests.get(url)
    results = []
    if response.status_code == 200:
        search_results = response.json().get('items', [])
        for result in search_results:
            title = result.get('title', 'No Title')
            link = result.get('link', '')
            results.append((title, link))
    return results

def get_title(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.title.string if soup.title else 'No Title'
    except requests.RequestException:
        return 'No Title'
