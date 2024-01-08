class Product:
    def __init__(self, name, code, area):
        self.name = name
        self.code = code
        self.area = area

n = int(input())

pro = []
for _ in range(n):
    name, code, area = tuple(map(str, input().split()))
    pro.append(Product(name, code, area))

Max = ""
Maxcode = ""
Maxarea = ""
for i in range(n):
    if pro[i].name > Max:
        Max = pro[i].name
        Maxcode = pro[i].code
        Maxarea = pro[i].area

print(f"name {Max}")
print(f"addr {Maxcode}")
print(f"city {Maxarea}")