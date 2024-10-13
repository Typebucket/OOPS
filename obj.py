class Vehicle:
    def __init__ (self,Maxspeed,Mileage):
       self.Maxspeed = Maxspeed
       self.Mileage = Mileage

Lamborghini = Vehicle(1000, 100)
print("The maximum speed of the lamborghini is: " ,Lamborghini.Maxspeed)
print("The Mileage of the Lamborghini is: " ,Lamborghini.Mileage)