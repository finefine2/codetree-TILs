class bomb:
    def __init__(self, code, color, sec):
        self.code = code
        self.color = color
        self.sec = sec

code, color, sec = tuple(map(str, input().split()))
Bomb = bomb(code, color, sec)
print(f"code : {Bomb.code}")
print(f"color : {Bomb.color}")
print(f"second : {Bomb.sec}")