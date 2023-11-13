chars = []
a = input() 
b = input() 
c = input() 

chars.append(a) 
chars.append(b)
chars.append(c) 

chars.sort(key = lambda x:len(x))

print(abs(len(chars[0])- len(chars[-1])))