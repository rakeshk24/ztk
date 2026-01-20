
#task1

# genres_shows = {
#     "comedy":"seinfeld",
#     "action":"khiladi",
#     "drama":"breaking bad",
#     "kids":"hanuman",
#     "suspense":"better call saul"
# }

# genre = input("enter the genre to find a suggestion: ").lower()

# if genre in genres_shows:
#     print(genres_shows[genre])
# else:
#     choice = input("do you want to add a new show? - y/n: ").lower()
#     if choice == "y":
#         show = input("enter the show: ").lower()
#         genres_shows[genre] = show
#         print(f"added a new entry: {genres_shows.popitem()}")
#     else:
#         print("thanks. exiting...")

#task2
# passport = {
#     "name":"rakesh",
#     "number":"12345",
#     "nationality":"india",
#     "expiry":"12-23-34"
# }
# choice = input("enter your choice: 1- to leave, 2 - to enter, 3 - to go home: ").lower()

# if choice == "1":
#     dest = input("pls enter destination: ").lower()
#     passport["destination"] = dest
#     print(passport)
# elif choice == "2":
#     if "destination" in passport:
#         passport.popitem()
#     else:
#         print("havent left the country yet")
# else:
#     print("going home. exiting...")

#task3

# print("this program collects a person's name and skills and then prints them")
# choice = input("enter 1 to continue or 0 to stop: ")
# name_skill = {}
# while choice != "0":
#     name = input("enter your name: ")
#     skills = list(input("enter your skills with space in between: ").split(" "))

#     name_skill[name] = skills
#     choice = input("enter 1 to continue or 0 to stop: ")

# for n, s in name_skill.items():
#     print(f"name is {n} and skills are {s}")

# for name in name_skill:
#     print(f"{name} : {name_skill[name]}")

#task4

# sentence = input("enter your sentence: ").split(" ")

# word_in_sentence_count = {}

# for word in sentence:
#     if word not in word_in_sentence_count:
#         word_in_sentence_count[word] = 1
#     else:
#         word_in_sentence_count[word] += 1

# for word in word_in_sentence_count:
#     print(f"{word} : {word_in_sentence_count[word]} counts")

# print(word_in_sentence_count)

#task5

# inventory = {
#     "milk" : 10,
#     "rice" : 100,
#     "onions" : 50,
#     "beer" : 25
# }

# choice = input("pick your option: 1 - check stock, 2 - add an item, 3 - restock an item, 4 - exit: ")

# while choice != "4":
#     if choice == "1":
#         print(inventory)
#     elif choice == "2":
#         item = input("enter the item you want to add: ")
#         quantity = input("enter the quantity: ")
#         inventory[item] = quantity
#         print(f"{item} with quantity - {quantity} added")
#     elif choice == "3":
#         item = input("enter the item you want to restock: ")
#         quantity = input("enter the quantity: ")
#         inventory[item] = quantity
#         print(f"{item}'s quantity updated with {quantity}")
#     else:
#         choice = input("enter a valid input")
#     choice = input("pick your option: 1 - check stock, 2 - add an item, 3 - restock an item, 4 - exit: ")