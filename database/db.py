
import sqlite3
import os

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

    # Add new columns to an existing database if needed
    cursor.execute("PRAGMA table_info(bookings)")
    existing_columns = [column[1] for column in cursor.fetchall()]

    new_columns = {
        "return_date": "TEXT",
        "total_days": "INTEGER",
        "total_price": "REAL"
    }

    for column_name, column_type in new_columns.items():
        if column_name not in existing_columns:
            cursor.execute(
                f"ALTER TABLE bookings ADD COLUMN {column_name} {column_type}"
            )

    connection.commit()
    connection.close()


def save_booking(vehicle_name, customer_name, phone,
                 booking_date, return_date, total_days, total_price):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO bookings
            (vehicle_name, customer_name, phone, booking_date,
             return_date, total_days, total_price)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            vehicle_name, customer_name, phone, booking_date,
            return_date, total_days, total_price
        ))

        connection.commit()
        print("BOOKING SAVED! ID:", cursor.lastrowid)

    finally:
        connection.close()


def get_all_bookings():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, customer_name, phone, vehicle_name,
               booking_date, return_date, total_days,
               total_price, status
        FROM bookings
        ORDER BY id DESC
    """)

    bookings = cursor.fetchall()
    connection.close()

    return bookings


def update_booking_status(booking_id, new_status):

    allowed_statuses = ["Pending", "Approved", "Rejected"]

    if new_status not in allowed_statuses:
        return False

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            UPDATE bookings
            SET status = ?
            WHERE id = ?
        """, (new_status, booking_id))

        connection.commit()

        return cursor.rowcount > 0

    finally:
        connection.close()

def get_booking_summary():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            COUNT(*),
            COALESCE(SUM(total_price), 0),
            SUM(CASE WHEN status = 'Pending' THEN 1 ELSE 0 END),
            SUM(CASE WHEN status = 'Approved' THEN 1 ELSE 0 END),
            SUM(CASE WHEN status = 'Rejected' THEN 1 ELSE 0 END)
        FROM bookings
    """)

    result = cursor.fetchone()
    connection.close()

    return {
        "total_bookings": result[0] or 0,
        "total_revenue": result[1] or 0,
        "pending": result[2] or 0,
        "approved": result[3] or 0,
        "rejected": result[4] or 0
    }
