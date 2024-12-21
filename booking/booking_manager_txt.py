import importlib.resources
import shutil
import tempfile

from booking.booking import Booking
from booking.booking_manager import BookingManager


class BookingManagerTXT(BookingManager):
    def __init__(self):
        super().__init__()
        self._load_bookings()

    def _save_bookings_to_file(self):
        with importlib.resources.path("data", "bookings.txt") as resource_path:
            with tempfile.NamedTemporaryFile(mode='a', delete=False) as temp_file:
                for b in self.bookings:
                    temp_file.write(f'{b.customer_id},{b.parking_garage_id},{b.start_time},{b.end_time},{b.status},{b.id}\n')
        shutil.move(temp_file.name, resource_path)

    def _load_bookings(self):
        with importlib.resources.open_text("data", "bookings.txt") as file:
            for line in file:
                customer_id, garage_id, start_time, end_time, status, id = line.strip().split(',')
                b = Booking(customer_id, garage_id, start_time, end_time, status, id)
                self.bookings.append(b)