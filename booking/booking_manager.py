from abc import ABC, abstractmethod

class BookingManager(ABC):
    def __init__(self):
        self.bookings = []

    def get_bookings(self):
        return self.bookings

    def book(self, booking):
        i = len(self.bookings) + 1
        booking.id = f'BK{i}'
        self.bookings.append(booking)
        self._save_bookings_to_file()

    def update_booking_status(self, booking_id, status):
        for b in self.bookings:
            if b.id == booking_id:
                b.status = status
                break
        self._save_bookings_to_file()

    def is_valid_booking(self, booking_id):
        for b in self.bookings:
            if b.id == booking_id:
                return True
        return False

    def get_bookings_by_customer(self, customer_id):
        return [b for b in self.bookings if b.customer_id == customer_id]

    def get_booking_by_id(self, booking_id):
        for b in self.bookings:
            if b.id == booking_id:
                return b
        return None

    @abstractmethod
    def _save_bookings_to_file(self):
        pass

    @abstractmethod
    def _load_bookings(self):
        pass
