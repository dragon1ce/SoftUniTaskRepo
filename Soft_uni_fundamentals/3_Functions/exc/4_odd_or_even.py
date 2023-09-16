numb = input()
def odd_and_even(numb):
    even_sum = 0
    odd_sum = 0
    for i in range(len(numb)):
        current_num = int(numb[i])
        if current_num % 2 == 0:
            even_sum += current_num
        else:
            odd_sum += current_num
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"
print(odd_and_even(numb))