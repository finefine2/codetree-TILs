class User:
    def __init__(self, codename, score):
        self.code = codename
        self.score = score
    
user = []
for _ in range(5):
    code, score = tuple(map(str, input().split()))
    user.append(User(code, score))

Min = 101
Mincode = ""
for i in range(5):
    if Min > int(user[i].score):
        Min = int(user[i].score)
        Mincode = user[i].code

print(Mincode, Min)