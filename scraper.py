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

        if page == 1:
            url = "https://books.toscrape.com/"
        else:
            url = f"https://books.toscrape.com/catalogue/page-{page}.html"

        response = requests.get(url)
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

            books_data.append({
                "title": link["title"],
                "price": price,
                "availability": availability.text.strip()
            })

    return books_data

