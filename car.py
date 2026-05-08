# Write your class definition here!

class Car:
    def _init_(self, car_id, brand, year, color, mileage=0.0):
        """Inicializa los atributos del auto."""
        self.car_id = car_id
        self.brand = brand
        self.year = year
        self.color = color
        self.mileage = float(mileage)

    def change_color(self, new_color):
        self.color = new_color

    def drive(self, miles):
        self.mileage += miles

    def _str_(self):
        return f"{self.car_id} - {self.year} {self.color} {self.brand} with {self.mileage} miles"