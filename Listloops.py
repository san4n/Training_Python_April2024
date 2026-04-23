# loops in list

my_list= [5,55,555]

for i in my_list:
    print(i)

    
m_list=[10,20,30,40,50,60,70,80,90]

"""
i.   Access and print the third element
ii.  Slice and print elements from index 2 to 5
iii. Use negative indexing to print last two elements
iv.  Use search method to find 80 in list

"""
print(m_list[2])
print(m_list[2:6])
print(m_list[-2:])

if 80 in m_list:
    print("80 is Present")
else:
    print("80 is not Present")

print(min(m_list)) #10
print(max(m_list)) #90
print(sum(m_list[:5])) #150
print(sum(m_list[5:])) #300





