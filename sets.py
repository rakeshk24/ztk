#task1
print("congrats, you have an invitation!")
lunch_rsvp = set()
dinner_rsvp = set()
while True:
    name = input("enter your name or x to exit: ").lower()
    if name == "x":
        break
    lunch = input("rsvp for lunch - y/n: ").lower()
    dinner = input("rsvp for dinner - y/n: ").lower()
    if lunch == "y":
        lunch_rsvp.add(name)
    if dinner == "y":
        dinner_rsvp.add(name)

print(f"lunch attendees are: {lunch_rsvp}")
print(f"dinner attendees are: {dinner_rsvp}")
print(f"common attendees for both lunch and dinner are: {lunch_rsvp.intersection(dinner_rsvp)}")
print(f"attendees for at least one of lunch and dinner are: {lunch_rsvp.union(dinner_rsvp)}")
      