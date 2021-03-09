import requests
from selectorlib import Extractor




class Temperature:

    """
    scrapes temperature from timeanddate.com/weather
    """


    def __init__(self, country, city):
        self.country = country
        self.city = city

    def get(self):
        url = f'https://www.timeanddate.com/weather/{self.country}/{self.city}'
        r = requests.get(url)
        c = r.content

        extractor = Extractor.from_yaml_file('temperature.yaml')

        extracted_temp = extractor.extract(str(c))

        just_temperature = float(extracted_temp['temp'].replace("\xa0\\xc2\\xb0C", ""))

        return just_temperature







