# class Student: 
#     def __init__(self,kor,eng,math,number): 
#         self.kor = kor 
#         self.eng = eng 
#         self.math = math 
#         self.number = number

# students = [
#     Student(90, 80, 90, 1), # 첫 번째 학생
#     Student(20, 80, 80, 2), # 두 번째 학생
#     Student(90, 30, 60, 3), # 세 번째 학생
#     Student(60, 10, 50, 4), # 네 번째 학생
#     Student(80, 20, 10, 5), # 다섯 번째 학생 
# ]

# students.sort(key=lambda x: -x.kor) 

# for idx,st in enumerate(students,start=1): 
#     print(f"{idx}등: {st.number}번")

# num_to_rank = [0] * (len(students)+1) 
# nums = [1,3,5,4,2] 

# for rank, num in enumerate(nums,start =1): 
#     num_to_rank[num] = rank 
# print(num_to_rank)

N = int(input()) 

class Student: 
    def __init__(self, height,weight,number):
        self.height = height
        self.weight = weight
        self.number = number
students = []
for i in range(1,N+1): 
    h,w = map(int,input().split())
    students.append(Student(h,w,i)) 

students.sort(key = lambda x: (-x.height, -x.weight, x.number))

for s in students: 
    print(s.height, s.weight, s.number)