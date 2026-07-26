# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 10:27:46 2026

@author: lenovo
"""

from database import cursor

def search_book():

    try:
        book_name = input("Enter book name: ")

        cursor.execute("""
            SELECT title, price, availability
            FROM books
            WHERE title LIKE ?
            ORDER BY price ASC
        """, (f"%{book_name}%",))

        rows = cursor.fetchall()

        if not rows:
            print("Book not found.")
        else:
            print("\n--- Books List ---")
            for row in rows:
                print(f"Title: {row[0]}")
                print(f"Price: £{row[1]:.2f}")
                print(f"Availability: {row[2]}")
                print("-" * 40)

    except Exception as e:
        print("حدث خطأ:", e)
        
def top_10_expensive_books():

    cursor.execute("""
        SELECT title, price, availability
        FROM books
        ORDER BY price DESC
        LIMIT 10
    """)

    rows = cursor.fetchall()

    for row in rows:
        print(f"Title: {row[0]}")
        print(f"Price: £{row[1]:.2f}")
        print(f"Availability: {row[2]}")
        print("-" * 40)
        
def statistics():

    cursor.execute("""
        SELECT COUNT(*), AVG(price), MAX(price), MIN(price)
        FROM books
    """)

    row = cursor.fetchone()

    print("\n----- Books Statistics -----")
    print(f"📚 Number of books: {row[0]}")
    print(f"💰 Average price: £{row[1]:.2f}")
    print(f"🔺 Highest price: £{row[2]:.2f}")
    print(f"🔻 Lowest price: £{row[3]:.2f}")