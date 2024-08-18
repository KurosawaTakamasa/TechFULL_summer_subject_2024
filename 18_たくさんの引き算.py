n, m, k = map(int, input().split())

while True:
    if n - k < m:
        break
    else:
        n -= k
        
print(n)