# Poly -> Multiple
# morphism -> Form

#  1. Method Overriding

class GrandFather:
    def grret(self):
        print ( "GrandFather says: " )


class Father (GrandFather):
    def grret(self):
        print ( "Father says: " )


class Kids (Father):
    def grret(self):
        print ( "Kids says: " )

gf = GrandFather()
f = Father()
kid = Kids()

gf.grret()
f.grret()
kid.grret()
 






#  2. Method Overloading

