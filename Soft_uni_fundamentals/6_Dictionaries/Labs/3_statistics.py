my_dict = {}
command = input()
while command != "statistics":
    key, value = command.split(": ")
    if key in my_dict:
        my_dict[key] += int(value)
    else:
        my_dict[key] = int(value)
    command = input()
print("Products in stock:")
for key, value in my_dict.items():
    print(f"- {key}: {value}")
print(f"Total Products: {len(my_dict)}")
print(f"Total Quantity: {sum(my_dict.values())}")
