# class Student: 
#     def __init__(self,kor=0,eng=0,math=0): 
#         self.kor = kor 
#         self.eng = eng 
#         self.math = math 

# students = [] 
# for _ in range(5): 
#     kor,eng,math = map(int,input().split()) 
#     students.append(Student(kor,eng,math))
# student3 = students[2] 
# print(f"student3: {student3.kor}, {student3.eng}, {student3.math}")
people = []
for _ in range(5): 
    name, score = input().split() 
    people.append((name,int(score)))
people.sort(key = lambda x: x[1]) 
ans = people[0] 
print(ans[0], ans[1])