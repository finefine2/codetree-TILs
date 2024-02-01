'''
속도가 감소하기 시작하는 위치를 잘 설정하여 해당 위치를 전후로 속도가 바뀌게끔하는 전략을 통해 해결
'''
import sys
X = int(input()) 

v = 1 
time, dist = 0,0     
Min = sys.maxsize
while True: 
    dist += v 
    time += 1 

    if dist == X: 
        break 
    if dist <= X - (v+1) * (v+2) / 2: 
        v +=  1
    elif dist <= X - (v+1) * v / 2: 
        continue
    else: 
        v -= 1 
print(time)