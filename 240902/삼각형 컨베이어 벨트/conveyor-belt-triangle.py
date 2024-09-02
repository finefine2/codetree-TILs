N,T = tuple(map(int,input().split()))

first = list(map(int,input().split()))
second = list(map(int,input().split()))
third = list(map(int,input().split()))

for _ in range(T):

    temp1 = first[N-1]
    for i in range(N-1,0,-1):
        first[i] = first[i-1]
    first[0] = third[N-1]

    temp2 = second[-1]
    for i in range(N-1,0,-1):
        second[i] = second[i-1]
    second[0] = temp1

    for i in range(N-1,0,-1):
        third[i] = third[i-1]
    third[0] = temp2

for f in first:
    print(f,end=" ")
print()
for s in second:
    print(s,end=" ")
print()
for t in third:
    print(t,end=" ")