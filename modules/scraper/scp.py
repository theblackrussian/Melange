import requests
from bs4 import BeautifulSoup
import os
import sys
from config import config

class WebScraper:

  def __init__(self, url):
    self.url = url
    self.session = requests.Session()

  def get_page(self):
    response = self.session.get(self.url)
    return response.text

  def parse_html(self, html):
    soup = BeautifulSoup(html, 'html.parser')
    return html

  def save_html(self, html):
    filename = os.path.join(config.WEBPAGE_DIR, self.get_filename())
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

  def get_filename(self):
    # Extract the slug from the URL
    slug = self.url.split('/')[-1]  # Get the last part of the URL
    # Remove URL parameters if any
    slug = slug.split('?')[0]
    # Ensure the slug ends with '.html'
    if not slug.lower().endswith('.html'):
      slug += '.html'
    return slug

if __name__ == '__main__':

  url = sys.stdin.read().strip()
  scraper = WebScraper(url)
  
  html = scraper.get_page()
  html = scraper.parse_html(html)

  scraper.save_html(html)