from collections import deque

working_bees = deque([int(x) for x in input().split()])
nectar_que = deque([int(x) for x in input().split()])
symbols = deque([x for x in input().split()])
total_honey = 0
while working_bees and nectar_que:
    bee = working_bees.popleft()
    nectar = nectar_que.pop()
    if nectar >= bee:
        symbol = symbols.popleft()
        honey = 0
        if symbol == "+":
            honey = bee + nectar
        elif symbol == "-":
            honey = bee - nectar
        elif symbol == "*":
            honey = bee * nectar
        elif symbol == "/" and nectar != 0:
            honey = bee / nectar
        total_honey += abs(honey)
    elif nectar < bee:
        working_bees.appendleft(bee)

print(f"Total honey made: {total_honey}")
if working_bees:
    print(f"Bees left: {', '.join([str(x) for x in working_bees])}")
if nectar_que:
    print(f"Nectar left: {', '.join([str(x) for x in nectar_que])}")