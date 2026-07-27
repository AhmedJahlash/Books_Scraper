# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 10:07:50 2026

@author: lenovo
"""

import requests
from bs4 import BeautifulSoup


def scrape_books():

    books_data = []

    for page in range(1, 51):
        print(f"Scraping page {page}/50...")

        if page == 1:
            url = "https://books.toscrape.com/"
        else:
            url = f"https://books.toscrape.com/catalogue/page-{page}.html"

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
        except requests.exceptions.RequestException as e:
            print(f"Error while connecting to the website: {e}")
            return []

        soup = BeautifulSoup(response.text, "html.parser")
        books = soup.find_all("article")

        for book in books:
            link = book.find("h3").find("a")

            price_text = book.find("p", class_="price_color").text
            price = float(
                "".join(c for c in price_text if c.isdigit() or c == ".")
            )

            availability = book.find(
                "p",
                class_="instock availability"
            )
            rating = book.find("p", class_="star-rating")
            rating = rating["class"][1]

            books_data.append({
                "title": link["title"],
                "price": price,
                "availability": availability.text.strip(),
                "rating": rating
                
            })

    return books_data

