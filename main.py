# List Comprehension
# new_list = [new_item for item in list]
# [action, for iteration in iterable] works like map in JavaScript
num_list = [0,1,2,3,4,5,6,7,8,9]
squared_num_list = [item**2 for item in num_list]
print(f"squared_num_list: {squared_num_list}")
# Action can be a function
def square_num(number):
    number = number**2
    return number
squared_num_list_function = [square_num(item) for item in num_list]
print(f"squared_num_list_function: {squared_num_list_function}")
# Iterable can be:
# String
name = "Ryan"
characters = [item for item in name]
print(f"characters: {characters}")
# Range
doubles = [2*item for item in range(10)]
print(f"doubles: {doubles}")

# Conditional List Comprehension
# Example get all even and odds
# new_list = [new_item for item in list]
# [action, for iteration in iterable if test/conditional= True]
even_nums = [item for item in range(100) if item%2==0]
print(f"even_nums: {even_nums}")
odd_nums = [item for item in range(100) if not item%2==0]
print(f"odd_nums: {odd_nums}")

# Iterate over 2 files of numbers and find matches
with open("file1.txt", "r") as file:
    list_1_string = file.read().splitlines()
    list_1_integer = [int(item) for item in list_1_string]

with open("file2.txt", "r") as file:
    list_2_string = file.read().splitlines()
    list_2_integer = [int(item) for item in list_2_string]

result = [item for item in list_1_integer if (item in list_2_integer)]

print(result)