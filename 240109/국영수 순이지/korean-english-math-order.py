class User:
    def __init__(self, name, kor, eng, mat):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat

n = int(input())

user = []
for _ in range(n):
    name, kor, eng, mat = tuple(map(str, input().split()))
    user.append(User(name, kor, eng, mat))

user.sort(key=lambda x: (-int(x.kor), -int(x.eng), -int(x.mat)))

for i in range(n):
    print(f"{user[i].name} {user[i].kor} {user[i].eng} {user[i].mat}")