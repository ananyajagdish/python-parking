class ParkingGarage:
    def __init__(self, name, max_capacity, remaining_capacity, address, id=None):
        self.name = name
        self.max_capacity = max_capacity
        self.remaining_capacity = remaining_capacity
        self.address = address
        self.id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def max_capacity(self):
        return self._max_capacity

    @max_capacity.setter
    def max_capacity(self, max_capacity):
        self._max_capacity = max_capacity

    @property
    def remaining_capacity(self):
        return self._remaining_capacity

    @remaining_capacity.setter
    def remaining_capacity(self, remaining_capacity):
        self._remaining_capacity = remaining_capacity

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    def __str__(self):
        return f'Name: {self.name}\nMax Capacity: {self.max_capacity}\nRemaining Capacity: {self.remaining_capacity}\nAddress: {self.address}'
