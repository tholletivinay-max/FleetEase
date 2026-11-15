import os
import sys

# Add the main FleetEase project folder to Python's import path
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_DIR)

from database.db import get_connection, DB_PATH

print("\n========== FLEETEASE DATABASE CHECK ==========")
print("Database file:", DB_PATH)
print("Database exists:", os.path.exists(DB_PATH))

connection = get_connection()
cursor = connection.cursor()

cursor.execute("SELECT COUNT(*) FROM bookings")
count = cursor.fetchone()[0]

print("\nFLEETEASE BOOKING RECORDS")
print("-------------------------")
print("Total bookings:", count)

cursor.execute("""
    SELECT id, vehicle_name, customer_name, phone, booking_date, status
    FROM bookings
    ORDER BY id DESC
""")

records = cursor.fetchall()

if records:
    for record in records:
        print("\nBooking ID:", record[0])
        print("Vehicle:", record[1])
        print("Customer:", record[2])
        print("Phone:", record[3])
        print("Booking Date:", record[4])
        print("Status:", record[5])
else:
    print("No booking records found.")

connection.close()
print("\n==============================================")