temp=eval(input("Enter temp in Celcius: "))
f_temp=9/5*temp+32

print(f_temp)

if f_temp > 212:
    print("Temp is below the boiling point")
if f_temp < 32:
    print("Temp is below the freezing point")
