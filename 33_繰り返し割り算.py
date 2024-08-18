n, m, k = map(int, input().split())

for _ in range(k):
    n = n / m

print(f'{n: .4f}')