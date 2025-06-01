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


def calculate_median(votes_by_rating, total_voters):
    """Calculate the median rating from vote distribution."""
    if not votes_by_rating or total_voters == 0:
        return 0
    
    # Sort by rating (ascending order)
    votes_by_rating.sort(key=lambda x: x[0])
    
    # Find median position
    median_pos = total_voters / 2
    
    # Count cumulative votes to find median
    cumulative_votes = 0
    for rating, votes in votes_by_rating:
        cumulative_votes += votes
        if cumulative_votes >= median_pos:
            return rating
    
    # Fallback (shouldn't reach here)
    return votes_by_rating[-1][0]


def extract_rating_from_page(html_content, url):
    """Extract the rating from a race rating page."""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    try:
        # Find the polls section
        polls_div = soup.find('div', class_='wp-polls')
        if not polls_div:
            return {"url": url, "rating": "No poll found", "votes": 0}
        
        # Extract total voters - look for "Total Voters: <strong>198</strong>"
        total_voters_text = polls_div.get_text()
        total_voters_match = re.search(r'Total Voters:\s*(\d+)', total_voters_text)
        if not total_voters_match:
            return {"url": url, "rating": "No voter count found", "votes": 0}
        
        total_voters = int(total_voters_match.group(1))
        
        # Extract ratings and percentages
        rating_items = polls_div.find_all('li')
        if not rating_items:
            return {"url": url, "rating": "No ratings found", "votes": total_voters, "median": "N/A"}
        
        total_weighted_score = 0
        votes_by_rating = []
        
        for item in rating_items:
            item_text = item.get_text(strip=True)
            
            # Parse format like "10 (2%)"
            parts = item_text.split('(')
            if len(parts) != 2:
                continue
                
            rating_str = parts[0].strip()
            percentage_str = parts[1].rstrip('%)').strip()
            
            try:
                rating = int(rating_str)
                percentage = float(percentage_str)
                
                # Calculate votes for this rating
                votes_for_rating = round((percentage / 100) * total_voters)
                
                # Store for median calculation
                votes_by_rating.append((rating, votes_for_rating))
                
                # Add to weighted score
                total_weighted_score += rating * votes_for_rating
                
            except (ValueError, IndexError):
                continue
        
        # Calculate median
        median_rating = calculate_median(votes_by_rating, total_voters)
        
        # Calculate average rating
        if total_voters > 0:
            average_rating = total_weighted_score / total_voters
            return {
                "url": url, 
                "rating": f"{average_rating:.2f}", 
                "votes": total_voters,
                "median": f"{median_rating:.1f}"
            }
        else:
            return {"url": url, "rating": "No votes", "votes": 0, "median": "N/A"}
            
    except Exception as e:
        return {"url": url, "rating": f"Error: {e}", "votes": 0, "median": "N/A"}


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
            print(f"  Median: {rating_info['median']}")
            print(f"  Votes: {rating_info['votes']}")
        else:
            print(f"  Failed to download page")


if __name__ == "__main__":
    main()
