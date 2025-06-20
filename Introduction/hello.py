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

# a = int(input("Enter the number :"))

# if (a % 10) == 0 :
#     print(str(a) + " is Divisible by 10")
# elif (a % 5) == 0 :
#     print(str(a) + " is Divisible by 5")
# else:
#     print(str(a) +" is not Divisible by 10 or 5.")


# --------------------------Loops -------------------

#  Q ) Let's write a code to print the next 3 consecutive numbers of the given integer input.



# a = int(input("Enter a number :"))
# i = 0
# while i < 3 :
#     a += 1
#     print(a)
#     i += 1
# print("End")

#  Q ) Write a program to print stars in N rows and N columns, where integer N is given as an input.


# a = int(input("Enter the number :"))
 
# i = 1
# while i <= a :
#     print("* " * a)
#     i += 1
    
# print("Complete")


# Q ) problem-----------------------

# a = input("enter the word :")

# i = 0
# lenght_of_a = len(a)
# while i < lenght_of_a :
#     print(a[i])
#     i += 1

# ------------For Loop
 
# name = "Pavan"
# for each_pavan in name :
#     print(each_pavan)


# num =  int(input("Enter the number :"))
# a = range(num)
# for each_pavan in (a) :
#     print(each_pavan)
    
    
# Q) Write a program to print right triangular pattern where integer N is given as input

# num = int(input("Enter a number :"))
# a = range(num)
# for each_num in a :
#     print("* " * (each_num + 1))


# -------------------Range
# Solution 1

# for each_num in range(3,10) :
#     print(each_num)

# Solution 2

# a = input("enter name:")
# len_of_a = len(a)
# b = a[0]
# for i in range(1,len_of_a) :
#     b = b + "-" + a[i]
# print(b)


# -----------------String Extended slicing

# name = "-R-a-v-i-"
# print(name[1:8:2])

# name = "Bhagavan Pavan"
# print(name[1:10:2])


# -------------------------String methods

# 1 ) is digit

# pin = "98439"
# is_digit = pin.isdigit
# is_4_digit = (len(pin) == 4)
# is_vaild =  is_digit and is_4_digit
# print(is_vaild)


# 2 ) strip

# num = " 84748 "
# str = num.strip()
# print(str)

# ------- Removing specified characters that are leading or trailing using strip(character)

# name = "B.Pavan.,   ,,,,....."

# name = name.strip("., ")
# print(name)

# 3 ) Replace

# sentence = "teh cat and teh dog"
# sentence = sentence.replace("teh","the")
# print(sentence)



# 4) Startswith

# url = "https:/onthegomodel.com"
# is_secure_url = url.startswith("https:/")
# print(is_secure_url)

# 5 ) Endswith

# gmail_id = "bhagavanpavna01@gmail.com"
# is_mail =gmail_id.endswith("@gmail.com")
# print(is_mail)


# 6) Upper


# name = "pavan"
# print(name.upper())

# 7) Lower

# name = "PAVAN"
# print(name.lower())



# ----------------------------------------Problem solving and debugging -------------------------------

# Q) Given a string to print substrings in expected pattern of N rows where N is the length of the string.

# str = input("Enter the word :")
# inde = 0
# lenght = len(str)

# for each_char in range(1,(lenght + 1)):
#     print (str[:each_char])


# Q) Given a string S and N integers, where N is the lenght of the string S. print the string after shuffling the character as per the order of the integers given.

# str = input("Enter the word :")
# shuffled_s = ""
# str_length =  len(str)
# # b = str(str_length)


# # print("Enter the cha values in " + b + "times")
# for i in range(str_length) :
#     index = int(input())
#     shuffled_s = shuffled_s + str[index]
    
# print(shuffled_s)


# Q ) Write a program to print if the given number is a prime number or not

# ---- 1  Approach

# a = int(input("Enter the number :"))

# i = 1
# count = 0
# while i <= a :
#     if a % i == 0 :
#         count += 1
#     i += 1

# if count == 2 :
#     print("the given number is Prime")
# else :
#     print("the given number is not a prime")


# ----------- 2 nd Approach

# a = int(input("Enter the number :"))

# count = 0

# for i in range(1,a) :
#     if (a % i) == 0 :
#         count += 1

# if count == 1 :
#     print("Prime Number")
# else :
#     print("Not a prime Number")

# ----------- 3 rd approach

# a = int(input("Enter the number :"))

# count = 0

# for i in range(2,a) :
#     if (a % i) == 0 :
#         count += 1

# if count == 0 :
#     print("Prime Number")
# else :
#     print("Not a prime Number")



# ----------Challenge

# n = int(input())
# k = n
# for i in range(1,n+1) :
#     spaces = " " * k
#     stars = "* " * i
#     print(spaces + stars)
#     k = k-1



# ------------------------Nested Loop

# for a in range  (3) :
#     print("puter :" + str(a))
#     for b in range (7,9) :
#         print(" inner : " + str(b))
# print("END")


# Q ) Write a program to print triangulaar pattern with numbers in N rows, where integer N is given as input.

# a = int(input("Enter width of the trinagle :"))

# for i in range (1,a+1):
#     k = ""
#     for j in range (1,i+1) :
#         k = k + str(j) + " "
#     print(k)
    
    
    
# n = int(input())
# for row_num in range (0,n+1) :
#     row_output = " "
#     seq_num = row_num
#     while seq_num > 0 :
#         row_output = row_output + str(seq_num)
#         seq_num = seq_num - 1
#     print(row_output)


# n = int(input())
# for row_num in range(n, 0, -1):
#     row_output = ""
#     seq_num = row_num
#     while seq_num > 0:
#         row_output += str(seq_num)
#         seq_num -= 1
#     print(row_output)


# --------------------------   Break

# for i in range (1,5) :
#     if i == 3 :
#         break
#     print(i)
# print("End")


# i = 0 
# while i < 10 :
#     if i == 5 :
#         break
#     print(i)
#     i += 1
# print("End")


# for a in range (2) :
#     print("Outer :" + str(a))
#     for b in range(4) :
#         if b == 4 :
#             break
#         print(" inner : " + str(b))


# Q) Given a sentence, print a new sentence with the first word in uppercase.

# ---------solution 1

# sentence = input()

# first_word = sentence[0:6]
# first_word_upper_case = first_word.upper()
# output = first_word_upper_case + sentence[6:]
# print (output)

# ---------------Solution 2


# sentence = input("Enter the sentence :")

# first_word_end_index = 0
# for char in sentence :
#     if char == " " :
#         break
#     else:
#         first_word_end_index = first_word_end_index + 1
        
# first_word = sentence[0:first_word_end_index]
# first_word_upper_case = first_word.upper()
# output = first_word_upper_case + sentence[first_word_end_index:]
# print(output)


# -----------------------Continue


# for a in range(3):
#     if a == 1:
#         continue
#     print(a)
# print("End")

# ---------------------- Pass

# age = int(input() )
# output = ""
# if age >= 20:
#     print("Your age is "+  str(age) + ". Your an adult now.")
# elif age > 12 :
#     pass
# else:
#     pass


# -----------identify the imstake


# n = int(input())
# is_prime = True
# for i in range(2,n) :
#     if(n % i) == 0:
#         is_prime = False
#         break
# print(is_prime)


# ------------------------unicodes-----------------

# ------- ord ()  its return the order value of the given character
# unicode_value = ord("G")
# print(unicode_value)

# ---------chr ()   it can return the character for given order of number

# char = chr(80)
# print(char)

# for i in range(1,250) :
#     char = chr(i)
#     print(char)
# print("End")


# ----------------------Comparing strings-----------------


# print("777" < "7777")
# print("89"< "99")
# print("99" > "80")

# help("keywords")

# ----------------------Round --------------------------

# a =  round(10.38575888,2)
# print(a)

# b = round(10,3)
# print(b)

# a = 0.1+0.2
# print(a)
# a = round(a,1)
# print(a)
# print(a == 0.3)

# ------------------------- Hollow Diamond Pattern
# Q ) Write a program to print hollow diamond pattern of size N(2*N-1 rows),
#     where integer N is given as an input.

# n = int(input())

# left_space_count = n-1
# left_space = " " * left_space_count
# row_output = left_space + "*"
# print(row_output)


# hellow_space_conut = -1
# for row in range(2,n+1):
#     left_space_count = n-row
#     left_space = " " * left_space_count
#     hellow_space_conut = hellow_space_conut + 2
#     hellow_space = " " * hellow_space_conut
#     row_output =  left_space + "*" + hellow_space + "*"
#     print(row_output)

    
# for row_bottom in range(1,n-1) :
#     left_space_count = row_bottom
#     left_space = " " * left_space_count
#     hellow_space_conut = hellow_space_conut - 2
#     hellow_space = " " * hellow_space_conut
#     row_output = left_space + "*" + hellow_space + "*"
#     print(row_output)
    
# left_space_count = n-1
# left_space = " " * left_space_count
# row_output = left_space + "*"
# print(row_output)



# ------------- Debug the question


# n = int(input())
# for i in range(1,n+1):
#     row_out = " " * (n-i)
#     row_out = row_out + "$" * n
#     print(row_out)


# -------------Floor Division------------

# print(3//2)         # it refers to integral part only

# # --------------String Escape Characters------------------

# # ---------------------         "\"   is alwayse escape character

# print("Bhagavan\npavan")                  #  ----------  \n is a New line escape character

# print("bhagavan\tpavan")                  #  ====------   \t is a tab character

# print("bhagavan\\pavan")                  #  ---------    \\ is back slash escape character

# print('it\'pavan')                        #  ---------    \' is a single quot escape char

# print("it\"pavan")                        #  ---------    \" is a double quot escape character


# Q ) Given two strings, print Yes if the second string is a subsequence of first string. Otherwise, print None

# strings =   abcde
#         =   ace

# Solution :

# full_string = input()
# sub_sequence = input()

# subseq_index = 0
# subseq_len = len(sub_sequence)

# for char in full_string:
#     if char == sub_sequence[subseq_index]:
#         subseq_index += 1
#         if subseq_index == subseq_len :
#             break

# if subseq_index == subseq_len :
#     print("Yes")
# else:
#     print("No")
 


# n = int(input())
# for i in range (1,n+1):
#     spaces = " "*(n-i)
#     left_nums = ""
#     right_muns = ""
#     for j in range(1,i+1) :
#         left_nums = str(j) + left_nums
#         right_muns = right_muns + str(j)
#     print(spaces + left_nums + right_muns[1:])


# ---------------------------- List --------------------

# a = 2 
# list_a = [5,"six",a,8.2]
# list_b = [1,list_a]
# print(type(list_a))
# print(list_a)
# print(len(list_a))
# print(type(list_b))
# print(list_b)
# print(len(list_b))

# ------------------ Accessing elements

# print(list_b[1])
# print(list_a[1])

# ---------------------  Iterating Over a List

# for item in list_a :
#     print(item)
   

# ----------------------- List Concatenation

# list_a = [1,2,3,4]
# list_b = ["a","b","c"]
# list_c = list_a + list_b
# print(list_c)

# --------------------------- Adding elements in a list

# list_a = []
# print(list_a)
# for i in range(1,5):
#     list_a += [i]
#     print(list_a)
    
# print(list_a)
    
    
# --------------------------- Repetation of list

# list_a = [1,2]
# list_b = list_a * 3
# print(list_b)


# ----------------------------  Obtain part of a list

# Obtaining a part of a list is called list slicing

# list_a = [1,2,3,4,5,6,7,8,9,10,11]
# list_b = list_a[:3]
# print(list_b)

# ----------- Estended slicing (step jumping)

# list_c = list_a[0:10:2]
# print(list_c)


# ----------------- Converting to list

# color = "red"
# list_a = list(color)
# print(list_a)

# -------------------  List of range

# list_a = list(range(4))
# print(list_a)

# ----------------------- List are mutable

# Lists can be modified items at any position can be updated

# list_a = [1,2,3,4,6]
# print(list_a)
# list_a[4] = 5
# print(list_a)

# ------------Identify the mistake

# animals = ['cat','dog']
# wild_animals = ['tigeer','fox'] 
# animals += [wild_animals]
# print(animals)


# ----------------- Objects

# print(id("Hello"))

# a = "Hello"
# print(id(a))
# a = a + " World"
# print(id(a))

# list_a = [1,2,3,4]
# list_b = list_a
# list_a += [5,6]
# print("list_a: " + str(list_a))
# print("list_b: " + str(list_b))


# list_a = [1,2]
# list_b = [3,list_a]
# list_a[1] = 4
# print(list_a)
# print(list_b)


# a = 2
# list_a = [1,a]
# print(list_a)
# a = 3
# print(list_a)
# list_a = [1,a]
# print(list_a)



# ----------------------- Splitting a string

# str = "1.2.3.4.5.6.7.8.9."
# str_list = str.split(".")
# print(str_list)

# nums = "1 2 3 4 5 "
# num_list = nums.split()
# print(num_list)


# string_a = "Python is a programming language"
# list_a = string_a.split('a')
# print(list_a)


# ----------------------- Joining strings

# Takes all the items in a sequence of string and joins them into one string



# list_a = "Python is a programming language"
# string_split = list_a.split("a")
# print(string_split)
# # list_a = ['python is ',' progr','mming l','ngu','ge']
# string_a = "a".join(string_split)
# print(string_a)


# list_a = list(range(4))
# string_a = ",".join(list_a)
# print(string_a)        #---------it will be error


# -----------------------List Negative Indexing

# list_a = [1,2,3,4,5,6,7,89,0]
# print(list_a[-1])
# print(list_a[-2])
# print(list_a[-3])
# print(list_a[-4])
# print(list_a[-5])


# ----------------- Negative indexing Slicing

# list_a = [1,2,3,4,5,6,7,8,9]
# list_b = list_a[-3:-1]
# print(list_b)

# ---------- Negative step size

# list_a = [1,2,3,4,5,6,7,8]
# list_b = list_a[4:1:-1]
# print(list_b)


# list_a = [1,2,3,4,5,6]
# list_b = list_a[::-1]
# print(list_b)

# str_1 = "Program"
# str_2 = str_1[::-1 ]
# print(str_2)



# ------------------- Identify the mistake


# list_a = input().split(",")
# list_b = input().split(",")
# len_of_list_a = len(list_a)
# n = len_of_list_a - 1
# for i in range(len_of_list_a) :
#     num_1 = list_a[i]
#     num_2 = list_b[n-i]
#     result = str(num_1) + " " + str(num_2)
#     print(result)


# -------------------------Function -----------------


# def greet() :
#     print("Hello")
    
# name = input()
# greet()
# print(name) 

# --------- function srting concatination -----------

# def greet(word) :
#     msg = "Hello " + word
#     print(msg)

# name = input()
# greet(word = name)


# --------------------- Returning a Value -------------------

# def greet(word) :
#     msg = "Hello " + word
#     return msg

# name = input()
# greeting = greet(word = name)
# print(greeting)


# ------------------- Identify the mistake

# def get_list(string_a) :
#     list_a = string_a.split(',')
#     len_list_a = len(list_a)
#     for i in range(len_list_a):
#         list_a[i] = int(list_a[i]) ** 2
        
#     return list_a

# string_a = input()
# numbers_list = get_list(string_a)
# print(numbers_list)



# -------------------- Multiple arguments ---------------

def greet(arg_1,arg_2) :
    print(arg_1 + " " + arg_2)

greeting = input("Enter your first name :")
name = input("Enter your second name :")
greet(greeting,name)




