employee_happiness = list(map(int, input().split()))
happiness_factor = int(input())
employee_happiness = list(map(lambda x: happiness_factor * x, employee_happiness))
avg_happiness = sum(employee_happiness) / len(employee_happiness)
counter = 0
for happy in employee_happiness:
    if happy >= avg_happiness:
        counter += 1
if counter >= len(employee_happiness) / 2:
    print(f"Score: {counter}/{len(employee_happiness)}. Employees are happy!")
else:
    print(f"Score: {counter}/{len(employee_happiness)}. Employees are not happy!")
