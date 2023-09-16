entry_data = input().split(", ")
sorted_list = sorted(entry_data, key=lambda x: (-len(x), x))
print(sorted_list)