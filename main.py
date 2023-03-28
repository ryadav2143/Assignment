
# Q1. You are writing code for a company. The requirement of the company is that you create a python
# function that will check whether the password entered by the user is correct or not. The function should
# take the password as input and return the string “Valid Password” if the entered password follows the
# below-given password guidelines else it should return “Invalid Password”.
# Note: 1. The Password should contain at least two uppercase letters and at least two lowercase letters.
# 2. The Password should contain at least a number and three special characters.
# 3. The length of the password should be 10 characters long.

def check_password(pasword):
    lower = []
    upper = []
    special_char = 0
    bool = False

    lower = [i for i in pasword if i == i.lower()]
    new_lower = list(filter(lambda x: not x.isdigit(), lower))
    upper = [i for i in pasword if i == i.upper()]
    new_upper = list(filter(lambda x: not x.isdigit(), upper))
    numaric = [i for i in pasword if i.isnumeric()]
    new_numaric = list(filter(lambda x: x.isdigit(), numaric))
    for i in pasword:
        if i.isalpha():
            continue
        elif i.isdigit():
            continue
        else:
            special_char = special_char + 1
    print(special_char)

    if len(new_lower) >= 2 and len(new_upper) >= 2 and len(new_numaric) >= 2 and special_char>=3 and len(pasword)>10:
        print("valid password")
    else:
        print("not valid")


enter = input()
check_password(enter)

# Q2. Solve the below-given questions using at least one of the following:
# 1. Lambda function
# 2. Filter function
# 3. Zap function
# 4. List Comprehension

# Check if the string starts with a particular letter
txt = "Hello, welcome to my world."
start_with = txt.startswith("H")
print(start_with)

# Check if the string is numeric
str = input()
numaric = [str.isnumeric()]
print(numaric)

# Sort a list of tuples having fruit names and their quantity. [("mango",99),("orange",80), ("grapes", 1000)
sort = [("mango",99),("orange",80), ("grapes", 1000)]
sorted_list = print([sorted(sort)])

# Find the squares of numbers from 1 to 10
# Find the cube root of numbers from 1 to 10.
cube_square_list= range(1,11)
cube = list(map(lambda x: x*x*x,cube_square_list))
print(cube)
square = list(map(lambda x: x*x,cube_square_list))
print(square)

# Check if a given number is evenY
a = int(input())
even_or_not = [ print("even number") if a%2==0 else print("odd number")]

# Filter odd numbers from the given list.[1,2,3,4,5,6,7,8,9,10]
odd = [1,2,3,4,5,6,7,8,9,10]
odd_list = [i for i in odd if i%2!=0]
print(odd_list)

# Sort a list of integers into positive and negative integers lists.
# [1,2,3,4,5,6,-1,-2,-3,-4,-5,0]
l1 = [1,2,3,4,5,6,-1,-2,-3,-4,-5,0]
newlist = list(filter(lambda x: x>=0,l1))
newlist1 = list(filter(lambda x: x<0,l1))
print(newlist)
print(newlist1)
