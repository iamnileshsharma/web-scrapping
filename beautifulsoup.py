# Web scraper to archive BBC headlines daily
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_bbc_news():
    url = "https://www.bbc.com/"
    response = requests.get(url)
    
    if response.status_code == 200:
        timestamp = datetime.now().strftime("%m.%d.%Y")
        filename = f"bbc_headlines_{timestamp}.txt"
        
        soup = BeautifulSoup(response.text, "lxml")
        news_items = soup.find_all("div", class_="sc-666b6d83-0 jSTfiy")
        
        with open(filename, "w") as file:
            file.write(f"BBC Headlines ({timestamp}):\n\n")
            for item in news_items:
                headline = item.find("h2").text.strip()
                summary = item.find("p").text.strip()
                file.write(f"Headline: {headline}\nSummary: {summary}\n\n")
        print(f"Successfully saved to {filename}!")
    else:
        print("Failed to fetch data")

if __name__ == "__main__":
    scrape_bbc_news()
