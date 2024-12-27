import os
import django

# Add the project directory to the Python path
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from payment.models import Seat
from flights.models import Flight

# Danh sách ghế cố định
SEAT_DATA = [
    ('F1', 100.00, 'first', 'AVAILABLE'),
    ('F2', 100.00, 'first', 'AVAILABLE'),
    ('F3', 100.00, 'first', 'AVAILABLE'),
    ('F4', 100.00, 'first', 'AVAILABLE'),
    ('F5', 100.00, 'first', 'AVAILABLE'),
    ('F6', 100.00, 'first', 'AVAILABLE'),
    ('F7', 100.00, 'first', 'AVAILABLE'),
    ('F8', 100.00, 'first', 'AVAILABLE'),
    ('F9', 100.00, 'first', 'AVAILABLE'),
    ('F10', 100.00, 'first', 'AVAILABLE'),
    ('F11', 100.00, 'first', 'AVAILABLE'),
    ('F12', 100.00, 'first', 'AVAILABLE'),
    ('F13', 100.00, 'first', 'AVAILABLE'),
    ('F14', 100.00, 'first', 'AVAILABLE'),
    ('F15', 100.00, 'first', 'AVAILABLE'),
    ('B1', 80.00, 'business', 'AVAILABLE'),
    ('B2', 80.00, 'business', 'AVAILABLE'),
    ('B3', 80.00, 'business', 'AVAILABLE'),
    ('B4', 80.00, 'business', 'AVAILABLE'),
    ('B5', 80.00, 'business', 'AVAILABLE'),
    ('B6', 80.00, 'business', 'AVAILABLE'),
    ('B7', 80.00, 'business', 'AVAILABLE'),
    ('B8', 80.00, 'business', 'AVAILABLE'),
    ('B9', 80.00, 'business', 'AVAILABLE'),
    ('B10', 80.00, 'business', 'AVAILABLE'),
    ('B11', 80.00, 'business', 'AVAILABLE'),
    ('B12', 80.00, 'business', 'AVAILABLE'),
    ('B13', 80.00, 'business', 'AVAILABLE'),
    ('B14', 80.00, 'business', 'AVAILABLE'),
    ('B15', 80.00, 'business', 'AVAILABLE'),
    ('E1', 50.00, 'economy', 'AVAILABLE'),
    ('E2', 50.00, 'economy', 'AVAILABLE'),
    ('E3', 50.00, 'economy', 'AVAILABLE'),
    ('E4', 50.00, 'economy', 'AVAILABLE'),
    ('E5', 50.00, 'economy', 'AVAILABLE'),
    ('E6', 50.00, 'economy', 'AVAILABLE'),
    ('E7', 50.00, 'economy', 'AVAILABLE'),
    ('E8', 50.00, 'economy', 'AVAILABLE'),
    ('E9', 50.00, 'economy', 'AVAILABLE'),
    ('E10', 50.00, 'economy', 'AVAILABLE'),
    ('E11', 50.00, 'economy', 'AVAILABLE'),
    ('E12', 50.00, 'economy', 'AVAILABLE'),
    ('E13', 50.00, 'economy', 'AVAILABLE'),
    ('E14', 50.00, 'economy', 'AVAILABLE'),
    ('E15', 50.00, 'economy', 'AVAILABLE')
]

def load_seats():
    """
    Load fixed seat data for all flights in the database.
    """
    try:
        flights = Flight.objects.all()  # Lấy tất cả các chuyến bay
        seat_objects = []

        for flight in flights:
            for seat_name, price, seat_type, status in SEAT_DATA:
                seat_objects.append(Seat(
                    seat_name=seat_name,
                    price=price,
                    type=seat_type,
                    status=status,
                    flight=flight
                ))

        # Chèn dữ liệu vào bảng Seat
        Seat.objects.bulk_create(seat_objects)
        print(f"Successfully added {len(seat_objects)} seats for all flights.")

    except Exception as e:
        print(f"Error loading seats: {e}")

if __name__ == "__main__":
    load_seats()
