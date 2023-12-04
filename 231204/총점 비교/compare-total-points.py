# from functools import cmp_to_key 
# class Student:
#     def __init__(self, kor, eng, math):
#         self.kor = kor
#         self.eng = eng
#         self.math = math
# students = [
#     Student(90, 80, 90), # 첫 번째 학생
#     Student(20, 80, 80), # 두 번째 학생
#     Student(90, 30, 60), # 세 번째 학생
#     Student(60, 10, 50), # 네 번째 학생
#     Student(80, 20, 10), # 다섯 번째 학생 
# ]

# # custom comparator 
# def compare(x,y): 
#     if x.kor % 30 == 0 and y.kor % 30 != 0: 
#         return -1 
#     if x.kor % 30 != 0 and y.kor % 30 == 0: 
#         return 1 
#     return 0 

# students.sort(key=cmp_to_key(compare))

# for s in students: 
#     print(s.kor, s.eng, s.math)

class Student: 
    def __init__(self, name, a,b,c): 
        self.name = name
        self.a = a 
        self.b = b 
        self.c = c 

students = [] 

n = int(input())
for _ in range(n): 
    name,a,b,c = input().split()

    students.append(Student(name,int(a),int(b),int(c)))

students.sort(key = lambda x: x.a + x.b + x.c)

for s in students: 
    print(s.name, s.a, s.b, s.c)