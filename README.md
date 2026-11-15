

# FleetEase – Vehicle Rental Management System

## 1. Project Overview

FleetEase is a web-based vehicle rental management system developed using Python and Flask. It allows customers to explore available cars and bikes, submit rental bookings, and view calculated rental prices.

The application also provides an admin dashboard for managing booking statuses and viewing booking reports.

## 2. Project Objectives

- Develop a simple vehicle rental platform.
- Display cars and bikes with rental prices.
- Allow customers to submit vehicle booking requests.
- Calculate rental duration and total rental cost.
- Store booking information using SQLite.
- Provide an admin dashboard for booking management.
- Display booking and revenue reports.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web application framework |
| HTML | Webpage structure |
| CSS | Website styling |
| JavaScript | Client-side interaction |
| SQLite | Database management |
| Git | Version control |
| GitHub | Source code hosting |
| VS Code | Development environment |

## 4. Main Features

1. **Vehicle Listings:** Displays cars and bikes with their details and rental prices.
2. **Vehicle Booking:** Collects customer details and rental dates.
3. **Price Calculation:** Calculates rental days and total rental cost.
4. **Database Storage:** Saves booking records in SQLite.
5. **Admin Dashboard:** Displays bookings and allows administrators to update booking statuses.
6. **Booking Reports:** Displays total bookings, revenue, and booking status summaries.

## 5. Project Folder Structure

```text
FLEETEASE/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── database/
│   ├── db.py
│   ├── view_bookings.py
│   └── fleetease.db
│
├── templates/
│   ├── index.html
│   ├── admin.html
│   └── reports.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
│
├── screenshots/
│
└── documentation/
```

## 6. Installation and Execution

### Step 1: Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Open the project folder

```bash
cd FLEETEASE
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the application

```bash
python app.py
```

### Step 5: Open the application

Homepage:

```text
http://127.0.0.1:5000/
```

Admin Dashboard:

```text
http://127.0.0.1:5000/admin/bookings
```

Booking Reports:

```text
http://127.0.0.1:5000/admin/reports
```

## 7. Database

FleetEase uses SQLite to store vehicle booking information, including:

- Booking ID
- Customer name
- Phone number
- Vehicle name
- Pickup date
- Return date
- Rental duration
- Total rental price
- Booking status

## 8. Future Enhancements

- Customer registration and login.
- Vehicle availability management.
- Customer booking history.
- Secure administrator authentication.
- Online payment integration.
- Improved reporting and analytics.

## 9. Conclusion

FleetEase demonstrates the development of a vehicle rental management application using Python, Flask, SQLite, HTML, CSS, and JavaScript. It combines customer booking functionality with administrative booking management and reporting.

## 10. Author

Developed as part of the Week 6 Internship Final Python Project.

# FleetEase - Vehicle Rental Platform

## Project Description
FleetEase is a vehicle rental web application
developed using Python Flask, HTML, CSS and JavaScript.

It allows users to explore cars and bikes available
for rental.

## Technologies Used
- Python
- Flask
- HTML5S
- CSS3
- JavaScript
- SQLite (planned database integration)

## Features
- Vehicle listing
- Cars and bikes categories
- Vehicle price information
- Responsive homepage
- Booking interface

## Project Structure
- app.py - Flask application
- templates/ - HTML templates
- static/css/ - CSS styling
- static/js/ - JavaScript
- database/ - Database files
- screenshots/ - Project screenshots
- documentation/ - Project documentation

## Installation

1. Clone the repository.
2. Open the project in VS Code.
3. Install dependencies:

   pip install -r requirements.txt

4. Run the application:

   python app.py

5. Open your browser:

   http://127.0.0.1:5000/

## Developer
Vinay

B.Tech - Artificial Intelligence and Data Science

## Project Name
FleetEase - Vehicle Rental Platform
