s = input()
s_l = []

for w in s:
    s_l.append(w)

if '+' in s_l:
    a = s_l.index('+') 
    b = len(s_l) - (a+1)
    print(a+b)
else:
    a = s_l.index('-')
    b = len(s_l) - (a+1)
    print(a-b)