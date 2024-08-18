n, m, mag = map(int, input().split())
e = mag * (m/(n+1))

if e > 1:
    print('YES')
else:
    print('NO')