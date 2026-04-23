class Example: # Class name is capital
    def __init__(self, a,b): #Autocall
        self.a =a #class variable
        self.b =b #class variable

    def add(self): #argument to every method
        return self.a+self.b


e = Example(8,6)
print(e.add()) # Output 14

d = Example(9,15)
print(d.add()) # Output 24
