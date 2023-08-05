# Project Title

Scraping and Capturing Images from a Website

## Description

This project is a Python web application that uses the BeautifulSoup library to scrape images from a publicly available website. The scraped images are then downloaded and saved locally. The web application is built using the Django framework and allows users to trigger the image scraping process by making a HTTP request to the specified URL. The scraped images are displayed in a table format on a webpage.

## Prerequisites

- Python 3.x
- Django
- BeautifulSoup
- Requests

## Installation

1. Clone the repository: `git clone https://github.com/python-hacked/Scrape-Image.git`
2. Change to the project directory: `cd scraping-images-app`
3. Install the required dependencies: `pip install -r requirements.txt`

## Usage

1. Run the Django development server: `python manage.py runserver`
2. Open your web browser and navigate to the URL: `http://127.0.0.1:8000`
3. Enter the URL of the website you want to scrape images from and submit the form.
4. The web application will scrape the images and display them in a table format on the next page.

## How It Works

- When a user submits the URL of a website, the Django view function `scrape_and_capture_images` is triggered.
- The view function sends a request to the specified URL and parses the HTML content using BeautifulSoup to find all image tags (`<img>`).
- The image URLs are extracted from the image tags and stored in a list (`image_urls`).
- The images are then downloaded and saved locally in the `media/` directory using the `requests` library.
- The `scraped_images.html` template is rendered with the list of `image_urls`, and the images are displayed in a table format.

## Contributing

Contributions to this project are welcome. Please open an issue or submit a pull request if you find any bugs or want to add new features.

