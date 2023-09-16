from math import ceil

budget = float(input())
students = int(input())
price_flour = float(input())
price_one_egg = float(input())
price_eggs_per_student = price_one_egg * 10
price_apron = float(input())
apron_quant = ceil(students * 1.2)
package_free = students // 5
flour_quant = students - package_free
budget_needed = (flour_quant * price_flour) + \
                (students * price_eggs_per_student) + \
                (apron_quant * price_apron)
diff = abs(budget-budget_needed)

if budget >= budget_needed:
    print(f"Items purchased for {budget_needed:.2f}$.")
else:
    print(f"{diff:.2f}$ more needed.")