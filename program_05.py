#Sum of all Digits of a Number

N = int(input())
sum = 0
while(N>0):
    sum += N % 10
    N = N // 10

print(sum)