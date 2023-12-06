def team_lineup(*args):
    country_pnames = dict()
    for k, v in args:
        if v not in country_pnames:
            country_pnames[v] = []
        country_pnames[v].append(k)
    sorted_dict = dict(sorted(country_pnames.items(),key=lambda x: (-len(x[1]),x[0])))
    string_to_return = []
    for country, players in sorted_dict.items():
        string_to_return.append(f"{country}:")
        a = len(country)
        b = len(players)
        for player in players:
            string_to_return.append(f"  -{player}")
    return "\n".join(string_to_return)


print(team_lineup(
            ("Lionel Messi", "Argentina"),
            ("Neymar", "Brazil"),
            ("Cristiano Ronaldo", "Portugal"),
            ("Harry Kane", "England"),
            ("Kylian Mbappe", "France"),
            ("Raheem Sterling", "England")))
print("DASDASFASFASF")
#