n = map(int,input().split())
n = list(n) 

if min(n) == n[0]:
    print(n[1] + n[2])
elif min(n) == n[1]:
    print(n[0] +n[2])
else:
    print(n[0] + n[1])