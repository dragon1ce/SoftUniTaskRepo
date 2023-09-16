from collections import deque
entry = input()
customer_list = deque()
while entry != "End":
    if entry == "Paid":
        while customer_list:
            print(customer_list.popleft())
    else:
        customer_list.append(entry)
    entry=input()
print(f"{len(customer_list)} people remaining.")