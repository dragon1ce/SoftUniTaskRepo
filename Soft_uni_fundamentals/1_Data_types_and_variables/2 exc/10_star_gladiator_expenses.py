lost_count = int(input())
helm_price_repair = float(input())
sword_price_repair = float(input())
shield_price_repair = float(input())
armor_price_repair = float(input())
shield_brake_counter = 0
total_repair_cost = 0

helm_break = 0
sword_break = 0
shield_break = 0
for lost in range(1, lost_count + 1):
    if lost % 2 == 0:
        helm_break += 1
        if lost % 3 == 0:
            shield_break += 1
            shield_brake_counter += 1
    if lost % 3 == 0:
        sword_break += 1
armor_break = shield_break // 2
total_repair_cost = (helm_price_repair * helm_break) + (sword_price_repair * sword_break) + (
        shield_price_repair * shield_break) + (armor_price_repair * armor_break)
print(f"Gladiator expenses: {total_repair_cost:.2f} aureus")
