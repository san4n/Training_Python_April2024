#Define a class called ToyCar

class ToyCar:
    def __init__(self,color,size,wheels):
        self.color=color
        self.size=size
        self.wheels=wheels


#Method to describe the toy car
    def describe(self):
        print(f"Color:{self.color}")
        print(f"Size:{self.size}")
        print(f"Wheels:{self.wheels}")

#Create two objects

car1=ToyCar("red","small",4)
car2=ToyCar("blue","large",6)

#Print the details of objects(each car)

car1.describe()
car2.describe()
