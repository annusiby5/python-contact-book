import sqlite3
import csv
from datetime import datetime


class ContactManager:
    def __init__(self):
        self.conn = sqlite3.connect("contacts.db")
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE,
            favorite INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        self.conn.commit()

    def add_contact(self):
        name = input("Enter Name: ").strip()
        phone = input("Enter Phone: ").strip()
        email = input("Enter Email: ").strip()

        if not name or not phone:
            print("❌ Name and Phone are required.\n")
            return

        self.cursor.execute(
            "SELECT * FROM contacts WHERE phone=?",
            (phone,)
        )

        if self.cursor.fetchone():
            print("❌ Phone number already exists.\n")
            return

        try:
            self.cursor.execute(
                """
                INSERT INTO contacts(name, phone, email)
                VALUES(?,?,?)
                """,
                (name, phone, email)
            )

            self.conn.commit()
            print("✅ Contact Added Successfully.\n")

        except sqlite3.IntegrityError:
            print("❌ Email already exists.\n")

    def view_contacts(self):

        self.cursor.execute("""
        SELECT * FROM contacts
        ORDER BY name
        """)

        contacts = self.cursor.fetchall()

        if not contacts:
            print("No contacts found.\n")
            return

        print("\n📇 CONTACT LIST")
        print("-" * 90)

        for contact in contacts:
            fav = "⭐" if contact[3] else ""
            print(
                f"ID:{contact[0]} | "
                f"{contact[1]} | "
                f"{contact[2]} | "
                f"{contact[3]} | "
                f"{fav} | "
                f"{contact[5]}"
            )

        print()

    def search_contact(self):
        keyword = input("Search by name or phone: ")

        self.cursor.execute("""
        SELECT * FROM contacts
        WHERE name LIKE ?
        OR phone LIKE ?
        """, (f"%{keyword}%", f"%{keyword}%"))

        contacts = self.cursor.fetchall()

        if contacts:
            print("\n🔍 RESULTS")
            for contact in contacts:
                print(
                    f"{contact[0]} | "
                    f"{contact[1]} | "
                    f"{contact[2]} | "
                    f"{contact[3]}"
                )
            print()
        else:
            print("No contacts found.\n")

    def update_contact(self):
        contact_id = input("Enter Contact ID: ")

        self.cursor.execute(
            "SELECT * FROM contacts WHERE id=?",
            (contact_id,)
        )

        if not self.cursor.fetchone():
            print("❌ Contact not found.\n")
            return

        name = input("New Name: ")
        phone = input("New Phone: ")
        email = input("New Email: ")

        self.cursor.execute("""
        UPDATE contacts
        SET name=?, phone=?, email=?
        WHERE id=?
        """, (name, phone, email, contact_id))

        self.conn.commit()

        print("✅ Contact Updated.\n")

    def delete_contact(self):
        contact_id = input("Enter Contact ID: ")

        confirm = input(
            "Are you sure? (y/n): "
        ).lower()

        if confirm != "y":
            print("Cancelled.\n")
            return

        self.cursor.execute(
            "DELETE FROM contacts WHERE id=?",
            (contact_id,)
        )

        self.conn.commit()

        print("🗑️ Contact Deleted.\n")

    def mark_favorite(self):
        contact_id = input(
            "Enter Contact ID: "
        )

        self.cursor.execute(
            """
            UPDATE contacts
            SET favorite=1
            WHERE id=?
            """,
            (contact_id,)
        )

        self.conn.commit()

        print("⭐ Added to Favorites.\n")

    def view_favorites(self):
        self.cursor.execute("""
        SELECT * FROM contacts
        WHERE favorite=1
        """)

        contacts = self.cursor.fetchall()

        if not contacts:
            print("No favorite contacts.\n")
            return

        print("\n⭐ FAVORITES")

        for contact in contacts:
            print(
                f"{contact[0]} | "
                f"{contact[1]} | "
                f"{contact[2]}"
            )

        print()

    def statistics(self):
        self.cursor.execute(
            "SELECT COUNT(*) FROM contacts"
        )

        total = self.cursor.fetchone()[0]

        self.cursor.execute("""
        SELECT COUNT(*)
        FROM contacts
        WHERE favorite=1
        """)

        favorites = self.cursor.fetchone()[0]

        print("\n📊 STATISTICS")
        print(f"Total Contacts : {total}")
        print(f"Favorite Contacts : {favorites}\n")

    def export_csv(self):
        self.cursor.execute(
            "SELECT * FROM contacts"
        )

        contacts = self.cursor.fetchall()

        with open(
            "contacts.csv",
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "ID",
                "Name",
                "Phone",
                "Email",
                "Favorite",
                "Created At"
            ])

            writer.writerows(contacts)

        print(
            "📄 Exported to contacts.csv\n"
        )

    def menu(self):
        while True:

            print("""
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
""")

            choice = input("Choose: ")

            if choice == "1":
                self.add_contact()

            elif choice == "2":
                self.view_contacts()

            elif choice == "3":
                self.search_contact()

            elif choice == "4":
                self.update_contact()

            elif choice == "5":
                self.delete_contact()

            elif choice == "6":
                self.mark_favorite()

            elif choice == "7":
                self.view_favorites()

            elif choice == "8":
                self.statistics()

            elif choice == "9":
                self.export_csv()

            elif choice == "10":
                print("Goodbye!")
                break

            else:
                print("❌ Invalid Choice.\n")

        self.conn.close()


if __name__ == "__main__":
    app = ContactManager()
    app.menu()