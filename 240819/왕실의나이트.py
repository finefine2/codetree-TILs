# 그래도 예전보다는 발전한듯? 
# 초기 알파벳으로 주어지는 걸 숫자로 변환하는 과정
strat_pos = input() 
alphas = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
r = int(start_pos[1]) - 1
c = alphas[start_pos[0]] - 1

movements = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)] 
cnt = 0 

def in_range(r,c): 
  return 0 <= r < 8 and 0 <= c < 8 

for m in movements: 
  if in_range(m[0]+r,m[1]+c): 
    cnt += 1 
print(cnt) 
