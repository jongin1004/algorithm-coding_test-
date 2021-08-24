x, y, bound = map(int, input().split())
res = []

x_max = max(list(filter(lambda value: x ** value < bound, list(range(20)))))
y_max = max(list(filter(lambda value: y ** value < bound, list(range(20)))))

for i in range(x_max + 1):
    for j in range(y_max + 1):
        if (x ** i) + (y ** j) <= bound:
            res.append((x ** i) + (y ** j))

res= list(set(sorted(res)))
print(res)

