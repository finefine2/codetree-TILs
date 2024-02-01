A,B,x,y = map(int,input().split())
# A -> x -> y -> B 
case1 = abs(x-A) + abs(B-y) 

# A -> y -> x -> B 
case2 = abs(y-A) + abs(x-B)
print(min(case1,case2))