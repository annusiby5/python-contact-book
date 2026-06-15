# python-contact-book

A menu driven Contact Management System built with **Python** and **SQLite**, allows users to efficiently store, manage, search, and organize contacts with features such as favorites, statistics and CSV export.

## Features

* ➕ Add new contacts
* 📋 View all contacts
* 🔍 Search contacts by name or phone number
* ✏️ Update existing contacts
* 🗑️ Delete contacts
* ⭐ Mark contacts as favorites
* 📂 View favorite contacts
* 📊 Contact statistics dashboard
* 📄 Export contacts to CSV
* 🛡️ Duplicate phone and email prevention
* 🕒 Automatic contact creation timestamps
* 🗄️ Persistent storage using SQLite

## Technologies Used

* Python
* SQLite3
* CSV

## Project Structure

```text
ContactVault/
│
├── contact_book.py
├── contacts.db
├── contacts.csv
├── README.md
├── LICENSE
└── .gitignore
```

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/python-contact-book.git
cd python-contact-book
```

### Run the Application

```bash
python contact_book.py
```

## Menu Options

```text
📖 CONTACT MANAGEMENT SYSTEM

1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Mark Favorite
7. View Favorites
8. Statistics
9. Export CSV
10. Exit
```

## Database Schema

```sql
CREATE TABLE contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE,
    favorite INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```



## Future Enhancements

* GUI using Tkinter
* User Authentication
* Password Hashing
* Import Contacts from CSV
* Contact Profile Pictures
* Dark/Light Theme
* Database Backup & Restore
* Birthday Reminders
* Unit Testing with Pytest

## Learning Outcomes

This project demonstrates:

* Object-Oriented Programming (OOP)
* SQLite Database Integration
* CRUD Operations
* File Handling
* Data Validation
* Command Line Application Development

## License

This project is open source and available under the MIT License.
