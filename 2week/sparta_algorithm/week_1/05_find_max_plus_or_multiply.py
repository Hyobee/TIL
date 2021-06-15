# Q. 다음과 같이 0 혹은 양의 정수로만 이루어진 배열이 있을 때, 
# 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 
# 숫자 사이에 '✕' 혹은 '+' 연산자를 넣어 결과적으로 
# 가장 큰 수를 구하는 프로그램을 작성하시오. 
# 단, '+' 보다 '✕' 를 먼저 계산하는 일반적인 방식과는 달리, 모든 연산은 왼쪽에서 순서대로 이루어진다.

input = [0, 3, 5, 6, 1, 2, 4]

# 숫자에 따라 곱하기 보다 더하는것의 결과값이 큰게 있다 0과 1이 그러한 경우이다.
# 그래서 변수로 들어오는 숫자(input = [0, 3, 5, 6, 1, 2, 4])가 1과 같거나 1보다 작을 떄를 조건문에 추가 => if number <= 1
# 결과값 또한 1보다 같거나 1보다 작을 수 있기 떄문에 결과값 또한 고려해야 하므로 조건문에 추가한다. => if number <= 1

def find_max_plus_or_multiply(array):
    multiply_sum = 0
    for number in array:
      if number <= 1 or c:
        multiply_sum + number
      else:
        multiply_sum *= number

    return 1


result = find_max_plus_or_multiply(input)
print(result)