
from db import get_connection

connection = get_connection()
cursor = connection.cursor()

cursor.execute("SELECT * FROM bookings")

records = cursor.fetchall()

print("FLEETEASE BOOKING RECORDS")

for record in records:
    print(record)

connection.close()
