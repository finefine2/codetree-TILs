N = int(input()) 

class Student: 
    def __init__(self,height,weight,number):
        self.height = height
        self.weight = weight
        self.number = number
student = []
for i in range(1,N+1): 
    h,w = map(int,input().split())
    student.append(Student(h,w,i))
student.sort(key=lambda x:(x.height,-x.weight))

for st in student: 
    print(st.height, st.weight, st.number)