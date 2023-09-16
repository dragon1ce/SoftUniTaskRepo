entry_data = input().split(">>")
valid_types = ("family", "heavyDuty", "sports")
total_tax_collected = 0


def calc_tax(initial_tax, tax_decline_per_year, tax_increase_per_km,
             km_for_increase, years_used, kilo_traveled):
    tax_decline_for_years = initial_tax - (tax_decline_per_year * years_used)
    tax_increased_times = kilo_traveled // km_for_increase
    new_tax_price = tax_decline_for_years + (tax_increased_times * tax_increase_per_km)
    return new_tax_price


for vehicle in range(len(entry_data)):
    list_vehicle = entry_data[vehicle].split()
    type_car = list_vehicle[0]
    years_used = int(list_vehicle[1])
    kilo_traveled = int(list_vehicle[2])
    tax_to_pay = 0
    if type_car not in valid_types:
        print("Invalid car type.")
        continue
    elif type_car == "family":
        initial_tax = 50
        tax_decline_per_year = 5
        tax_increase_per_km = 12
        km_for_increase = 3000
        tax_to_pay = calc_tax(initial_tax, tax_decline_per_year, tax_increase_per_km,
                              km_for_increase, years_used, kilo_traveled)
    elif type_car == "heavyDuty":
        initial_tax = 80
        tax_decline_per_year = 8
        tax_increase_per_km = 14
        km_for_increase = 9000
        tax_to_pay = calc_tax(initial_tax, tax_decline_per_year, tax_increase_per_km,
                              km_for_increase, years_used, kilo_traveled)
    elif type_car == "sports":
        initial_tax = 100
        tax_decline_per_year = 9
        tax_increase_per_km = 18
        km_for_increase = 2000
        tax_to_pay = calc_tax(initial_tax, tax_decline_per_year, tax_increase_per_km,
                              km_for_increase, years_used, kilo_traveled)
    total_tax_collected += tax_to_pay
    print(f"A {type_car} car will pay {tax_to_pay:.2f} euros in taxes.")
print(f"The National Revenue Agency will collect {total_tax_collected:.2f} euros in taxes.")
