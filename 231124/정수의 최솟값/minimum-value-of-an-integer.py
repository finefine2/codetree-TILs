'''
def add(*args):
    return sum(args)


>> add(1, 3, 2, 6, 5, 4)

21
'''

a,b,c = map(int,input().split())

def mini(n1,n2,n3): 
    return min(n1,n2,n3) 

print(mini(a,b,c))