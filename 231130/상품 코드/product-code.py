class Product: 
    def __init__(self,name="codetree",code="50"): 
        self.name = name 
        self.code = code 
P1 = Product() 
a,b = input().split() 
P2 = Product(a,b)
print(f"product {P1.code} is {P1.name}")
print(f"product {P2.code} is {P2.name}")