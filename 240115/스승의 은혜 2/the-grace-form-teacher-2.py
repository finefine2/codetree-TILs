n,b = map(int,input().split())

prices = [
    int(input())
    for _ in range(n)
]

prices = sorted(prices) #오름차순으로 정렬해서 가격이 적은 것부터..!

cnt = 0
chance = 0

for price in prices:
    if b < price:
        if chance:
            if price//2 <= b:
                b -= price//2
                cnt+=1
        else:
            break #다음 가격보다 작으면 종료
    else:
        b -= price
        cnt+=1

print(cnt+1)