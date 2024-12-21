import importlib.resources
import shutil
import tempfile

from user.user_manager import UserManager
from address import Address
from user.customer import Customer

class UserManagerTXT(UserManager):
    def __init__(self):
        super().__init__()
        self._load_customers()

    def _save_customers_to_file(self):
        with importlib.resources.path("data", "customers.txt") as resource_path:
            with tempfile.NamedTemporaryFile(mode='a', delete=False) as temp_file:
                for c in self.customers:
                    temp_file.write(f'{c.firstname},{c.lastname},{c.email_address},{c.address.address1},{c.address.city},{c.address.state},{c.address.postal_code},{c.id}\n')
        shutil.move(temp_file.name, resource_path)

    def _load_customers(self):
        with importlib.resources.open_text("data", "customers.txt") as file:
            for line in file:
                firstname, lastname, email, address1, city, state, postal_code, id = line.strip().split(',')
                a = Address(address1, city, state, postal_code)
                c = Customer(firstname, lastname, email, a, id)
                self.customers.append(c)