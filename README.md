# Library Management System

The Library Management System is a comprehensive application designed to streamline and automate the management of library resources. Built using Python with a graphical user interface (GUI) developed in Tkinter, this system provides a user-friendly experience for librarians and staff to efficiently handle various library operations.

## Key Features

- `Member Management`: The system allows users to add, update, delete, and reset member information. This includes storing personal details such as name, contact information, and membership status.

- `Book Management`: Users can manage the library's book inventory by adding, updating, deleting, and resetting book details. This includes storing information such as title, author, genre, ISBN, and availability status.

- `Transaction Management`: The system handles the borrowing and returning of books. It automatically calculates due dates based on the borrowing date and the standard loan period, and it tracks late returns to calculate fines.

- `Records Display`: All records, including member information, book details, and transaction histories, are displayed in a tabular format for easy viewing and management. This feature ensures that users can quickly find and review the information they need.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/library-management-system.git
    cd library-management-system
    ```

2. **Install the required Python packages:**
    ```bash
    pip install tkinter mysql-connector-python
    ```

3. **Set up the MySQL database:**
    - Create a database named `python`.
    - Create a table named `library` with the following structure:
    ```sql
    CREATE TABLE library (
        MEMBER_TYPE VARCHAR(255),
        PRN_NO VARCHAR(255),
        ID_NUMBER VARCHAR(255),
        FIRST_NAME VARCHAR(255),
        LAST_NAME VARCHAR(255),
        ADDRESS1 VARCHAR(255),
        ADDRESS2 VARCHAR(255),
        POSTCODE VARCHAR(255),
        MOBILE_NUMBER VARCHAR(255),
        BOOK_ID VARCHAR(255),
        BOOK_TITLE VARCHAR(255),
        AUTHOR VARCHAR(255),
        DATE_BORROWED DATE,
        DUE_DATE DATE,
        DAYS_ON_BOOKS INT,
        LATE_RETURN_FINE VARCHAR(255),
        DATE_OVER_DUEDATE VARCHAR(255),
        ACTUAL_PRICE VARCHAR(255)
    );
    ```

## Usage

1. **Run the application:**
    ```bash
    python library_management_system.py
    ```

2. **Use the interface to manage library data:**
    - Add member information by filling in the fields and clicking "Add Data".
    - View existing records in the table below the form.
    - Update or delete records by selecting them from the table and clicking the appropriate button.
    - Reset the form fields by clicking "Reset".
    - Exit the application by clicking "Exit".

## Dependencies

- Python 3.x
- Tkinter
- MySQL Connector

## Screenshots

![Library Management System](https://github.com/shivanisgit/library_management_system/blob/main/images/project1.png)

## Contributing

Feel free to submit issues and enhancement requests.

