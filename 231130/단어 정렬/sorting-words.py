N = int(input()) 
words = [] 
for _ in range(N): 
    words.append(input()) 

words.sort() 
for w in words: 
    print(w)