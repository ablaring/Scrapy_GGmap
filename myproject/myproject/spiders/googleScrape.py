import scrapy
from scrapy_splash import SplashRequest
import re
import csv


class BoulangerieSpider(scrapy.Spider):
    name = 'boulangerie'
    allowed_domains = ['google.fr']
    start_urls = ['https://www.google.fr/maps/place/']
    cookies = {
        "AEC": "Ackid1T-gZp8f6h0NwQq03I_wpv6bQN2xr5d_8ArYiV2mG7cCZscafdD0w",
        "CONSENT": "PENDING+725",
        "NID": "511=bsJpf5cJ0CdDAH2QmxnvGX2PCCIzrCtflJ3bIMSd8cEdTp4AccPrYJFV5uiiGaLRU9UwvRsnjeEtOeQ9LevknvK3tzwXh8FjJ71U2rClbY5hXQSU_kHXrClwdLhxCNARTfmedZaC1FtD7RWQ8OI7E9nQEtwsEAcNJiJ311C57ws",
        "SOCS": "CAISNQgEEitib3FfaWRlbnRpdHlmcm9udGVuZHVpc2VydmVyXzIwMjMxMDE3LjA0X3AwGgJmciACGgYIgO_WqQY"
    }
    row_index = 2

    def start_requests(self):
        with open('source.txt', 'r', encoding='utf-8') as file:
            for line in file:
                boulangerie = line.strip().replace(' ', '+')
                url = f"https://www.google.fr/maps/search/{boulangerie}"
                yield SplashRequest(url, self.parse_result, args={'wait': 2}, meta={'boulangerie': line},
                                    cookies=self.cookies, endpoint='render.html')

    def parse_result(self, response):
        self.row_index += 1
        boulangerie = response.meta['boulangerie']
        numbers = []
        for phone in response.xpath(
                '//div[contains(@class, "Io6YTe") and contains(@class, "fontBodyMedium") and contains(@class, "kR99db")]'):
            extracted_numbers = re.findall(r'\d{2} \d{2} \d{2} \d{2} \d{2}', phone.extract())
            numbers.extend(extracted_numbers)

        # Write the phone numbers to the 15th column (column index 14) of the CSV file
        with open('data/Sam400bdd.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            row = [''] * 14  # Create a list of 14 empty strings
            row.append(','.join(numbers))  # Add the phone numbers to the 15th column
            writer.writerow(row)  # Write the row to the CSV file
