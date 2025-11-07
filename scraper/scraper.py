from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import os
from urllib.parse import urljoin

url = 'https://voguescovers.blogspot.com/p/blog-page_1.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

image_info_list = []
urls = []

print(soup.title.text)
buttons = soup.find_all('a')


def extract_region_from_url(link):
    match = re.search(r'vogue-(\w+)\.html', link)
    if match:
        return match.group(1)
    else:
        return None


def scrape_images(link, region):
    print("Starting download for " + region + "...")
    image_response = requests.get(link)
    image_soup = BeautifulSoup(image_response.text, 'html.parser')

    main_div = image_soup.find('div', {'class': 'post-body entry-content'})

    output_folder = 'images'
    os.makedirs(output_folder, exist_ok=True)

    image_links = main_div.find_all('a', href=True)

    for i, image_link in enumerate(image_links):
        image_url = urljoin(link, image_link['href'])

        image_name = f'{region}_{i + 1}.jpg'
        image_path = os.path.join(output_folder, image_name)

        image_response = requests.get(image_url)

        with open(image_path, 'wb') as img_file:
            img_file.write(image_response.content)

        image_info = {
            'name': image_name,
            'region': region,
            'url': image_url
        }

        image_info_list.append(image_info)
    print("Finished download for " + region)


for button in buttons:
    button_url = button.get('href')

    if button_url is None:
        continue

    if "http://voguescovers.blogspot.com/p/vogue-" in button_url:
        urls.append(button_url)
        scrape_images(button_url, extract_region_from_url(button_url))

print("Saving csv ...")
df = pd.DataFrame(image_info_list)
df.to_csv('image_info.csv', index=False)
print("Saved csv")
