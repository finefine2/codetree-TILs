a, b, c = map(int, input().split())

if (a * 24 * 60 + b * 60 + c) >= (11 * 24 * 60 + 11 * 60 + 11):
    answer = (a * 24 * 60 + b * 60 + c) - (11 * 24 * 60 + 11 * 60 + 11)
else:
    answer = -1 
    
print(answer)