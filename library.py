import mysql.connector

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vignesh@2008",
    database="library_db"
)

cursor = db.cursor()

while True:

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Update Book")
    print("4. Delete Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # CREATE - Add Book
    if choice == "1":

        book_id = int(input("Enter Book ID: "))
        book_name = input("Enter Book Name: ")
        author = input("Enter Author Name: ")
        quantity = int(input("Enter Quantity: "))

        sql = "INSERT INTO books VALUES (%s, %s, %s, %s)"
        values = (book_id, book_name, author, quantity)

        cursor.execute(sql, values)
        db.commit()

        print("Book added successfully!")

    # READ - View Books
    elif choice == "2":

        cursor.execute("SELECT * FROM books")

        books = cursor.fetchall()

        print("\nID | Book Name | Author | Quantity")
        print("-----------------------------------")

        for book in books:
            print(book)

    # UPDATE - Update Book
    elif choice == "3":

        book_id = int(input("Enter Book ID to update: "))
        book_name = input("Enter new Book Name: ")
        author = input("Enter new Author Name: ")
        quantity = int(input("Enter new Quantity: "))

        sql = """
        UPDATE books
        SET book_name = %s, author = %s, quantity = %s
        WHERE book_id = %s
        """

        values = (book_name, author, quantity, book_id)

        cursor.execute(sql, values)
        db.commit()

        print("Book updated successfully!")

    # DELETE - Delete Book
    elif choice == "4":

        book_id = int(input("Enter Book ID to delete: "))

        sql = "DELETE FROM books WHERE book_id = %s"

        cursor.execute(sql, (book_id,))
        db.commit()

        print("Book deleted successfully!")

    # EXIT
    elif choice == "5":

        print("Thank you for using Library Management System!")
        break

    else:

        print("Invalid choice. Please try again.")

cursor.close()
db.close()
