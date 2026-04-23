##from random import randint
##
##x = randint(1,10)
##
##for i in range(3):
##    print(x)

##import random
##
##y=random.randint(2,54)
##
##print(y)

##from random import randint

### Task 1: Generate 50 random integers between 3 and 6
##random_numbers = [random.randint(3, 6) for _ in range(50)]
##print("Random numbers between 3 and 6:", random_numbers)
##
### Task 2: Compute x * y
##x = random.randint(1, 50)
##y = random.randint(2, 5)
##result = x * y
##print(f"x = {x}, y = {y}, x*y = {result}")

##for i in range(50):
##    print(randint(3,6))

#from __future__ import print_function
####for i in range(1, 5):
####    for j in range(i):
####        print(i, end=' ')
####    print()
##
##second = int(input("Enter seconds: "))
##seconds = second%60
##minute = second//60
##hr = minute//60
##if minute>60:
##    minute = minute//60
##
##print(hr," ",minute," ",seconds)




##
##import math
##
### --- Part 1: Compute sin, cos, tan for user input ---
##angle_deg = float(input("Enter angle in degrees: "))
##angle_rad = math.radians(angle_deg)
##
##print(f"Angle: {angle_deg}°")
##print(f"sin({angle_deg}°) = {math.sin(angle_rad):.4f}")
##print(f"cos({angle_deg}°) = {math.cos(angle_rad):.4f}")
##print(f"tan({angle_deg}°) = {math.tan(angle_rad):.4f}")
##
### --- Part 2: Print sin/cos table from 0° to 345° in 15° steps ---
##print("\nAngle |   sin   |   cos")
##print("-------------------------")
##for deg in range(0, 346, 15):
##    rad = math.radians(deg)
##    print(f"{deg:3}°  | {math.sin(rad):.4f} | {math.cos(rad):.4f}")

