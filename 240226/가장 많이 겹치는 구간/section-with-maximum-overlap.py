n = int(input())

check = [0] * 200001

arr = []
for i in range(n):
    a, b = map(int, input().split())

    check[a] += 1
    check[b] -= 1

s = [0] * 200001

for i in range(200000):
    s[i+1] = s[i] + check[i]
    
print(max(s))

# for i in range(100001):

# print(max(check))