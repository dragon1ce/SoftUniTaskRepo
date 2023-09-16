a = input().split()
dictionary = {}
for i in range(0,len(a),2):
    key = a[i]
    value = a[i+1]
    dictionary[key] = int(value)
b = input().split()
for item in b:
    if item in dictionary:
        print(f"We have {dictionary[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")