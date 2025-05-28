Book Tracker CLI (Summary)
Book Tracker CLI is a terminal-based app that helps you manage your reading life. You can add books, track their status (like "Want to Read", "Currently Reading", or "Finished Reading"), and view or update your list anytime — all from the command line.

✅ Key Features
Create and log into your user profile

Add books with title and author

Assign a reading status to each book

View, update, or delete books

Simple and easy-to-navigate CLI interface

🧰 Tech Stack
Python

SQLite (database)

SQLAlchemy (ORM)

Basic input/output functions for the CLI

🗂 Project Folders
models/: Defines User, Book, and ReadingStatus

controllers/: Handles logic like adding books or users

db/: Contains schema.py to create the database tables

Pipfile and Pipfile lock: Keep the dependencies locked for the project

cli.py : Main file to launch the app

🏁 How to Use
Clone the project

Set up your environment and install dependencies

Run the schema.py to create the database tables

Launch the app with python -m lib.cli

Follow on-screen prompts to add and manage your books

🔮 Future Ideas
Add reviews or ratings

Export reading list to file

Online API integration for book lookup

👤 Author
Benson Kariuki– GitHub: munge124

