
import os
from datetime import datetime

# Find the main project folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Location of the activity log
LOG_DIR = os.path.join(BASE_DIR, "logs")
LOG_FILE = os.path.join(LOG_DIR, "booking_activity.txt")


def log_booking(vehicle_name, booking_date, return_date,
                total_days, total_price):

    try:
        # Create logs folder if it does not exist
        os.makedirs(LOG_DIR, exist_ok=True)

        # Open file in append mode
        with open(LOG_FILE, "a", encoding="utf-8") as file:

            current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            file.write(
                f"Time: {current_time}\n"
                f"Vehicle: {vehicle_name}\n"
                f"Pickup Date: {booking_date}\n"
                f"Return Date: {return_date}\n"
                f"Rental Days: {total_days}\n"
                f"Total Price: Rs. {total_price}\n"
                f"{'-' * 40}\n"
            )

    except OSError as error:
        print("Unable to save booking log:", error)


def log_error(error):

    try:
        os.makedirs(LOG_DIR, exist_ok=True)

        with open(LOG_FILE, "a", encoding="utf-8") as file:

            current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            file.write(
                f"ERROR TIME: {current_time}\n"
                f"ERROR DETAILS: {error}\n"
                f"{'-' * 40}\n"
            )

    except OSError as file_error:
        print("Unable to save error log:", file_error)
