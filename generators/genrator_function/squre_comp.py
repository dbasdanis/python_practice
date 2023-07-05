my_list = [num ** 2 for num in range(1,10)]
print(my_list)

# Generators Expressions
# This is how you create a list comprehensionL
# my_list = (expression for element in iterable)
my_list = (num ** 2 for num in range(1,10))
print(my_list)