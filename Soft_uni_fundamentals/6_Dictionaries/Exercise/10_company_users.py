company_users = {}
while True:
    entry = input().split(" -> ")
    if entry[0] == "End":
        break
    company_name = entry[0]
    user_id = entry[1]
    if company_name not in company_users:
        company_users[company_name] = []
    if user_id not in company_users[company_name]:
        company_users[company_name].append(user_id)

for company, users in company_users.items():
    print(f"{company}")
    for i in range(len(users)):
        print(f"-- {users[i]}")
    