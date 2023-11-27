# arr 는 _list 와 상관 없음 
# def modify(arr): 
#     arr[0] = 10 
# _list = [1,2,3,4] 
# modify(_list[:]) 
# # 리스트와 동일한 원소를 갖는 새 리스트를 만들어 값을 전달함 
# for elem in _list: 
#     print(elem, end=" ")

n = int(input()) 
list_ = list(map(int,input().split())) 

for num in list_: 
    if num % 2 == 0: 
        num /= 2 
    print(int(num),end=" ")