n = int(input())
parking = {}
for _ in range(n):
    entry = input().split()
    if entry[0] == "register":
        command, username, license_plate = entry
    elif entry[0] == "unregister":
        command, username = entry
    if command == "register":
        if username not in parking.keys():
            parking[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate}")
    elif command == "unregister":
        if username not in parking.keys():
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            parking.pop(username)
for key, value in parking.items():
    print(f"{key} => {value}")