s = input()
l1 = []

for i in s:
    if i == ' ':
        pass
    else:
        l1.append(i)

l2 = l1[:]
l2.reverse()

s1 = ''
s2 = ''

for j, k in zip(l1, l2):
    s1 += j
    s2 += k

if s1 == s2:
    print('Yes')
else:
    print('No')