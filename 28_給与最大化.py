p1, p2 = map(int, input().split())
h1, h2 = map(int, input().split())
a = int(input())

salary = 0

if a == 0:
    pass
elif a <= h1 + h2:
    if p1 < p2:
        if a < h2:
            salary = p2*a
        else:
            salary = p2*h2 + p1*(a-h2)
    else:
        if a < h1:
            salary = p1*a
        else:
            salary = p1*h1 + h2*(a-h1)
else:
        salary = p1*h1 + p2*h2

print(salary)
