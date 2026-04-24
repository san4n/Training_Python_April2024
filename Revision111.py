
x = [] #Create a empty list

n = int(input("Enter positive integer for length of list: ")) # Define range of the list

for i in range(n+1):
    num = eval(input("Enter a number: "))
    if num%5==0:
        print("Divisible by 5")
    else:
        print("No divisible by 5")
    x.append(num)

print(x) #print the list

for j in range(n+1):
    if x[j]%2==0:
        print(x[j]," is divisible by 2")
    else:
        print(x[j]," is not divisible by 2")
    
    
