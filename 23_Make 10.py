a, b, c = map(int, input().split())

if a + b == 10 or b + c == 10 or c + a == 10:
    print('Yes')
else:
    print('No')