from typing import Dict


class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: Dict[str:int] = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name: str, mana_cost: int):
        if skill_name not in self.skills:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        else:
            return f"Skill already added"

    def player_info(self):
        print_line = [f"Name: {self.name}", f"Guild: {self.guild}", f"HP: {self.hp}", f"MP: {self.mp}"]
        for k, v in self.skills.items():
            print_line.append(f"==={k} - {v}")
        return "\n".join(print_line)
