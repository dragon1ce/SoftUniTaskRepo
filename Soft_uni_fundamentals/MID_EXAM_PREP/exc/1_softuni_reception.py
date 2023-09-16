import math

first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
student_count = int(input())
hours_counter = 0
while student_count > 0:
    hours_counter += 1
    if hours_counter % 4 == 0:
        continue
    student_count -= (first_employee_efficiency + second_employee_efficiency + third_employee_efficiency)
print(f"Time needed: {hours_counter}h.")


first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
student_count = int(input())
total_efficiency = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency
hours_needed = student_count / total_efficiency
xa = math.ceil(hours_needed)
xaxa = xa // 4
print(f"Time needed: {xa + xaxa}h.")