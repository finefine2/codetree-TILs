'''
누가 들어오면 이전의 모든 메세지를 읽게 된다.
총 m개의 메세지 중 p번째 메세지를 읽지 않았을 가능성이 있는 사람 출력
'''
N,M,P = map(int,input().split()) 
messages = [] 
for i in range(M): 
    c,u = input().split() 
    messages.append((c,int(u))) 

check = False
if messages[P-1][1] == 0: 
    check = True 
for i in range(N): 
    num = chr(ord("A") + i) 
    flag = False 
    for c,u in messages: 
        if u >= messages[P-1][1] and c == num: 
            flag = True 
    if not flag and not check: 
        print(num,end=" ")