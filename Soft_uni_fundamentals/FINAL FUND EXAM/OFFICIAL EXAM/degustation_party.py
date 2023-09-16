def liked(guest_dict, guest, meal) -> dict:
    if guest in guest_dict.keys():
        if meal not in guest_dict[guest]:
            guest_dict[guest].append(meal)
    elif guest not in guest_dict.keys():
        guest_dict[guest] = [meal]
    return guest_dict


def disliked(guest_dict, guest, meal) -> dict:
    global disliked_meals
    if guest not in guest_dict.keys():
        print(f"{guest} is not at the party.")
    if guest in guest_dict.keys():
        if meal not in guest_dict[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection.")
        else:
            i = guest_dict[guest].index(meal)
            guest_dict[guest].pop(i)
            disliked_meals += 1
            print(f"{guest} doesn't like the {meal}.")
    return guest_dict


guests = {}
disliked_meals = 0
while True:
    command = input()
    if command == "Stop":
        break
    satisfied, guest_now, meal_now = command.split("-")
    if satisfied == "Like":
        guests = liked(guests, guest_now, meal_now)
    elif satisfied == "Dislike":
        guests = disliked(guests, guest_now, meal_now)

for key, value in guests.items():
    print(f"{key}: {', '.join(value)}")
print(f"Unliked meals: {disliked_meals}")