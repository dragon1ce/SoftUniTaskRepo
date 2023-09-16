from collections import deque
deq = deque(input().split())
n = int(input())-1
while len(deq) != 1:
    deq.rotate(-n)
    print(f"Removed {deq.popleft()}")
print(f"Last is {''.join(deq)}")
