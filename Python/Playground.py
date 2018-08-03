# #!/usr/bin/python
#
#
# # # # print("Hello, World!")
# # # #
# # # #
# # # #
# # # # i = 0
# # # #
# # # # while (i < 3):
# # # #     num = int(input("Enter a number"))
# # # #
# # # #     if num > 0:
# # # #         print("This number is positive")
# # # #     elif num < 0:
# # # #         print("This number is negative")
# # # #     else:
# # # #         print("This number is 0")
# # # #     i += 1
# # #
# # # greeting = "Hello, World!"
# # # for letter in greeting:
# # #     print(letter.upper())
# # #
# # #
# # # for i in range(10, 5, -1):
# # #     print(i)
# # #
# # #
# # # my_name = "Olivia"
# # # friend1 = "Jess"
# # # friend2 = "Julia"
# # # friend3 = "Ciera"
# # # friend4 = "Matthew"
# # #
# # # print("My name is " + my_name + " and my friends are " + friend1 + " , ")
# # # print("My name is %s and my friends are %s, %s, %s, and %s." %(my_name, friend1, friend2, friend3, friend4))
# # name = str(raw_input("Enter your name"))
# # adverb = str(raw_input("Enter an adverb"))
# # plural_noun = str(raw_input("Enter a plural noun"))
# # noun = str(raw_input("Enter another noun"))
# # noun2 = str(raw_input("Enter another noun"))
# # animal = str(raw_input("Enter an animal"))
#
#
#
# # print(("One day %s woke up and realized that they had slept through their alarm. %s sprinted to "
# # "the bus stop %s, dragging their %s behind them while shouting at the bus driver to stop. %s leaped over "
# # " a %s and almost bumped into a %s, desperate to not be late to school."
# # " Alas, the bus driver drove away, leaving %s to ride their %s to school.")
# # %(name, name, adverb, plural_noun, name, noun, noun2, name, animal))
#
# def greetSecretAgent(first_name, last_name):
#     return ("%s, %s %s") %(last_name, first_name, last_name)
#
# greeting = greetSecretAgent("Olivia", "Tobin")
# print(greeting)

# def mystery1(a):
#     return a + 5
#
# def mystery2(b):
#     return b * 2
#
# result = mystery1(mystery2(3))
#
#
# def mystery(word, number):
#     number = number * 2
#     word = word.upper()
#     return word * number #you can't multiply two strings
#
# print(mystery("2", "he"))


friends = ["Olivia", "Jackelen",
           "Phoebe", "Savion"]
myName = "olivia"
print("My name is %s and I have %s friends" %(myName, len(friends)))
friends.append("Areeta")
friends.insert(1, "Logan")
friends.remove("Areeta")

print("My friends are: ")
for i in range(0,len(friends)):
    if (i == 0):
        print(friends[0]),
    else:
        print("and " + friends[i])

print(range(4))




for friend in friends:
    print(friend)


# for i in range(0, len(friends)):
#     print(friends[i])
#
#
# tableGroups = [["Olivia", "Savion"], ["Jackelen", "Phoebe"]]
#
# for i in range(0, len(tableGroups)):
#     for j in range(0, len(tableGroups[i])):
#         print(tableGroups[i][j])
