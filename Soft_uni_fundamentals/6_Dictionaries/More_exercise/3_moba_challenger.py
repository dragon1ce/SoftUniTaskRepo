def by_arrow(gamer, place, points: int, players: dict) -> dict:
    if gamer not in players.keys():
        players[gamer] = {}
        players[gamer][place] = points
    elif gamer in players.keys():
        if place not in players[gamer]:
            players[gamer][place] = points
        elif place not in players[gamer] and players[gamer][place] < points:
            players[gamer][place] = points
    return players


def by_vs(player_one, player_two, players: dict) -> dict:
    p1_total = 0
    p2_total = 0
    p1 = []
    p2 = []
    if player_one in players.keys() and player_two in players.keys():
        for place, points in players[player_one].items():
            p1_total += points
            p1.append(place)
        for place, points in players[player_two].items():
            p2_total += points
            p2.append(place)
        if any(x in p2 for x in p1):
            if p1_total > p2_total:
                del players[player_two]
            elif p2_total > p1_total:
                del players[player_one]
    return players


player_position = {}
player_total_points = {}
while True:
    command = input()
    if command == "Season end":
        break
    elif " -> " in command:
        player, position, skill = command.split(" -> ")
        skill = int(skill)
        player_position = by_arrow(player, position, skill, player_position)
    else:
        player1, player2 = command.split(" vs ")
        player_position = by_vs(player1, player2, player_position)

for name, pos_point in player_position.items():
    player_total_points[name] = 0
    for pts in pos_point.values():
        player_total_points[name] += pts
ordered_players_by_points = dict(sorted(player_total_points.items(), key=lambda x: -x[1]))
ordered_players_position = {}
for key, value in player_position.items():
    ordered_points = dict(sorted(value.items(), key=lambda x: (-x[1], x[0])))
    ordered_players_position[key] = ordered_points

for gamers, role_points in ordered_players_by_points.items():
    print(f"{gamers}: {role_points} skill")
    for role, pts in ordered_players_position[gamers].items():
        print(f"- {role} <::> {pts}")
