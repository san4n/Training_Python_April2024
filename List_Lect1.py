#Creating list

my_list1= [1,2,3,4,5]
my_list2= []
my_list3= [2.4,5.366,5.98,8.7]
my_list4= ["apple","orange","banana","kiwi"]

my_list5= [4,8.5,6,"Hello!",[1,2,3,4]]

#Access Items of List
#Indexing

print(my_list1[2])#Print 3rd element of list1
# 3
print(my_list4[2])
# banana
print(my_list1[1:4])
# [2,3,4]
print(my_list1[:4])#default start from 0 index
# [1,2,3,4]
print(my_list1[1:])#default go until last index
# [2,3,4,5]

#Modifying List
# Update single item

my_list5=[10,20,30,40]
print(my_list5)
my_list5[2]='banana' # Update list, change the item at index 2

print(my_list5)
#[10, 20, 'banana', 40]
new_list = my_list5
print(new_list)
#[10, 20, 'banana', 40]
new_list[1:3] = ['apple',99]
print(new_list)
#[10,'apple',99, 40]













