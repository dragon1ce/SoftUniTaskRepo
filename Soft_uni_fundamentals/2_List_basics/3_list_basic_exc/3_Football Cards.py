team_a = [i for i in range(1, 12)]
team_b = [i for i in range(1, 12)]
entry = input()
cards = entry.split()
is_broken = False
for card in cards:
    if "A" in card:
        number = card.split("-")[1]
        if int(number) in team_a:
            team_a.remove(int(number))
    elif "B" in card:
        number = card.split("-")[1]
        if int(number) in team_b:
            team_b.remove(int(number))
    if len(team_a) < 7 or len(team_b) < 7:
        is_broken = True
        break
print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if is_broken: print("Game was terminated")
