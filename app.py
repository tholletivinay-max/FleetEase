

from flask import Flask, render_template, jsonify, request, redirect, url_for

from datetime import date
def get_booking_summary():
    # Your logic here to fetch the data
    return ...

from database.db import (
    initialize_database,
    save_booking,
    get_all_bookings,
    update_booking_status,
    get_booking_summary
)

app = Flask(__name__)

vehicles = [
    {"id": 1, "name": "Hyundai i20", "category": "Car",
     "price": 1500, "fuel": "Petrol", "seats": 5,
     "image": "https://images.unsplash.com/photo-1606611013016-969c19ba27bb?w=800"},

    {"id": 2, "name": "Honda City", "category": "Car",
     "price": 2200, "fuel": "Petrol", "seats": 5,
     "image": "https://images.unsplash.com/photo-1552519507-da3b142c6e3d?w=800"},

    {"id": 3, "name": "Royal Enfield Classic 350", "category": "Bike",
     "price": 800, "fuel": "Petrol", "seats": 2,
     "image": "https://images.unsplash.com/photo-1558981806-ec527fa84c39?w=800"},

    {"id": 4, "name": "Yamaha MT-15", "category": "Bike",
     "price": 600, "fuel": "Petrol", "seats": 2,
     "image": "https://images.unsplash.com/photo-1558981403-c5f9899a28bc?w=800"}
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
    return_date = data.get("return_date", "").strip()

    if not all([vehicle_name, customer_name, phone,
                booking_date, return_date]):
        return jsonify({"message": "Please fill in all fields."}), 400

    vehicle = next(
        (v for v in vehicles if v["name"] == vehicle_name), None
    )

    if vehicle is None:
        return jsonify({"message": "Invalid vehicle selected."}), 400

    if not phone.isdigit() or len(phone) != 10:
        return jsonify({"message": "Enter a valid 10-digit phone number."}), 400

    try:
        pickup = date.fromisoformat(booking_date)
        returning = date.fromisoformat(return_date)

        if pickup < date.today():
            return jsonify({"message": "Pickup date cannot be in the past."}), 400

        if returning < pickup:
            return jsonify({"message": "Return date must be on or after pickup date."}), 400

        total_days = (returning - pickup).days + 1
        total_price = total_days * vehicle["price"]

        save_booking(
            vehicle_name,
            customer_name,
            phone,
            booking_date,
            return_date,
            total_days,
            total_price
        )

        return jsonify({
            "message": "Booking submitted successfully!",
            "total_days": total_days,
            "total_price": total_price
        }), 201

    except ValueError:
        return jsonify({"message": "Please enter valid dates."}), 400

@app.route("/admin/bookings")
def admin_bookings():
    bookings = get_all_bookings()
    return render_template("admin.html", bookings=bookings)

@app.route("/admin/reports")
def admin_reports():
    summary = get_booking_summary()
    return render_template("reports.html", summary=summary)

@app.route("/admin/update-status/<int:booking_id>", methods=["POST"])
def change_booking_status(booking_id):

    new_status = request.form.get("status")

    updated = update_booking_status(booking_id, new_status)

    if not updated:
        return "Invalid booking or status.", 400

    return redirect(url_for("admin_bookings"))


if __name__ == "__main__":
    initialize_database()
    app.run(debug=True)
