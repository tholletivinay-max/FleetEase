
from flask import Flask, render_template, jsonify

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


if __name__ == "__main__":
    app.run(debug=True)
