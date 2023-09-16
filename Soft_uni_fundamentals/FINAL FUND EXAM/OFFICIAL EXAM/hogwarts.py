def abjuration(spell):
    spell = spell.upper()
    print(spell)
    return spell


def necromancy(spell):
    print(spell.lower())
    return spell.lower()


def illusion(spell, s_command):
    index = int(s_command[1])
    letter = s_command[2]
    if index in range(len(spell)):
        spell = spell[:index] + letter + spell[index + 1:]
        print("Done!")
    else:
        print("The spell was too weak.")
    return spell


def divination(spell, s_command):
    first_substring = s_command[1]
    second_substring = s_command[2]
    count = 0
    while first_substring in spell:
        spell = spell.replace(first_substring, second_substring)
        count += 1
    if count > 0:
        print(spell)
    return spell


def alteration(spell, s_command):
    substring = s_command[1]
    if substring in spell:
        spell = spell.replace(substring, "")
        print(spell)
    return spell


main_spell = input()

while True:
    command = input()
    if command == "Abracadabra":
        break
    command = command.split()
    spell_command = command[0]
    if spell_command == "Abjuration":
        main_spell = abjuration(main_spell)
    elif spell_command == "Necromancy":
        main_spell = necromancy(main_spell)
    elif spell_command == "Illusion":
        main_spell = illusion(main_spell, command)
    elif spell_command == "Divination":
        main_spell = divination(main_spell, command)
    elif spell_command == "Alteration":
        main_spell = alteration(main_spell, command)
    else:
        print("The spell did not work!")
