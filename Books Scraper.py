# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 17:32:11 2026

@author: lenovo
"""

import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url)

print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article")

books_data = []

for book in books:
    link = book.find("a")
    price = book.find("p", class_="price_color")
    availability = book.find("p", class_="instock availability")

    print(link["title"])
    print(price.text)
    print(availability.text.strip())
    
''''''''''''

import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article")

books_data = []

for book in books:
    link = book.find("h3").find("a")
    price_text = book.find("p", class_="price_color").text
    price = float(
    "".join(c for c in price_text if c.isdigit() or c == "."))
    
    availability = book.find("p", class_="instock availability")

    book_data = {
        "title": link["title"],
        "price": price.text,
        "availability": availability.text.strip()
    }

    books_data.append(book_data)
    


for book in books_data:
   
   
    print(
          f"Title: {book['title']}, "
          f"Price: {book['price']}, "
          f"Availability: {book['availability']}")
    
with open("books.csv", "w", newline="", encoding="utf-8") as file:
    
    writer = csv.writer(file)
    writer.writerow(["title", "price", "availability"])
    for book in books_data:
        writer.writerow([
            book["title"],
            book["price"],
            book["availability"]
        ])   
   
import sqlite3

conn = sqlite3.connect("books.db")
cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    price REAL NOT NULL,
    availability TEXT NOT NULL
)
                  
               """)
         
for book in books_data:
    cursor.execute("""
    INSERT INTO books (title, price, availability)
    VALUES (?, ?, ?)
    """, (
        book["title"],
        book["price"],
        book["availability"]
    ))

    conn.commit()


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
        "".join(c for c in price_text if c.isdigit() or c == "."))
        
        availability = book.find("p", class_="instock availability")

        book_data = {
            "title": link["title"],
            "price": price,
            "availability": availability.text.strip()
        }

        books_data.append(book_data)
        
        
print(len(books_data))
    
def search_book():
    
    
    try:
        book_name = input("Enter book name: ")

        cursor.execute("""
SELECT b.title, b.price, b.availability
FROM books b
WHERE b.title LIKE ?
ORDER BY b.price ASC
""", (f"%{book_name}%",))

        rows = cursor.fetchall()

        if not rows:
            print("book not found.")
        else:
            print("\n--- books List ---")
            for row in rows:
                print(f"title: {row[0]}, price: {row[1]}, availability : {row[2]}")

    except Exception as e:
        print("حدث خطأ:", e)
    
def top_10_expensive_books():
    cursor.execute("""
SELECT title, price, availability
FROM books
ORDER BY price DESC
LIMIT 10
""")
    rows =  cursor.fetchall()
    for row in rows:
       
       
       print(f"Title: {row[0]}")
       print(f"Price: £{row[1]:.2f}")
       print(f"Availability: {row[2]}")
       print("-" * 40)
       
 


    

def statistics():
    cursor.execute("""
                   SELECT COUNT(*), AVG(price), MAX(price),MIN(price) 
                   FROM books
                   """)
                   

    row = cursor.fetchone()
    
    print("\n----- Books Statistics -----")
    print(f"📚 Number of books: {row[0]}")
    print(f"💰 Average price: £{row[1]:.2f}")
    print(f"🔺 Highest price: £{row[2]:.2f}")
    print(f"🔻 Lowest price: £{row[3]:.2f}")
   
    
   

search_book()



top_10_expensive_books()

statistics()

cursor.execute("""
               DROP TABLE IF EXISTS books
 
               
               """)
    
    
    
    