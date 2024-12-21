from abc import ABC, abstractmethod

class UserManager(ABC):
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        i = len(self.customers) + 1
        customer.id = f'CS{i}'
        self.customers.append(customer)
        self._save_customers_to_file()

    def get_customers(self):
        return self.customers

    def get_customer(self, email):
        for c in self.customers:
            if c.email_address == email:
                return c
        return None

    def is_valid_customer(self, customer_id):
        for c in self.customers:
            if c.id == customer_id:
                return True
        return False

    @abstractmethod
    def _save_customers_to_file(self):
        pass

    @abstractmethod
    def _load_customers(self):
        pass