class Student:
    def __init__(self, code, place, time):
        self.code = code
        self.place = place
        self.time = time
    
a, b, c = tuple(input().split())
s = Student(a, b, c)

print(f"secret code : {s.code}")
print(f"meeting point : {s.place}")
print(f"time : {s.time}")