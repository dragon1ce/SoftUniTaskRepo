n = int(input())
a=[]
for i in str(n):
    a.append(i)
a.sort(reverse=True)
num=""
for i in a:
    num+=i
print(int(num))