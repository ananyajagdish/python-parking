from booking.booking import Booking
from booking.booking_manager_txt import BookingManagerTXT
from garage.garage_manager_txt import GarageManagerTXT
from user.customer import Customer
from user.user_manager_txt import UserManagerTXT


class ParkingManager:
    def __init__(self):
        self.um = UserManagerTXT()
        self.bm = BookingManagerTXT()
        self.gm = GarageManagerTXT()

    def register_customer(self, firstname, lastname, email, address):
        c = self.um.get_customer(email)
        if c is None:
            c = Customer(firstname, lastname, email, address)
            self.um.add_customer(c)
            return True
        return False

    def book(self, garage_id, customer_id, start_time, end_time):
        if (self.um.is_valid_customer(customer_id)) and start_time < end_time:
            b = self.gm.reserve_parking_garage(garage_id)
            if b:
                b = Booking(customer_id, garage_id, start_time, end_time, 'BOOKED')
                self.bm.book(b)
                return True
        return False

    def park(self, booking_id):
        b = self.bm.get_booking_by_id(booking_id)
        if b is not None and b.status == 'BOOKED':
            self.bm.update_booking_status(booking_id, 'PARKED')
            return True
        return False

    def exit(self, booking_id):
        b = self.bm.get_booking_by_id(booking_id)
        if b is not None and b.status == 'PARKED':
            self.bm.update_booking_status(booking_id, 'EXITED')
            self.gm.release_parking_garage(b.parking_garage_id)
            return True
        return False

    def get_bookings_by_customer(self, customer_id):
        return self.bm.get_bookings_by_customer(customer_id)

    def get_parking_garages(self):
        return self.gm.get_parking_garages()

    def get_all_customers(self):
        return self.um.get_customers()

