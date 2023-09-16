number_to_check = int(input())
is_prime = True
for num in range(2,number_to_check):
    if number_to_check % num == 0:
        is_prime = False
        break
print(is_prime)