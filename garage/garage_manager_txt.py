from address import Address
from garage.garage_manager import GarageManager
import importlib.resources
import shutil
import tempfile
from garage.parking_garage import ParkingGarage


class GarageManagerTXT(GarageManager):
    def __init__(self):
        super().__init__()
        self._load_garages()

    def _save_garages_to_file(self):
        with importlib.resources.path("data", "garages.txt") as resource_path:
            with tempfile.NamedTemporaryFile(mode='a', delete=False) as temp_file:
                for g in self.parking_garages:
                    temp_file.write(f'{g.name},{g.max_capacity},{g.remaining_capacity},{g.address.address1},{g.address.city},{g.address.state},{g.address.postal_code},{g.id}\n')
        shutil.move(temp_file.name, resource_path)

    def _load_garages(self):
        with importlib.resources.open_text("data", "garages.txt") as file:
            for line in file:
                print(line)
                name, max, remaining, address1, city, state, postal_code, id = line.strip().split(',')
                a = Address(address1, city, state, postal_code)
                g = ParkingGarage(name, int(max), int(remaining), a, id)
                self.parking_garages.append(g)