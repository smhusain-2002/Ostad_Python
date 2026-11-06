# Association:          Using one class obj in another class 

class Laptop:
    def __init__(self, brand):
        self.brand = brand

class Studnet:

    def __init__(self, name, laptop_obj):
        self.name = name
        self.laptop_v = laptop_obj

    def show_laptop(self):
        print ( f"{self.name} has a laptop named {self.laptop_v.brand}" )


lap = Laptop("Asus")
stud1 = Studnet("Rahim", lap)
stud1.show_laptop()


# Aggregation:          have a relationship

class Department:
    def __init__(self, name):
        self.name = name

class University:
    def __init__(self, name):
        self.name = name
        self.depart = []

    def add_dept(self, dept):
        self.depart.append(dept)

    def show_dept(self):
        return [department.name for department in self.depart]

uni1 = University("IIUC")

dept1 = Department("CSE")
dept2 = Department("BBA")
dept3 = Department("MBA")
dept4 = Department("Math")

uni1.add_dept(dept1)
uni1.add_dept(dept2)
uni1.add_dept(dept3)
uni1.add_dept(dept4)

print (uni1.show_dept())


# Composition               Have a relation where one obj cannot exist without other obj
# Example: Relationship between Car and Engine. Without Engine a car cannot be made

class Engine:
    def __init__(self, power):
        self.power = power


class Car:
    def __init__(self, brand, power):
        self.brand = brand
        self.engine = Engine(power)

    def show_details (self):
        print (f"{self.brand} has an engine with {self.engine.power} HP")


car = Car ("Toyota", 100)
car.show_details()