# ============ Question 1 --- Finding the Password

######  A detective got a latest case file. To solve it he needs to access a personal computer of a man
###### ---> The computer has a paper attached to it with a string S and number  writter
###### ---> The detective finds out that S is actually a secret code, designed to write in zig-zig pattern with height N
###### ---> The password for the computer is obtained by combining the latters form each row of zig-zag pattern. Help the detective by finding the password

##### ====> Main Question
#####       Write a program that reads a string S and a number N representing the secret code and the hight of it when written in zig-zag pattern.

#### =====> Solution Approach

#  ---> Iterate over the string
#  ---> Get the Position of each character of string based on the pattern(1 to N and N-1 to 3)
#  ---> Concatenate the characters of a string of a string with respect to their positons
#  ---> Print the Resultant string

def get_pattern(n):
    return list(range(1,n+1))+ list(range(2, n))[::-1]

def get_positions(pattern,word_length):
    pattern_length = len(pattern)
    repetitions = word_length // pattern_length
    extra = word_length % pattern_length
    positions = pattern * repetitions + pattern[:extra]
    return positions

def get_reordered_word(word,positions,n):
    new_word = ""
    for i in range(1, n+1):
        for j in range(len(positions)):
            if positions[j] == i:
                new_word += word[j]
    return new_word
            
def main():
    s = input()
    n = int(input())
    pattern = list(range(1,n+1)) + list(range(n-1,1,-1))
    positions = get_positions(pattern, len(s))
    new_word = get_reordered_word(s,positions,n)
    print(new_word)


main()

### input : bhagavanpavan
#           6
### output : bvhaaapngnaav











