numbers=[-3,5,-1,8,0,-4]
print("Given inputs is",numbers)
positive_list=[num for num in numbers if num>0]
squares=[numbers**2 for numbers in positive_list]
print("Positive numbers",positive_list)
print("Squares",squares)