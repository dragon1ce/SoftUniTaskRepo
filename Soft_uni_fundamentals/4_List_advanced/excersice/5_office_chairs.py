rooms = int(input())
free_chairs = 0
enough = True
for i in range(1, rooms + 1):
    inp = input().split()
    chairs = len(inp[0])
    visitors = int(inp[1])
    if chairs < visitors:
        print(f"{visitors - chairs} more chairs needed in room {i}")
        enough = False
    else:
        free_chairs += (chairs - visitors)
if enough:
    print(f"Game On, {free_chairs} free chairs left")
