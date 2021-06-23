# Q. 다음과 같이 0 혹은 양의 정수로만 이루어진 배열이 있을 때, 
# 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 
# 숫자 사이에 '✕' 혹은 '+' 연산자를 넣어 
# 결과적으로 가장 큰 수를 구하는 프로그램을 작성하시오. 
# 단, '+' 보다 '✕' 를 먼저 계산하는 일반적인 방식과는 달리, 모든 연산은 왼쪽에서 순서대로 이루어진다.

input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
  multiply_sum = 0 
  for number in array:
    if number <= 1 or multiply_sum <= 1:
      multiply_sum += number
    else:
      multiply_sum * number
  return multiply_sum

result = find_max_plus_or_multiply(input)
print(result)

  # 현재 계산한 합계를 저장하는 변수를 작성해준다. => multiply_sum = 0 
  # for문을 통해 변수에 배열을 담아 비교한다. => for number in array:
  # 1보다 같거나 작다면 더하는 것이 낫고
  # 1보다 클경우 곱하는 것이 낫다.
  # if number <= 1:
  # 현재 합계를 저장한 변수도 0 이기 떄문에 같은 맥락으로 조건문에 넣어준다.