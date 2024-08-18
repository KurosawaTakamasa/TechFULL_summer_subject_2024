n = int(input())

mi, ma = map(int, input().split())
count = ma - mi + 1

for i in range(mi, ma + 1):
    i = str(i)
    n_str = str(n)
    if len(n_str) > len(i):
        continue
        
    match_found = False
    
    for j in range(len(i) - len(n_str) + 1):
        if i[j:j+len(n_str)] == n_str:
            match_found = True
            break

    if match_found:
        count -= 1

print(count)
