class Address:
    def __init__(self, address1, city, state, postal_code):
        self.address1 = address1
        self.city = city
        self.state = state
        self.postal_code = postal_code

    @property
    def address1(self):
        return self._address1

    @address1.setter
    def address1(self, address1):
        self._address1 = address1

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        self._city = city

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state

    @property
    def postal_code(self):
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        self._postal_code = postal_code

    def __str__(self):
        return f'{self.address1}, {self.city}, {self.state} {self.postal_code}'