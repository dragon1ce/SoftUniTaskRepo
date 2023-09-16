num_snowballs = int(input())
winning_ball = 0
win_snowball_weight = 0
win_snowball_time = 0
win_snowball_quality = 0
snowball_weight = 0
snowball_time = 0
snowball_quality = 0
for ball in range(1, num_snowballs + 1):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    calc = (snowball_weight / snowball_time) ** snowball_quality
    if calc > winning_ball:
        win_snowball_weight = snowball_weight
        win_snowball_time = snowball_time
        win_snowball_quality = snowball_quality
        winning_ball = int(calc)
print(f"{win_snowball_weight} : {win_snowball_time} = {winning_ball} ({win_snowball_quality})")
