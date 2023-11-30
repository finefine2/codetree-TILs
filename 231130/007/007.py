class Student: 
    def __init__(self,kor,eng,math): 
        self.kor = kor 
        self.eng = eng 
        self.math = math 

class Secret: 
    def __init__(self,code,place,time): 
        self.code = code
        self.place = place
        self.time = time 

a,b,c = input().split()
secret1 = Secret(a,b,c) 

print(f"secret code : {secret1.code}")
print(f"meeting point : {secret1.place}")
print(f"time : {secret1.time}")