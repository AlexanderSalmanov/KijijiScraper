from bs4 import BeautifulSoup
import requests
from datetime import datetime, date
from utils import AnnouncementScraper

from db import SessionLocal
from models import Announcement

with SessionLocal() as session:
    """
    Deleting all Announcements each time the program runs.
    The main purpose is not to overpopulate the database.
    """
    session.query(Announcement).delete()
    session.commit()


base_url = 'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273'

base_html = requests.get(base_url).text

soup = BeautifulSoup(base_html, 'html.parser')

# This section is necessary for getting the number of pages via total announcement
# count divided by 40 (number of announcements per page)
announcement_count_tag = soup.find('span', {'class': 'resultsShowingCount-1707762110'})

res_count = int(announcement_count_tag.text.split()[-2])

total_pages = res_count // 40
pages = list(range(1, total_pages+1))

# From now, we can start iterating through pages
for page in pages:
    url = f'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-2/c37l1700273?ad=offering'
    html = requests.get(url)
    ann_scraper = AnnouncementScraper(html.text, 'html.parser')
    ads_container = ann_scraper.find_all('div', {'class': 'container-results large-images'})[1]

    prices = ann_scraper.get_prices()

    images = ann_scraper.get_images()

    titles = ann_scraper.get_titles()

    locations = ann_scraper.get_locations()

    beds = ann_scraper.get_beds()

    descriptions = ann_scraper.get_descriptions()

    dates = ann_scraper.get_dates()

    objects = [Announcement(
        title=titles[i],
        location=locations[i],
        date=dates[i],
        price=prices[i].get('price'),
        currency=prices[i].get('currency'),
        beds=beds[i],
        description=descriptions[i],
        image_url=images[i]
    ) for i in range(len(prices))]

    with SessionLocal() as session:
        session.bulk_save_objects(objects)
        session.commit()
