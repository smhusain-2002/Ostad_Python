# Single Inheritance, Mutiple and Multilevel

class GrandFather:
    def __init__(self, color, l_name):
        self.color = color
        self.lastName = l_name

    def gf_method(self):
        print("1st Generation.")

class Father (GrandFather):
    def __init__(self, color, l_name, hobby):
        super().__init__(color, l_name)
        self.hobby = hobby

    def f_method(self):
            print("2nd Generation.")


gf = GrandFather("Brown", "Khan")
f1 = Father("Brown", "Khan", "Football")
print (f1.color)


#   Mutiple Inheritance

class Kids (Father, GrandFather):
    def __init__(self, color, l_name, hobby, study):
        super().__init__(color, l_name, hobby)
        self.study = study


k1 = Kids( "Fare", "Mridha", "Tennis", "CSE" )
k1.gf_method()
k1.f_method()

print (k1.study)
print (k1.color)


print ( k1.color, k1.study, k1.hobby, k1.lastName )


# Hierarchical Inheritance

class Vehicle:

     def engine_type(self):
          print ( "Vehicle has an engine." )

class Car (Vehicle):
     def num_doors(self):
          print ( "Car has 4 doors." )

class Truck(Vehicle):
     def load_capacity(self):
          print ( "Truck can carry 10 tons." )

car = Car()
car.num_doors()
car.engine_type()

# Hybrid Inheritance


# Not Done.... .... .... .... .... ....  :(