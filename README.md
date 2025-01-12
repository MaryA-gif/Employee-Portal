# Employee-Portal
Employee Login and Details Storage using Python, Tkinter with SQL

# Employee Portal

A Python-based GUI application that allows employees to log in, enter their details, and save them into an SQL database. The portal also provides functionality to display the saved employee information.

## Features
- **Login System**: Users can log in securely using a GUI login page.
- **Data Entry**: Users can input their details (e.g., Name, ID, Department).
- **Data Display**: Displays the entered employee details on the same GUI window.(using tree view concept)
- **Database Integration**: Stores all employee details in an SQL database for persistent storage.

## Technologies Used
- **Programming Language**: Python
- **GUI Library**: Tkinter
- **Database**: SQL (XAMPP)

## Installation and Setup
Follow these steps to run the project locally:

### Prerequisites
- Python 3.x installed on your system
- An SQL database (e.g., SQLite or MySQL, i used XAMPP) set up on your system
- Required Python libraries installed (Tkinter, SQLite/MySQL connector)

### Usage
-**Login**:
Enter your name & password to access the portal.

-**Main page**:
-**Add Employee Details**:
After logging in, fill out the form with employee details such as Name, ID, and Department.
Click "Add employee" to store the data in the database and there some options to modify the database by using "Update Employee","Delete Employee","Delete All","New Employee" buttons to perform functions.

-**Display Data**:
View the entered details dynamically displayed on the GUI after saving.
