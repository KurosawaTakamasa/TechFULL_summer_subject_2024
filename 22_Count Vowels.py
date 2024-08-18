n = int(input())
s = input()
b = ['a', 'i', 'u', 'e', 'o']

count = 0

for w in s:
    if w in b:
        count += 1

print(count)