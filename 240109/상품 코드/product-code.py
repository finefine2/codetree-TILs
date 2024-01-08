class Product:
    def __init__(self, name, code):
        self.name = name
        self.code = code


first = Product(name = "codetree", code = "50")
# first.name = "codetree"
# first.code = "50"

name, code = tuple(map(str, input().split()))
pro = Product(name, code)

print(f"product {first.code} is {first.name}")
print(f"product {pro.code} is {pro.name}")