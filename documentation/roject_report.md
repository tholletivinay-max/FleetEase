# FLEETEASE
## Vehicle Rental Management System

**Internship Assignment:** Week 6 – Final Project  
**Project Title:** FleetEase – Vehicle Rental Management System  
**Student Name:** Tholleti Vinay  
**Course:** B.Tech – Artificial Intelligence and Data Science  
**Institution:** Dhanalakshmi Srinivasan University  
**Project Type:** Python Full-Stack Web Application  

---

# 1. Abstract

FleetEase is a web-based vehicle rental management system developed using Python, Flask, HTML, CSS, JavaScript and SQLite.

The application allows customers to explore available cars and bikes, submit vehicle rental bookings, calculate rental prices and view their booking history.

It also provides an administrative dashboard for managing bookings, updating booking statuses and viewing booking reports.

The project demonstrates Python programming concepts, object-oriented programming, database connectivity, file handling and exception handling.

# 2. Introduction

Vehicle rental services provide customers with convenient access to vehicles without requiring ownership.

However, managing vehicle bookings manually can create problems such as overlapping reservations, incorrect price calculations and difficulty maintaining booking records.

FleetEase aims to simplify these operations through a web-based application.

The system provides a simple interface for customers and management features for administrators.

# 3. Problem Statement

Traditional vehicle rental management may involve manual booking records, time-consuming calculations and difficulties tracking vehicle availability.

The main problems addressed by FleetEase are:

- Manual management of vehicle bookings.
- Difficulty tracking customer booking information.
- Incorrect rental price calculations.
- Overlapping vehicle reservations.
- Difficulty managing booking statuses.
- Lack of centralized booking reports.

# 4. Project Objectives

1. Develop a user-friendly vehicle rental website.
2. Display cars and bikes with their rental prices.
3. Allow customers to submit booking requests.
4. Calculate rental duration and total rental cost automatically.
5. Store booking information in an SQLite database.
6. Prevent overlapping bookings for the same vehicle.
7. Provide customer booking history.
8. Provide an administrative dashboard.
9. Generate booking and revenue summaries.
10. Demonstrate Python programming and OOP concepts.

# 5. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web framework |
| HTML | Webpage structure |
| CSS | Website styling |
| JavaScript | Client-side interactions |
| SQLite | Database storage |
| Git | Version control |
| GitHub | Repository hosting |
| VS Code | Development environment |

# 6. Main Features

## 6.1 Vehicle Listings

Displays available vehicle categories, including cars and bikes, with their names, images and rental prices.

## 6.2 Vehicle Booking

Customers enter their name, mobile number, pickup date and return date to submit a booking request.

## 6.3 Automatic Price Calculation

The application calculates the rental duration and total price.

Formula:

Total Days = (Return Date - Pickup Date) + 1

Total Price = Total Days × Daily Rental Price

## 6.4 Vehicle Availability Management

The system checks existing bookings and prevents overlapping reservations for the same vehicle.

Pending and approved bookings are considered reserved. Rejected bookings do not block availability.

## 6.5 Customer Booking History

Customers can search for their previous bookings using the phone number entered during booking.

## 6.6 Admin Dashboard

Administrators can view customer booking details and update booking statuses to Pending, Approved or Rejected.

## 6.7 Booking Reports

The reports page displays:

- Total bookings.
- Total recorded booking revenue.
- Pending bookings.
- Approved bookings.
- Rejected bookings.

## 6.8 Booking Activity Log

The application records booking activities in a text file using Python file handling.

# 7. Python Concepts Used

| Concept | Implementation |
|---|---|
| Variables and data types | Customer details, prices and dates |
| Input and output | Booking information and responses |
| Conditional statements | Booking validation and availability |
| Loops | Vehicle listings and booking records |
| Functions | Booking, database and reporting operations |
| Lists | Vehicle collections |
| Dictionaries | Vehicle information |
| Classes and objects | Vehicle, Car and Bike classes |
| Inheritance | Car and Bike inherit from Vehicle |
| Encapsulation | Private rental price attribute |
| Polymorphism | Overridden get_category() method |
| File handling | Booking activity log |
| Exception handling | Handling invalid input and file errors |
| Python libraries | datetime, os and sqlite3 |

# 8. System Architecture

FleetEase follows a simple three-layer application structure.

**Presentation Layer**
- HTML
- CSS
- JavaScript

**Application Layer**
- Python
- Flask
- Vehicle classes
- Booking validation
- Price calculation
- Availability checking

**Data Layer**
- SQLite database
- Booking records
- Booking activity log

The frontend communicates with the Flask backend, which processes requests and interacts with the database.

# 9. Project Folder Structure

```text
FLEETEASE/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── models/
│   └── vehicle.py
│
├── database/
│   ├── db.py
│   ├── view_bookings.py
│   └── fleetease.db
│
├── templates/
│   ├── index.html
│   ├── admin.html
│   ├── reports.html
│   └── my_bookings.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
│
├── utils/
│   └── booking_logger.py
│
├── logs/
│   └── booking_activity.txt
│
├── screenshots/
│
└── documentation/
    └── project_report.md
```

# 10. Database Design

FleetEase uses SQLite to store vehicle booking information.

The bookings table contains:

| Field | Description |
|---|---|
| id | Unique booking ID |
| vehicle_name | Selected vehicle |
| customer_name | Customer name |
| phone | Customer mobile number |
| booking_date | Pickup date |
| return_date | Return date |
| total_days | Rental duration |
| total_price | Calculated rental price |
| status | Booking status |

# 11. Application Workflow

1. Customer opens the FleetEase homepage.
2. Customer explores available vehicles.
3. Customer selects a vehicle.
4. Customer enters personal and rental details.
5. System validates the submitted information.
6. System checks vehicle availability.
7. System calculates rental duration and price.
8. Booking information is saved in SQLite.
9. Booking activity is recorded in a text file.
10. Administrator views and manages bookings.
11. Reports display booking statistics and revenue.

# 12. Testing and Validation

The following test cases are used to evaluate the application.

| Test Case | Expected Result |
|---|---|
| Open homepage | Homepage displays successfully |
| View vehicles | Cars and bikes are displayed |
| Submit valid booking | Booking is saved |
| Enter invalid phone number | Validation error displayed |
| Select past pickup date | Booking rejected |
| Select return date before pickup | Booking rejected |
| Submit overlapping booking | Booking rejected |
| Book another available vehicle | Booking accepted |
| Search booking history | Matching records displayed |
| Update booking status | Status updated |
| View booking reports | Summary displayed |
| Create booking activity | Log file updated |

**Note:** Attach actual application screenshots as evidence of the tests performed. Do not mark a test as successful unless it has been verified.

# 13. Output Screenshots

Insert the actual screenshots captured during project execution.

Recommended screenshots:

1. FleetEase homepage.
2. Vehicle listings showing cars and bikes.
3. Successful booking confirmation.
4. Invalid booking validation message.
5. Overlapping booking rejection.
6. Customer booking history.
7. Admin booking dashboard.
8. Booking status update.
9. Booking reports.
10. Booking activity log.

# 14. Challenges Faced

During development, several technical challenges were addressed:

1. Configuring Python, Flask and VS Code.
2. Connecting the frontend with Flask routes.
3. Creating and managing the SQLite database.
4. Validating customer booking information.
5. Calculating rental duration and total prices.
6. Preventing overlapping vehicle reservations.
7. Implementing OOP concepts in the existing application.
8. Integrating customer history and administrative reports.
9. Managing source code using Git and GitHub.

# 15. Security and Limitations

The current project is an internship demonstration application.

The following improvements are necessary before production deployment:

- Add administrator authentication.
- Add secure customer registration and login.
- Protect customer booking history using OTP or authentication.
- Use secure configuration and deployment settings.
- Add stronger database transaction protection for simultaneous bookings.
- Integrate a secure online payment gateway.

# 16. Future Enhancements

- Customer registration and login.
- Administrator authentication.
- Advanced vehicle availability calendar.
- Online payment integration.
- Email and SMS booking notifications.
- Advanced search and filtering.
- Vehicle image uploads.
- Cloud database integration.
- Responsive mobile interface.

# 17. Conclusion

FleetEase demonstrates the development of a vehicle rental management system using Python and modern web technologies.

The application combines vehicle listings, customer bookings, automatic rental price calculation, availability validation, database storage, booking history, administrative management and reporting.

The project provides practical experience in Python programming, object-oriented programming, Flask web development, SQLite database operations, file handling, exception handling and GitHub version control.

It also provides a foundation for developing more advanced vehicle rental management applications in the future.

# 18. References

- Python Documentation: https://docs.python.org/3/
- Flask Documentation: https://flask.palletsprojects.com/
- SQLite Documentation: https://www.sqlite.org/docs.html
- HTML Documentation: https://developer.mozilla.org/en-US/docs/Web/HTML
- Git Documentation: https://git-scm.com/doc
- GitHub Documentation: https://docs.github.com/

---

**End of Project Report**

**Project:** FleetEase – Vehicle Rental Management System  
**Assignment:** Week 6 – Final Python Project