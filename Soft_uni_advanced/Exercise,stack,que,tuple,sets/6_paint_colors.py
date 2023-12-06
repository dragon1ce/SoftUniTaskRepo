from collections import deque

my_string = deque(input().split())
colors_found = []
main_colors = ["red", "blue", "yellow"]
secondary_colors = {"orange": ["yellow", "red"],
                    "purple": ["red", "blue"],
                    "green": ["yellow", "blue"],
                    }
while my_string:
    left = my_string.popleft()
    right = my_string.pop() if my_string else ""
    word = left + right
    word_reversed = right + left

    if word in main_colors or word in secondary_colors:
        colors_found.append(word)
    elif word_reversed in main_colors or word_reversed in secondary_colors:
        colors_found.append(word_reversed)
    else:
        if len(left) > 1:
            my_string.insert(len(my_string) // 2, left[:-1])
        if len(right) > 1:
            my_string.insert(len(my_string) // 2, right[:-1])

for color in colors_found:
    if color in secondary_colors:
        for c in secondary_colors[color]:
            if c not in colors_found:
                colors_found.remove(color)
                break
print(colors_found)