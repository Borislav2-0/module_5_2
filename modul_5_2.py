class House:
    def __init__(self, number_of_floors):
        self.number_of_floors = number_of_floors
        print(number_of_floors)

    def set_sew_number_of_floors(self, floors):
        self.floors = floors
        self.number_of_floors += floors
        print(self.number_of_floors)


house = House(0)
house.set_sew_number_of_floors(10)
