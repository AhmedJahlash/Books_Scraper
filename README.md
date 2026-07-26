# 📚 Books Scraper

A Python web scraping project that collects book information from **Books to Scrape** website and stores the data in CSV file and SQLite database.

The project demonstrates web scraping, data processing, database storage, and creating simple reports using Python.

---

## 🚀 Project Features

- Scrape books data from multiple pages.
- Extract book information:
  - 📖 Book title
  - 💰 Price
  - 📦 Availability
- Save scraped data into CSV file.
- Store data in SQLite database.
- Search books by title.
- Display top 10 expensive books.
- Show books statistics:
  - Number of books
  - Average price
  - Highest price
  - Lowest price

---

## 🛠 Technologies Used

- Python
- Requests
- BeautifulSoup4
- SQLite
- CSV

---

## 📂 Project Structure

```
Books Scraper/
│
├── main.py              # Main program and user menu
├── scraper.py           # Web scraping functions
├── database.py          # SQLite database operations
├── reports.py           # Search and statistics functions
├── books.csv            # Exported books data
├── books.db             # SQLite database
├── README.md            # Project documentation
└── .gitignore           # Ignored files
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/AhmedJahlash/Books_Scraper.git
```

Move into the project folder:

```bash
cd Books_Scraper
```

Install required libraries:

```bash
pip install requests beautifulsoup4
```

---

## ▶️ How to Run

Run the main program:

```bash
python main.py
```

---

## 📊 Available Reports

The application provides:

### 🔎 Search Book

Search for books by title and display:

- Title
- Price
- Availability


### 💎 Top 10 Expensive Books

Displays the ten books with the highest prices.


### 📈 Statistics

Shows:

- Total number of books.
- Average book price.
- Highest price.
- Lowest price.

---

## 🗄 Database

The project uses SQLite database:

Database file:

```
books.db
```

Table:

```
books
```

Columns:

| Column | Type |
|---|---|
| id | INTEGER |
| title | TEXT |
| price | REAL |
| availability | TEXT |

---

## 📄 Output Files

The scraper generates:

### CSV File

```
books.csv
```

Contains all collected books information.

### SQLite Database

```
books.db
```

Stores books data for searching and reporting.

---

## 👨‍💻 Author

**Ahmed Jahlash**

---

## 📌 Future Improvements

- Add graphical interface using Tkinter.
- Export reports to Excel.
- Add automatic scheduled scraping.
- Add more data analysis features.