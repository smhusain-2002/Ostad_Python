class Car:

    company_name = "AXA Motor SDN. BHD." # Class variable

    def __init__(self):
        self.brand = ""                 # Instance variable
        self.model = ""
        self.numberseat = 0
        self.numberdoor = 0
        self.color = ""
        self.manufyr = 0
        self._price = 0


    def __init__(self, brand, numberseat, numberdoor, color, manufyr, model):
        self.brand = "Toyota"
        self.color = "Silver"
        self.manufyr = "2013"
        self.numberdoor = 4
        self.numberseat = 7
        self.model = "Rush"
        self._price = 63000

    def __init__(self, brand="Honda", numberseat=2, numberdoor=2, color="Black", manufyr=2013, model="Civic"):
        self.brand = brand
        self.color = color
        self.manufyr = "2013"
        self.numberdoor = numberdoor
        self.numberseat = numberseat
        self.model = manufyr
        self.model= model
        self._price = 34000

    def display_info(self):
        print("Only Model Info", self.model, ".")
        print("Car Owner name: ", self.company_name, ".")

    def gget_price(self, password):
        if password == "Admin":
            print(self._price)
        else:
            print( "Invalid Access" )

    def sset_price(self, password, price):
        if password == "Admin":
            self._price = price
            print ("New Price Updated")
        else:
            print( "Invalid Access" )

    @classmethod
    def change_Company(cls, name):
        cls.company_name = name

    @staticmethod
    def year_diff(year):
        return 2026-int(year)

    @property
    def price(self):       # It is a readonly method
        return self._price

    @price.setter
    def price(self, new_price):
        self._price = new_price
    


car1 = Car(brand="Toyota", numberseat=2, numberdoor=2, color="Black", manufyr=2013, model="Rush")
print ( "Car Brand Name: ", car1.brand, "." )
car2 = Car()
print ( "Car Brand Name: ", car2.brand , ".")
car3 = Car()
print ( "Car Brand Name: ", car3.brand , ".")

car1.display_info()
car2.display_info()
car3.display_info()

# there are 2 ways we can change the Class Variable
print("=== == === == == === = = == = == = = == = = = = ")
Car.company_name = "XYZ Motors"

car1.display_info()
car2.display_info()
car3.display_info()

print("=== == === == == ++++++++++++++= = == = = == = = = = ")
Car.change_Company("ABC Motors")        # this is better way

car1.display_info()
car2.display_info()
car3.display_info()

print(car3.company_name)


yr = Car.year_diff(car1.manufyr)
print (yr)

print (car1.price)

# Example of Getter and Setter
print (car1._price)
car1.price = 10000
print (car1._price)

