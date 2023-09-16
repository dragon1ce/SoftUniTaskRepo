numbers = list(map(int, input().split()))
n = int(input())

# Remove the smallest n numbers from the list
remaining_numbers = sorted(numbers)[n:]

# Create a new list with the remaining numbers in the same order as in the input
result = [num for num in numbers if num in remaining_numbers]

# Join the remaining numbers with a comma and a space
output = ", ".join(map(str, result))

print(output)