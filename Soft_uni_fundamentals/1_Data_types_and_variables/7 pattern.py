# n = int(input())
# for i in range(n+1):
#     print("*"*i)
# for i in range(n-1,0,-1):
#     print("*"*i)
#
j=0
n = int(input())
for i in range((n*2)):
    if i<n:
        print("*"*i)
        j+=1
    else:
        print("*"*j)
        j-=1