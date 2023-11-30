# class Studnet: 
#     def __init__(self,kor=0,eng=0,math=0): 
#         self.kor = kor 
#         self.eng = eng 
#         self.math = math 
# st1 = Studnet(90,80,90) 
# print(st1.kor) 
# print(st1.eng) 
# print(st1.math) 

# st2 = Studnet() 
# print(st2.kor) 
# print(st2.eng) 
# print(st2.math) 

class info: 
    def __init__(self,ID="codetree",level=10):
        self.ID = ID 
        self.level = level

id1 = info()
print(f"user {id1.ID} lv {id1.level}")
a,b = input().split()
id2 = info(a,b) 
print(f"user {id2.ID} lv {id2.level}")