list_nums = input().split(", ")
possitive_list = [x for x in list_nums if int(x) >= 0]
negative_list = [x for x in list_nums if int(x) < 0]
even_list = [x for x in list_nums if int(x) % 2 == 0]
odd_list = [x for x in list_nums if int(x) % 2 != 0]
print(f"Positive: {', '.join(possitive_list)}")
print(f"Negative: {', '.join(negative_list)}")
print(f"Even: {', '.join(even_list)}")
print(f"Odd: {', '.join(odd_list)}")
