#!/usr/bin/python
import random
#Exerise 1


def longest_word(word1, word2, word3):
    if len(word1) > len(word2) and len(word1) > len(word3):
        return word1
    elif len(word2) > len(word1) and len(word2) > len(word3):
        return word2
    else:
        return word3

print(longest_word("apples", "bananas", "oranges"))


#Exercise 2

def reverse_string(string):
    new_string = ""
    for i in range(len(string)-1, -1, -1):
        new_string += string[i]
    return new_string

print(reverse_string("Olivia"))

#Exercise 3
def sum_to_n(n):
    sum = 0
    for i in range(0, n+1):
        sum += i;
    return sum

print(sum_to_n(4))

#Exercise 4

def is_triangle(s1, s2, s3):
    if (s1 + s2 > s3):
        return True
    else:
        return False

print(is_triangle(4, 5, 9))

#Exercise 5

def roll_dice(numRolls):
    sum = 0
    for i in range(0, numRolls):
        sum += random.randint(1,6)
    return sum

print(roll_dice(2))




#Extension 2
def snake_case(word):
    new_string = ""
    starting_index = 0
    for i in range(0, len(word)):
        if word[i].isupper():
            new_string += word[starting_index: i]
            new_string += "_"
            starting_index = i
    return new_string

print(snake_case("ameliaBedelia"))
