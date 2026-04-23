# Get user input as a list of integers
nums = eval(input("Enter numbers separated by spaces: "))

# 1. Print count of items
print("Count of items:", len(nums))

# 2. Print last item
print("Last item:", nums[-1])

# 3. Print reverse of list
print("Reversed list:", nums[::-1])

# 4. Check if 5 is in the list
print("Contains 5?", 5 in nums)

# 5. Count how many times 5 appears
print("Count of 5s:", nums.count(5))

# 6. Print sorted list
print("Sorted list:", sorted(nums))

# 7. Trimmed list (remove first and last items)
trimmed = nums[1:-1]
print("Trimmed list:", trimmed)

# 8. Count items less than 5
count_less_than_5 = sum(1 for x in nums if x < 5)
print("Items less than 5:", count_less_than_5)
