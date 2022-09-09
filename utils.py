from bs4 import BeautifulSoup
from datetime import date, datetime

def check_literal(string):
    return any(char.isalpha() for char in string)


class AnnouncementScraper(BeautifulSoup):
    """
    Special utility class inheriting BeautifulSoup class which encapsulates
    all scraping functionality within itself.
    """

    def get_prices(self):
        prices = self.find_all('div', {'class': 'price'})
        price_results = []
        for item in prices:
            no_spaces = item.text.strip().replace(',', '')
            try:
                price_results.append({
                    'currency': no_spaces[0],
                    'price': float(no_spaces[1:])
                })
            except ValueError as e:
                price_results.append({
                    'currency': 'N/A',
                    'price': 0.0,
                })
        return price_results

    def get_images(self):
        images = self.find_all('img')
        image_sources = [str(item.get('src')) for item in images]
        return image_sources

    def get_titles(self):
        titles = self.find_all('a', {'class': 'title'})
        titles_lst = [str(i.text).strip() for i in titles]
        return titles_lst

    def get_locations(self):
        locations = self.find_all('div', {'class': 'location'})
        loc_strings = [i.find('span', {'class': ''}).text.strip() for i in locations]
        return loc_strings

    def get_beds(self):
        beds = self.find_all('span', {'class': 'bedrooms'})
        bed_strs = [str(i.text).replace('\n', '').replace(' ', '')[5:] for i in beds]
        return bed_strs

    def get_descriptions(self):
        desc = self.find_all('div', {'class': 'description'})

        desc_strs = [str(i.text).replace('\n', '') for i in desc]

        descriptions = [' '.join(i.split()) for i in desc_strs]
        return descriptions

    def get_dates(self):
        dates_tags = self.find_all('span', {'class': 'date-posted'})
        dates_strs = [' '.join(i.text.split()) for i in dates_tags]
        dates_list = [datetime.strptime(i, '%d/%m/%Y') if not check_literal(str(i)) else date.today() for i in dates_strs]
        return dates_list
