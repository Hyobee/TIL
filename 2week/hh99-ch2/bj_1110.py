l = input().split()
n = int(l[0])

start_num = n
count = 0
while True:
    count +=1
    n1 = int(n % 10)
    n10 = int(n / 10)
    m = int(n1 + n10)
    k = int(n1 * 10 + m % 10)
    
    if k == start_num:
        break
    n = k
print(count)


# 26
# 2+6 = 8
# 68
# 6+8 = 14
# 84
# 8+4 = 12
# 42
# 4+2 = 6
# 26

#  2   6   =>   2+6   =>  8
# n10  n1  =>  n10+n1 =>  m
# 68
# n1x10 + m

# n1이 10의 자리 수가 되기 위해 곱하기 10을 해준다
# 그 후에 m을 더해준다.
# k는 다음 수 이다.