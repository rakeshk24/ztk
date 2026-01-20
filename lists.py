
#tasklist1

# print("this is a gme where you are asked to enter the fruit names")

# in_name = input("enter a fruit name or quite to exit: ")
# fruit_names = []

# while in_name != "quit":
#     fruit_names.append(in_name)
#     in_name = input("enter a fruit name or quite to exit: ")

# print("done entering names")
# guess = input("now guess a name from the fruit list: ")

# while guess not in fruit_names:
#     guess = input("wrong. guess a name from the fruit list: ")

# print("you got it, congrats")

#tasklist2

# name = input("enter a capital city name or 0 to quit: ")
# capitals = []

# while name != "0":
#     if name not in capitals:
#         capitals.append(name)
#     name = input("enter a capital city name or 0 to quit: ")

# capitals.sort(key = len)
# print(capitals)

#tasklist3

# name_score = ["rak - 70", "apa - 80", "rah - 90"]
# score = []
# for _ in name_score:
#     score.append(int(_.split("-")[1]))

# sum = 0
# for _ in score:
#     sum += _

# print(round(sum/len(score),0))

#tasklist4

# from random import randint

# names = input("enter names with spaces in between: ")
# number_of_teams = 3
# names = names.split()

# for name in names:
#     team = randint(1,number_of_teams)
#     print(f"{name} in {team} team")


#tasklist5
# print("price trend analysis")
# prices = input("enter prices with space in between: ").split(" ")
# prices = list(map(int, prices))
# plus = 0
# minus = 0
# for i in range(len(prices)):
#     if prices[i] < prices[len(prices)-i+1]:
#         plus += 1
#     elif prices[i] > prices[len(prices)-i+1]:
#         minus += 1
# if plus > minus:
#     print("increasing trend")
# elif plus < minus:
#     print("decreasing trend")

#tasklist6
# fruit_list = ['apple', 'banana', 'orange', 'straw', 'kiwi', 'straw']

# guess = input("guess the fruit name in the list: ")
# count = fruit_list.count(guess)
# print(f"{guess} appears {count} times in the list")

#tasklist7

# def find_position(num:int, numbers:list) -> list:
#     positions = []
#     for i in range(len(numbers)):
#         if num == numbers[i]:
#             positions.append(i+1)
#     return positions
    
# num_list = [10, 20, 30, 40, 10, 20, 40]
# num_guess = int(input("enter a number: "))
# index_list = []
# if num_guess in num_list:
#     index_list = find_position(num_guess, num_list)
# else:
#     print("number not in the list")

# print(index_list)

#tasklist8
teacher = []
name = input("enter your name: ").capitalize()
position = input("enter your position: ").capitalize()
students_list = list(map(int, input("enter the student groups size with space in between: ").split()))

teacher.append(name)
teacher.append(position)
teacher.append(students_list)
print(teacher)