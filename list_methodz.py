##my_list=[10,2,3,8,14,8,8,68,7,8,9,1]
##new_list=[5,89,1,2,54,0]
##
###list_name.method
##
##my_seclist= my_list
##
##my_seclist.sort(reverse=True) #
##new_list.sort()
##print(my_list)
##print(new_list)
##
##print(len(my_list)) #12
##
##n=0
for i in range(0,12):
    if my_list[i]==8:
        n=n+1
print("8 occurrence in my_list: ", n)

# Remove method to remove item

for j in range(n):
    my_list.remove(8)
##
##print(my_list)
##
### remove by index number
##
##y = my_list.pop(2)
##print (y)
##
##print(my_list)
##
### insert by index value
###add in the element
### index,value
##
##my_list.insert(8,999)
##print(my_list)
##my_list.insert(-1,105)
##print(my_list)


# Append method to addon elements
# at last of list

myy_list=[5,6,8,9]
myy_list.append(88)
print(myy_list)

#search the elements in list
party_list=['cake','balloons','chairs']

if 'cake' in party_list:
    print("Cake is in list")
else:
    print("Cake is not in list")

# slicing and concatenation

numbers = [1,2,3,4,5]
extra_numbers = [6,7]
new_list = numbers+extra_numbers
print(new_list)


# Combining two list

fruits = ['apple','banana']
more_fruits = ['orange','kiwi']

fruits.extend(more_fruits)
print(fruits)
print(more_fruits)

# reverse the list

fruits.reverse()
print(fruits)



























