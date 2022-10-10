class Person:
    def __init__(self):
        self.name = ""
        self.noOfVehicle = ""
        self.vehicle1 = ""
        self.vehicle2 = ""

    def setPersonDetails(self, newName, noOfVehicle, vehicle1, vehicle2):
        self.name = newName
        self.noOfVehicle = noOfVehicle
        self.vehicle1 = vehicle1
        self.vehicle2 = vehicle2

    def getPersonDetails(self):
        print(self.name, "has", self.noOfVehicle, "vehicle one is",
              self.vehicle1, "and another is", self.vehicle2)


class vehicle:
    def __init__(self):
        self.fuel = ""
        self.uses = ""
        self.operation = ""


class hondaAccordCar(vehicle):
    def sethondaAccordCar(self, newfuel, uses, madein):
        self.fuel = newfuel
        self.uses = uses
        self.operation = madein

    def getHondaAccordCar(self):
        print("Honda accord car runs on fuel called", self.fuel)
        print("Honda accord is", self.uses, "and", self.operation, "in India")


class DucatiBike(vehicle):
    def setDucatiBike(self, newFuel, uses, imported):
        self.fuel = newFuel
        self.uses = uses
        self.operation = imported

    def getDucatiBike(self):
        print("Ducati runs on fuel called", self.fuel)
        print("Ducati is", self.uses, "and", self.operation, "vehicle")


if __name__ == "__main__":
    p = Person()
    p.setPersonDetails("Sourabh", "two", "honda accord car", "Ducati Bike")
    p.getPersonDetails()

    h = hondaAccordCar()
    h.sethondaAccordCar("diesel", "new", "made")
    h.getHondaAccordCar()

    d = DucatiBike()
    d.setDucatiBike("petrol", "used", "imported")
    d.getDucatiBike()