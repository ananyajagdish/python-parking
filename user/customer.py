class Customer:

    def __init__(self, firstname, lastname, email_address, address, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.id = id
        self.email_address = email_address
        self.address = address

    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        self._firstname = firstname

    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        self._lastname = lastname

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def email_address(self):
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        self._email_address = email_address

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    def __str__(self):
        return f'Name: {self.firstname} {self.lastname}\nEmail: {self.email_address}\nAddress: {self.address}'