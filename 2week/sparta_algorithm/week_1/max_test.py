# Q. 다음과 같이 숫자로 이루어진 배열이 있을 때, 이 배열 내에서 가장 큰 수를 반환하시오.

input = [3, 5, 6, 1, 2, 4]

# 방법 2)
def find_max_num(array):
  max_num = array[0]

  for num in array:
    if num > max_num:
      max_num = num

  return max_num

result = find_max_num(input)
print(result)

# 가장 큰 수 반환 하기 위해 => 비교군 필요 => 비교변수 생성
# 비교 변수 생성 방법 2가지
  # 방법 1) 이중 for문을 통한 변수 생성 후 비교연산 if를 통해 큰 값 반환
  # 방법 2) 배열 내 첫번째 값을 지정변수로 지정 => max_num = array[0]
    # 비교연산 if를 통해 변수와 지정변수의 크기를 비교하여 큰 값에 치환한다.
    # 이 때 max_num과 num의 위치도 중요하다. max_num = num 순이여야하지 num = max_num 순이면 안됨.
    # 대입연산자의 경우, 대입연산자의 오른쪽 수를 왼쪽수로 대입하기 때문

# 방법 1)

# def find_max_num(array):
#   for num in array:
#     for compare_num in array:
#       if num < compare_num:
#         break
#     else:
#       return num

# result = find_max_num(input)
# print(result)

# 배열 내 가장 큰 구하기 => 각 숫자들을 비교해야 한다 => 비교군 필요
# 비교군을 형성을 위해서는 변수가 필요하다. 변수를 생성하는데는 두 가지 방법이 있다.
  # 방법 1) 이중 포문을 통한 변수형성
  # 방법 2) 배열 내 첫번쨰 값을 통한 지정변수 설정
# 방법을 선택하였다면, 두 개의 변수끼리 비교연산 if를 통하여 큰 값을 가려낸다.
  # 방법 1의 경우) 작은 값이면 break, 큰 값이면 return을 해준다.
  # 방법 2의 경우) 큰 값이면, 큰값으로 치환해 준다.





