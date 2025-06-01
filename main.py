import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin


def extract_race_urls(html_content):
    """Extract race rating post URLs from the index page HTML."""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find all articles with race rating posts
    articles = soup.find_all('article', class_=re.compile(r'.*rate-the-race.*'))
    
    race_urls = []
    for article in articles:
        # Find the entry title link
        title_link = article.find('h2', class_='entry-title')
        if title_link:
            link = title_link.find('a')
            if link and link.get('href'):
                race_urls.append(link['href'])
    
    return race_urls


def download_page(url):
    """Download a web page and return its content."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error downloading {url}: {e}")
        return None


def extract_rating_from_page(html_content, url):
    """Extract the rating from a race rating page."""
    # This will need to be implemented based on the structure of individual race pages
    # For now, return a placeholder
    return {"url": url, "rating": "TBD"}


def main():
    print("F1 Race Rating Extractor")
    print("=" * 40)
    
    # Download the latest index page from RaceFans
    index_url = "https://www.racefans.net/category/regular-features/rate-the-race/"
    print(f"Downloading index page: {index_url}")
    
    index_content = download_page(index_url)
    if not index_content:
        print("Error: Failed to download index page")
        return
    
    # Extract race URLs from index page
    race_urls = extract_race_urls(index_content)
    print(f"Found {len(race_urls)} race rating posts:")
    
    for url in race_urls:
        print(f"  - {url}")
    
    print("\nDownloading individual race pages...")
    
    # Download each race page and extract ratings
    for url in race_urls:
        print(f"\nProcessing: {url}")
        page_content = download_page(url)
        
        if page_content:
            rating_info = extract_rating_from_page(page_content, url)
            race_name = url.split('/')[-2].replace('-', ' ').title()
            print(f"  Race: {race_name}")
            print(f"  Rating: {rating_info['rating']}")
        else:
            print(f"  Failed to download page")


if __name__ == "__main__":
    main()
