# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 10:20:28 2026

@author: lenovo
"""

import sqlite3

conn = sqlite3.connect("books.db")
cursor = conn.cursor()



def create_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL UNIQUE,
            price REAL NOT NULL,
            availability TEXT NOT NULL
        )
    """)
    conn.commit()


def insert_books(books_data):

    cursor.execute("DELETE FROM books")
    conn.commit()

    unique_books = {}

    for book in books_data:
        unique_books[book["title"]] = book

    for book in unique_books.values():
        cursor.execute("""
            INSERT INTO books (title, price, availability)
            VALUES (?, ?, ?)
        """, (
            book["title"],
            book["price"],
            book["availability"]
        ))

    conn.commit()
    
def close_connection():
    conn.close()
    
    
