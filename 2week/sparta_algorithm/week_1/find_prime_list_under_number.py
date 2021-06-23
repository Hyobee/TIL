# Q. 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오. 
# 소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수이다.

# # 20이 입력된다면, 아래와 같이 반환해야 합니다!
# [2, 3, 5, 7, 11, 13, 17, 19]

input = 20


def find_prime_list_under_number(number):
    prime_list = []

    for n in range(2, number + 1):
        for i in prime_list:
            if n % i == 0 and i * i <= n:
                break
        else:
            prime_list.append(n)

    return prime_list


result = find_prime_list_under_number(input)
print(result)

    # number 이하의 소수를 찾아야 함.
        # 2~number까지 모든 숫자를 찾아야 함.
        # 1, 0은 소수가 아니기 때문에 고려대상이 아님.

        # number에 + 1을 한 이유는 range 함수가 자기 자신 전(number - 1)까지 카운트하는 속성을 가졌기때문이다. 
        # 우리가 원하는 것은 2~number 이기 때문에 number를 포함하기 위해서는 +1을 해줘야 함.
