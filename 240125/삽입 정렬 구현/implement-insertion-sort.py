n = int(input())

arr = list(map(int, input().split()))

for i in range(n):
  k = i-1
  num = arr[i]
  # num으로 저장해놓고
  while k >= 0 and arr[k] > num:
    arr[k+1] = arr[k]
    k -= 1
    # num보다 작은 경우 앞으로 당겨주면서 앞의 값들을 뒤로 미룬다.
  arr[k+1] = num

for k in arr:
  print(k, end = " ")