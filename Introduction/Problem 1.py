#### ============================ String Validation
#### ====== Q 1 ) Write a program that reads a string S, and checks if the stirng S satisifies all the below conditions
####            --> S should contain only letters and underscored(_)
####            --> All letters in S should be in uppercase(A-Z)
#### Note : S can contain multiple words and all the words in S are separted by underscore (MANGO_TREE)
#### ================
#### Another question 2 ---> (a to z)
#### Another question 3 ---> (A to Z or a to z)
#### Another question 4 ---> S should contain only letters (A to Z or a to z)
####                    ---> The first word in S should always start with a lowercase letter




# Uppercase_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# def is_uppercase_letter(letter):
#     return letter in Uppercase_letter

# def is_underscore(character):
#     return character == '_'  

# def all_satisified(results):
#     final_result = True
#     for result in results:
#         final_result = final_result and result
#     return final_result    
    
# def get_no_of_words(s):
#     return len(s.split('_'))

# def is_valid_string(s):
#     results = []
#     for character in s:
#         result = is_uppercase_letter(character) or is_underscore(character)
#         results.append(result)
#     return all_satisified(results)

# def main():
#     string =  input()
#     is_valid = is_valid_string(string)
#     if is_valid :
#         print("Above string is all are capital and each character is separated by _")
#         result = "True " + str(get_no_of_words(string))
#     else:
#         result = False
#     print(result)
    
# main()


# ============= Another example same question

# Upper_case_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# def all_satisfied(results):
#     final_result = True
#     for result in results:
#         final_result = final_result and result
#     return final_result

# def is_valid_string(input_str):
#     reuslts = []
#     for cahr in input_str:
#         result = (cahr in Upper_case_letter) or (cahr == '_')
#         if result is False :
#             return False
#     return True

# def main():
#     input_str =  input()
#     is_valid = is_valid_string(input_str)
#     if is_valid :
#         print("Above string is all are capital and each character is separated by '_'")
#         result = "True " + str(len(input_str.split('_')))
#     else:
#         result = False
#     print(result)
    
# main()

## ========= Input = HOEHHH_HAFH_KEERTHI_PAVAN_GAYATHRI_MYLOVERS
## ========= OutPut = Above string is all are capital and each character is separated by '_'
##                    True 6

## ============== Question 2 ==============


# Lower_case_letter = "abcdefghijklmnopqrstuvwxyz"

# def all_satisfied(results):
#     final_result = True
#     for result in results:
#         final_result = final_result and result
#     return final_result

# def is_valid_string(input_str):
#     reuslts = []
#     for cahr in input_str:
#         result = (cahr in Lower_case_letter) or (cahr == '_')
#         if result is False :
#             return False
#     return True

# def main():
#     input_str =  input()
#     is_valid = is_valid_string(input_str)
#     if is_valid :
#         print("Above string is all are capital and each character is separated by '_'")
#         result = "True " + str(len(input_str.split('_')))
#     else:
#         result = False
#     print(result)
    
# main()


## ========= Input = my_name_bhagavan_pavan
## ========= OutPut = Above string is all are Small characters and each character is separated by '_'
##                    True 4


## ============== Question 3 ===================


# Both_case_letter = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# def all_satisfied(results):
#     final_result = True
#     for result in results:
#         final_result = final_result and result
#     return final_result

# def is_valid_string(input_str):
#     reuslts = []
#     for cahr in input_str:
#         result = (cahr in Both_case_letter) or (cahr == '_')
#         if result is False :
#             return False
#     return True

# def main():
#     input_str =  input()
#     is_valid = is_valid_string(input_str)
#     if is_valid :
#         print("Above string is all are both Upper and Lower and each character is separated by '_'")
#         result = "True " + str(len(input_str.split('_')))
#     else:
#         result = False
#     print(result)
    
# main()


## ========= Input = My_name_is_Bhagavan_Pavan
## ========= OutPut = Above string is all are both Upper and Lower and each character is separated by '_'
##                    True 5

small_case = "abcdefghijklmnopqrstuvwxyz"
Both_case_letter = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# check if the first character is lowercase
def first_letter_small(input_str):
    return len(input_str) > 0 and input_str[0] in small_case

# check full string validity
def is_valid_string(input_str):
    # first char must be small
    if not first_letter_small(input_str):
        return False

    # every char must be letter or '_'
    for char in input_str:
        if not (char in Both_case_letter or char == '_'):
            return False
    return True

# count words (split by '_' and also at uppercase letters)
def count_words(input_str):
    words = []
    word = input_str[0]  # start with first letter
    
    for ch in input_str[1:]:
        if ch == "_":  # underscore → new word
            words.append(word)
            word = ""
        elif ch.isupper():  # uppercase → new word
            words.append(word)
            word = ch
        else:
            word += ch
    if word:  # add last word if not empty
        words.append(word)
    return len(words), words

def main():
    input_str = input("Enter string: ")
    is_valid = is_valid_string(input_str)
    
    if is_valid:
        count, words = count_words(input_str)
        print("Above string is valid: starts with small and big letter, contains only letters or '_'")
        print("True", count)
        print("Words:", words)
    else:
        print(False)

main()


## ========= Input = my_Name_isBhagavan_Pavan
## ========= OutPut = Above string is valid: starts with small and big letter, contains only letters or '_'
##                    True 7

