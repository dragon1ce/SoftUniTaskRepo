# cards = input().split(" ")
# shuffle_count = int(input())
#
# first_card = cards[0]
# last_card = cards[-1]
# cards_list = cards[1:-1]
# # print(cards_list)
# half_deck_count = int(len(cards_list) / 2)
#
# # print(f"First Half = :{first_half} and Second Half = :{second_half}")
# for shufle in range(1, shuffle_count + 1):
#     first_half = cards_list[:half_deck_count]
#     second_half = cards_list[half_deck_count:]
#     c= 0
#     for i in range(len(first_half)):
#         first_half.insert(c, second_half[i])
#         c += 2
#     cards_list = first_half
# cards_list.insert(0, first_card)
# cards_list.append(last_card)
# print(cards_list)
left = []
right = []
shuffled = input().split(" ")
shuffle_count = int(input())
mid = len(shuffled)//2
for j in range(shuffle_count):
    left = shuffled[0:mid]
    right = shuffled[mid:]
    shuffled.clear()
    for k in range(mid):
        shuffled.append(left[k])
        shuffled.append(right[k])
print(shuffled)
