# Variables
# Global & Local Variables
x = 10 # Global Variable
def fu():
    y = 20  # Local Variable
    x = 15
    print(x)
    print(y)

fu()  # Call Function
print(x)
#print(y) # Not in scope

def fn():
    global x
    x = 25
    print(x)

print(x) # still 10
fn()
print(x)

z,y,a = 15,32,"A"
print(y)
print(a)

#num1,num2 = eval(input("Num1:"),input("Num2:"))
