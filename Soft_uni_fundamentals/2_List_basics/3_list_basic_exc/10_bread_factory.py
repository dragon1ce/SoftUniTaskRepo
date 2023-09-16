import sys

events_string = input().split("|")
event_list = [x.split("-") for x in events_string]
energy = 100
coins = 100
failed = False

for event in event_list:
    key = event[0]
    value = int(event[1])

    if key == "rest":
        if energy + value <= 100:
            energy += value
            print(f"You gained {value} energy.")
        else:
            gained_energy = 100 - energy
            print(f"You gained {gained_energy} energy.")
            energy = 100
        print(f"Current energy: {energy}.")

    elif key == "order":
        energy -= 30
        if energy >= 0:
            coins += value
            print(f"You earned {value} coins.")
        else:
            energy += 80
            if energy > 100:
                energy = 100
            print("You had to rest!")

    else:
        if coins >= value:
            coins -= value
            print(f"You bought {key}.")
        else:
            print(f"Closed! Cannot afford {key}.")
            sys.exit()
if not failed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")

