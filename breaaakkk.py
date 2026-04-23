##temp = 0
##while temp != -1000:
##    temp = eval(input(': '))
##    if temp != -1000:
##        print(9/5*temp+32)
##    else:
##        print('Bye!')
##

print("*"*10)

while True:
    temp = eval(input(': '))
    if temp == -1000:
        print("Bye")
        break
    print(9/5*temp+32)
    
print("Out of Loop")
