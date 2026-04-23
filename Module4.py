##n = int(input("Enter a positive no: "))
##f= 1
##
##for i in range(1,n+1):
##    f = f*i
##
##print(f"Factorial of {n} is {f}.")
    
##import time
##
### Simulated sensor reading loop
##for i in range(5):  # read 5 times
##    distance = 100 - i*10  # fake sensor data
##    print(f"Sensor reading {i+1}: {distance} cm")
##    time.sleep(1)  # delay to mimic real sensor polling
##

##"""
##Motor Control Loop
##"""
##speed = 0
##while speed < 100:  # accelerate until max speed
##    print(f"Motor speed: {speed}")
##    speed += 20

import time

# Simulated sensor loop
while True:
    distance = 43  # pretend sensor value
    print(f"Distance sensor: {distance} cm")
    time.sleep(1)  # wait 1 second
