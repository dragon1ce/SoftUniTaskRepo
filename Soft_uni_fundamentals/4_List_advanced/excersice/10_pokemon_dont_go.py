pokemon_list = list(map(int, input().split()))
total = 0
while len(pokemon_list) > 0:
    val = 1
    input_int = int(input())
    if 0 <= input_int <= len(pokemon_list) - 1:
        val = pokemon_list.pop(input_int)
    elif input_int < 0:
        val = pokemon_list.pop(0)
        pokemon_list.insert(0,pokemon_list[-1])
    elif input_int >= len(pokemon_list):
        val = pokemon_list.pop(-1)
        pokemon_list.append(pokemon_list[0])
    pokemon_list = [x + val if x <= val else x - val for x in pokemon_list]
    total += val
print(total)