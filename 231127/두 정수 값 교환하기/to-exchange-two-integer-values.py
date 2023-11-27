def swap(a,b): 
    a,b = b,a 
    return a,b

n,m = map(int,input().split()) 
ans1,ans2 = swap(n,m) 
print(ans1, ans2)