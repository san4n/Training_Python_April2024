import time

for i in range(5,0,-1):
    print(i,end=' ')
    time.sleep(1) #delay for 1sec
print("Blast Off!")

##name = "Penang"
##
##for i in name:
##    print(i)

name = "Hassan"
for k in range(1,11):
    print(k,name)

x = len(name) # determine the no of characters

print(f"Characters in name are :{x}")
