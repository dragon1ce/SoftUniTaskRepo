number_of_lines = int(input())
positive_list = []
negative_list = []
for line in range(number_of_lines):
    num = int(input())
    if num >= 0:
        positive_list.append(num)
    else:
        negative_list.append(num)
sum = 0
for nums in negative_list:
    sum += nums
print(positive_list)
print(negative_list)
print(f"Count of positives: {len(positive_list)}\n"
      f"Sum of negatives: {sum}")
