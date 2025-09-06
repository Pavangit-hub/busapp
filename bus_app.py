# bus_app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple in-memory bus data
buses = {
    1: {"route": "City A → City B", "seats": 40, "booked": []},
    2: {"route": "City B → City C", "seats": 40, "booked": []},
    3: {"route": "City A → City C", "seats": 40, "booked": []},
}

@app.route("/")
def home():
    return "🚌 Welcome to Bus Booking API!"

@app.route("/buses", methods=["GET"])
def list_buses():
    return jsonify(buses)

@app.route("/book/<int:bus_id>", methods=["POST"])
def book_seat(bus_id):
    passenger = request.json.get("name")
    bus = buses.get(bus_id)
    if not bus:
        return jsonify({"error": "Invalid Bus ID"}), 404

    if len(bus["booked"]) < bus["seats"]:
        bus["booked"].append(passenger)
        return jsonify({"message": f"Seat booked for {passenger} on Bus {bus_id}"})
    else:
        return jsonify({"error": "No seats available"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
