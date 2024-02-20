# .은 단일 문자와 일치
# a*은 0개 이상의 a와 일치
# .*로 하면 단일 문자들이 가능하다.

# 솔직히 잘 몰라서 다른 사람 풀이를 참고하였다.

s = input()
p = input()

ss = len(s)
pp = len(p)

s = " " + s
p = " " + p

check = [[0] * 21 for _ in range(21)]
check[0][0] = 1

for j in range(pp):
    for i in range(ss):
        if not check[i][j]:
            continue
        
        if j != pp - 1 and p[j+2] == '*':
            check[i][j+2] = 1

            for k in range(i+1, ss + 1):
                if p[j+1] != '.' and s[k] != p[j+1]:
                    break
                check[k][j+2] = 1

        elif p[j+1] == '.':
            check[i+1][j+1] = 1
        else:
            if s[i+1] == p[j+1]:
                check[i+1][j+1] = 1


if check[ss][pp]:
    print("true")
else:
    print("false")