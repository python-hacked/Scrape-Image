import os
import requests
from bs4 import BeautifulSoup
from django.conf import settings
from django.shortcuts import render

def scrape_and_capture_images(request):
    url = 'https://www.amazon.in/mobile-phones/b/?ie=UTF8&node=1389401031&ref_=nav_cs_mobiles_9292c6cb7b394d30b2467b8f631090a7'  # Replace with the website you want to scrape
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Write your scraping logic here using BeautifulSoup

    # For image scraping, find image tags and capture the image URLs
    image_urls = [img['src'] for img in soup.find_all('img')]

    # Download and save images locally (you can modify this according to your needs)
    for img_url in image_urls:
        image_data = requests.get(img_url).content
        filename = os.path.basename(img_url)

        # Ensure the 'media' folder exists before saving the images
        media_folder = settings.MEDIA_ROOT
        if not os.path.exists(media_folder):
            os.makedirs(media_folder)

        with open(os.path.join(media_folder, filename), 'wb') as f:
            f.write(image_data)

    return render(request, 'scraped_images.html', {'image_urls': image_urls})
