##num = eval(input("Enter a number: "))
##
##if (num%5==0):
##    print("Divisable by 5")
##else:
##    print("Not divisable by 5")
##    

from random import randint

x = randint(1,10) #range of number
y = randint(3,7)
print(x,y)

# Math module

from math import sin,pi,sqrt,factorial

##print('Pi is roughly',pi)
##print("sin(60)=",sin(60))

y = eval(input("Enter a number: "))
y_f=factorial(y)
print(f"Factorial of {y} is {y_f}")
y_sr=sqrt(y)
print(f"Square root of {y} is {y_sr}")


