class Booking:
    def __init__(self, customer_id, parking_garage_id, start_time, end_time, status, id=None):
        self.customer_id = customer_id
        self.parking_garage_id = parking_garage_id
        self.start_time = start_time
        self.end_time = end_time
        self.status = status
        self.id = id

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        self._customer_id = customer_id

    @property
    def parking_garage_id(self):
        return self._parking_garage_id

    @parking_garage_id.setter
    def parking_garage_id(self, parking_garage_id):
        self._parking_garage_id = parking_garage_id

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        self._start_time = start_time

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        self._end_time = end_time

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    def __str__(self):
        return f'Customer ID: {self.customer_id}\nParking Garage ID: {self.parking_garage_id}\nStart Time: {self.start_time}\nEnd Time: {self.end_time}\nStatus: {self.status}'
