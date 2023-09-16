quantity = int(input())
days = int(input())

ornament_price = 2
ornament_points = 5

tree_skirt_price = 5
tree_skirt_points = 3

tree_garland_price = 3
tree_garland_points = 10

tree_lights_price = 15
tree_lights_points = 17

total_spending = 0
total_points = 0
if days % 10 == 0:
    total_points -= 30
for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        total_spending += (ornament_price * quantity)
        total_points += ornament_points
    if day % 3 == 0:
        total_spending += ((tree_skirt_price + tree_garland_price) * quantity)
        total_points += tree_skirt_points + tree_garland_points
    if day % 5 == 0:
        total_spending += (tree_lights_price * quantity)
        total_points += tree_lights_points
        if day % 3 == 0:
            total_points += 30
    if day % 10 == 0:
        total_points -= 20
        total_spending += tree_skirt_price + tree_garland_price + tree_lights_price

print(f"Total cost: {total_spending}")
print(f"Total spirit: {total_points}")
