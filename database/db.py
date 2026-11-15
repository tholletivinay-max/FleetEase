
import sqlite3
import os

# Database location
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "database", "fleetease.db")


def get_connection():
    return sqlite3.connect(DB_PATH)


def initialize_database():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vehicle_name TEXT NOT NULL,
            customer_name TEXT NOT NULL,
            phone TEXT NOT NULL,
            booking_date TEXT NOT NULL,
            status TEXT DEFAULT 'Pending'
        )
    """)

    connection.commit()
    connection.close()


def save_booking(vehicle_name, customer_name, phone, booking_date):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO bookings
        (vehicle_name, customer_name, phone, booking_date)
        VALUES (?, ?, ?, ?)
    """, (vehicle_name, customer_name, phone, booking_date))

    connection.commit()
    connection.close()
