

from flask import Flask, render_template, jsonify, request
from database.db import initialize_database, save_booking

app = Flask(__name__)

# Sample vehicle information
vehicles = [
    {
        "id": 1,
        "name": "Hyundai i20",
        "category": "Car",
        "price": 1500,
        "fuel": "Petrol",
        "seats": 5,
        "image": "https://images.unsplash.com/photo-1606611013016-969c19ba27bb?w=800"
    },
    {
        "id": 2,
        "name": "Honda City",
        "category": "Car",
        "price": 2200,
        "fuel": "Petrol",
        "seats": 5,
        "image": "https://images.unsplash.com/photo-1552519507-da3b142c6e3d?w=800"
    },
    {
        "id": 3,
        "name": "Royal Enfield Classic 350",
        "category": "Bike",
        "price": 800,
        "fuel": "Petrol",
        "seats": 2,
        "image": "https://images.unsplash.com/photo-1558981806-ec527fa84c39?w=800"
    },
    {
        "id": 4,
        "name": "Yamaha MT-15",
        "category": "Bike",
        "price": 600,
        "fuel": "Petrol",
        "seats": 2,
        "image": "https://images.unsplash.com/photo-1558981403-c5f9899a28bc?w=800"
    }
]


@app.route("/")
def home():
    return render_template("index.html", vehicles=vehicles)


@app.route("/api/vehicles")
def get_vehicles():
    return jsonify(vehicles)


@app.route("/api/bookings", methods=["POST"])
def create_booking():

    data = request.get_json(silent=True) or {}

    vehicle_name = data.get("vehicle_name", "").strip()
    customer_name = data.get("customer_name", "").strip()
    phone = data.get("phone", "").strip()
    booking_date = data.get("booking_date", "").strip()

    if not all([vehicle_name, customer_name, phone, booking_date]):
        return jsonify({"message": "Please fill in all fields."}), 400

    if vehicle_name not in [v["name"] for v in vehicles]:
        return jsonify({"message": "Invalid vehicle selected."}), 400

    if not customer_name or not phone.isdigit() or len(phone) != 10:
        return jsonify({"message": "Enter a valid name and 10-digit phone number."}), 400

    try:
        from datetime import date
        selected_date = date.fromisoformat(booking_date)

        if selected_date < date.today():
            return jsonify({"message": "Booking date cannot be in the past."}), 400

        save_booking(vehicle_name, customer_name, phone, booking_date)

        return jsonify({
            "message": "Booking request submitted successfully!"
        }), 201

    except ValueError:
        return jsonify({"message": "Invalid booking date."}), 400


if __name__ == "__main__":
    initialize_database()
    app.run(debug=True)
