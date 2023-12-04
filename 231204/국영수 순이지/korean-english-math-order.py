n = int(input()) 

class Score: 
    def __init__(self,name,kor,eng,math): 
        self.name = name
        self.kor = kor 
        self.eng = eng 
        self.math = math 

students = [] 
for _ in range(n): 
    n,k,e,m = input().split()
    students.append(Score(n,int(k),int(e),int(m)))

students.sort(key = lambda x: (-x.kor,-x.eng,-x.math))

for s in students: 
    print(s.name, s.kor, s.eng, s.math)