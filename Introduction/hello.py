# print("Hello, World!")
# print(2+5)
# print("2+3")
# print("2+3=" + str(2+3))

# age =10
# print(age)

# a = 5
# b = 6
# print(a+b)
# print(a)
# print(b)
# b = 9
# print(b)
# print(10/2+5)

# -----------------String Concatenation-----------------

# a = "Hello"
# b = "World"
# print(a+" "+b)


# ------------------String Repetition------------------

# a = "Pavan" * 5
# print(a)

# -------------------String Lenght------------------

# a = "Bhagavn pavan"
# Lenght = len(a)
# print(Lenght)

# b = input("Enter Input :")
# Lenght = len(b)
# print(Lenght)


# Name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello " + Name + ", you are " + age + " years old.")
# ----Accesing Specific Characters in String

# print(Name[5])

# ---------------------Stirng Slicing---------------------

# Name = "Pavan"
# print(Name[0:3])

# print(Name[2:])

# print(Name[:4])

# print(Name[:])


# ----------------------Checking Data Type ---------------------

# print(type(5)) # int
# print(type(5.0)) # float
# print(type("5")) # str
# print(type(True)) # bool
# print(type(None)) # NoneType
# print(type('a')) # str
# print(type("a")) # str
# print(type([1, 2, 3])) # list
# print(type((1, 2, 3))) # tuple


# ------------------------------Type Convertion --------------------------

# a = "5"
# a = int(a)
# print(type(a)) # int
# print(a)
# print(a+5) # 10


# b = "2.5"
# b = float(b)
# print(type(b)) # float
# print(b)
# print(int(b)) # 2


# a = input(); b = input(); print(int(a) + int(b))

# a = input()
# a = int(a)
# b = input()
# b = int(b)
# result = a+b

# print(result)


# # hello.py
# a = input("Enter first number: ")
# b = input("Enter second number: ")
# print(int(a) + int(b))

# a = input()
# a = int(a)
# b = input()
# b = int(b)

# result = a+b

# print("sum" +" "+ str(result))



# -----------------Relational Operators-----------------------

# print(5<10)

# print(5>10)

# Q) Compare two strings in a first three characters are same or not using input for user

# str1 = input("Enter String 1 :")
# str2 = input("Enter String 2 :")

# a = str1[0:3]
# print(a)
# b = str2[0:3]
# print(b)
# print(a == b)


# Q ) Write a program to check if both the numbers are positive and if atleast one of the numbers is greater than 5.

# a = input("Enter the first number :")
# b = input("Enter the second number :")
# d = int(a)
# c = int(b)

# is_positive = (d > 0) and (c > 0)

# is_greater_than = (d > 5) or (c > 5)

# result = is_positive and is_greater_than

# print(result)


# -----------------------Conditional Statements--------------------------

 
# a = int(input("enter first number :"))
# b = int(input("enter second number :")) 

# if a > b :
#     print("a is bigger")
# else :
#     print("b is Bigger")


# if 2 < 3 :
#     print("2 is less than 3.")
# print("End")


# Q ) Write a program to print the greatest among the two nubers.

# a = int(input("Enetr the first number :"))
# b = int(input("Enter the second number :"))

# if a > b :
#     print(a)
# else :
#     print(b)


# Q ) Write a program that reads a single line of input and pints tha first and last 
#     characters of the given input and print the asterisk (*) in place of the remaining characters.

# single_line = input()

# First_char = single_line[0]
# str_lenght = len(single_line)
# last_char = single_line[str_lenght - 1]
# stars = "*" * (str_lenght - 2)
# result = First_char + stars + last_char
# print(result)

# Q ) Write a program to check if the given two dogit number is greater than 25 and 
#     its first digit is greater than its second digit.

# -------------Solution 1

# num = int(input("Enter the two Digit number :"))

# first_digit = num / 10
# second_digit = num % 10


# if num > 25 :
#     if first_digit > second_digit :
#         print("true")
# else :
#     print("false") 

# print("end")

# ----------------Solution 2
# it is  dynamic solution input is any number

# num = int(input())

# is_number_greater_than_25 = (num > 25)

# number_str = str(num)
# first_digit = int(number_str[0])
# str_len = len(number_str)
# last_digit = int(number_str[str_len - 1])

# is_first_digit_greater = (first_digit > last_digit)

# result = (is_first_digit_greater and is_number_greater_than_25)
# print(result)


# Q ) Write a program if the given number is even or odd

# num = int(input("Enter the number :"))

# result = (num % 2)

# if  result == 0:
#     print("Even")
# else :
#     print("Odd")

# ------------------Exponent Operator

# print(9**3)

# Q ) Given two integers a and b find the greatest among a**B (a power b) and 
#     b**a (b power a) and print the value

# a = int(input("Enter first number :"))
# b = int(input("Enter second number :"))

# first_power =  a**b
# print(first_power)
# second_power = b**a
# print(second_power)

# is_greater = (first_power > second_power)

# if is_greater :
#     print("First number Power of second number is Greater.")
# else:
#     print("Second number Power of first number is Greater.")


# Q ) Given a two digit number print "Lucky Number" if any of the following condition are satisfied
#         * the number is a multiple of 9
#         * One of the digit is 9 
#     print "Unlucky Number" in all other cases.

# -------------Solution 1


# num = int(input("Enter the number: "))

# is_multiple_of_9 = ((num % 9 ) == 0 )
# num_str = str(num) 
# length = len(num_str)
# first_digit = int(num_str[0])
# each_digit = int(num_str[1])
# i = 0
# result = "false"  # Initialize result to avoid NameError
# while i < length :
#     if num_str[i] == '9' :
#         result = "true"
#     i += 1

# any_is_true = (is_multiple_of_9 or result == "true")
    
# if  any_is_true :
#     print("Lucky Number")
# else :
#     print("Unlucky Number")
    
    
    
    
# Q ) Write a Program to print the greatest among the three numbers

# first = int(input("Enter first number :"))

# second = int(input("Enter second number :"))

# third = int(input("Enter third number :"))

# if first > second and first >third :
#     print("first number is correct")
    
# elif  second > first and second > third :
#     print("second number is greater")
    
# elif third > first and third > second :
#     print("third number is greater")
# else:
#     print("there is tie numbers are there")

# -------------------Solution 2

# a = int(input("enter 1st number :"))

# b = int(input("enter 2nd number :"))

# c = int(input("enter 3rd number :"))

# is_a_greatest = (a>b) and (a>c)

# if is_a_greatest :
#     print(a)
# else:
#     is_b_greatest = (b>c)
#     if is_b_greatest :
#         print(b)
#     else:
#         print(c)


# Q )  Write a program that checks whether the given number is divisible by 10 or by 5 or neither

a = int(input("Enter the number :"))

if (a % 10) == 0 :
    print(str(a) + " is Divisible by 10")
elif (a % 5) == 0 :
    print(str(a) + " is Divisible by 5")
else:
    print(str(a) +" is not Divisible by 10 or 5.")



