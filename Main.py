# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 17:32:11 2026

@author: lenovo
"""


    



import csv

   
from scraper import scrape_books
from database import (
    create_table,
    insert_books,
    close_connection
)
from reports import (
    search_book,
    top_10_expensive_books,
    statistics,
    books_by_rating,
    search_books_by_price
)

books_data = scrape_books()
if not books_data:
    print("No data was scraped. Program stopped.")
    close_connection()
    exit()

create_table()
insert_books(books_data)

        
with open("books.csv", "w", newline="", encoding="utf-8") as file:
    
    writer = csv.writer(file)
    writer.writerow(["title", "price", "availability", "rating"])
    for book in books_data:
        writer.writerow([
            book["title"],
            book["price"],
            book["availability"],
            book.get("rating")
        ])  


       

while True:

    print("\n=== Books Scraper ===")
    print("1. Search Book")
    print("2. Top 10 Expensive Books")
    print("3. Statistics")
    print("4. Books by Rating")
    print("5. search_books_by_price")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == "1":
        search_book()

    elif choice == "2":
        top_10_expensive_books()

    elif choice == "3":
        statistics()
        
    elif choice == "4":
        books_by_rating()
        
    elif choice == "5":
        search_books_by_price()

    elif choice == "6":
        close_connection()
        print("Goodbye!")
        break

    else:
        print("Invalid choice")

    







   


    
    
    