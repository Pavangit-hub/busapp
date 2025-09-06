# bus_app.py
# Simple Bus Booking Application

class Bus:
    def __init__(self, bus_id, route, seats=40):
        self.bus_id = bus_id
        self.route = route
        self.seats = seats
        self.booked = []

    def available_seats(self):
        return self.seats - len(self.booked)

    def book_seat(self, passenger_name):
        if self.available_seats() > 0:
            self.booked.append(passenger_name)
            print(f"✅ Seat booked for {passenger_name} on Bus {self.bus_id}.")
        else:
            print("❌ No seats available!")

    def display_info(self):
        print(f"\n🚌 Bus {self.bus_id}")
        print(f"Route: {self.route}")
        print(f"Total Seats: {self.seats}")
        print(f"Booked: {len(self.booked)}")
        print(f"Available: {self.available_seats()}")


# Sample Data
buses = [
    Bus(bus_id=1, route="City A → City B"),
    Bus(bus_id=2, route="City B → City C"),
    Bus(bus_id=3, route="City A → City C")
]

def main():
    while True:
        print("\n=== Bus Booking System ===")
        print("1. Show Buses")
        print("2. Book Seat")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            for bus in buses:
                bus.display_info()
        elif choice == "2":
            bus_id = int(input("Enter Bus ID: "))
            name = input("Enter Passenger Name: ")
            for bus in buses:
                if bus.bus_id == bus_id:
                    bus.book_seat(name)
                    break
            else:
                print("❌ Invalid Bus ID.")
        elif choice == "3":
            print("👋 Thank you for using the Bus Booking System!")
            break
        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    main()
