n = int(input())
y = 5*10**15

if y % n == 0:
    print(y//n)
else:
    print(y//n + 1)
