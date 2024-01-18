a, b, c = map(int, input().split())

Max = -1
for i in range(1000):
    for j in range(1000):
        if a * i + b * j <= c:
            Max = max(Max, a*i + b*j)

print(Max)