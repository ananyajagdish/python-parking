from abc import ABC, abstractmethod

class GarageManager(ABC):
    def __init__(self):
        self.parking_garages = []

    def get_parking_garages(self):
        return self.parking_garages

    def get_parking_garage(self, garage_id):
        for g in self.parking_garages:
            if g.id == garage_id:
                return g
        return None

    def reserve_parking_garage(self, garage_id):
        for g in self.parking_garages:
            if g.id == garage_id and g.remaining_capacity > 0:
                g.remaining_capacity -= 1
                self._save_garages_to_file()
                return True
        return False

    def release_parking_garage(self, garage_id):
        for g in self.parking_garages:
            if g.id == garage_id:
                g.remaining_capacity += 1
                self._save_garages_to_file()
                return True
        return False

    def add_parking_garage(self, garage):
        self.parking_garages.append(garage)
        self._save_garages_to_file()

    def is_valid_parking_garage(self, garage_id):
        for g in self.parking_garages:
            if g.id == garage_id:
                return True
        return False

    def get_available_parking_garages(self):
        available_garages = []
        for g in self.parking_garages:
            if g.remaining_capacity > 0:
                available_garages.append(g)
        return available_garages

    @abstractmethod
    def _save_garages_to_file(self):
        pass

    @abstractmethod
    def _load_garages(self):
        pass