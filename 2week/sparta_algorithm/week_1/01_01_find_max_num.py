# Q. 다음과 같이 숫자로 이루어진 배열이 있을 때, 이 배열 내에서 가장 큰 수를 반환하시오.

input = [3, 5, 6, 1, 2, 4]

def find_max_num(array): 
    for num in array: # array 의 길이만큼 아래 연산이 실행
      for compare_num in array: # array 의 길이만큼 아래 연산이 실행
        if num < compare_num: # 비교 연산 1번 실행
          break
      else:
        return num


result = find_max_num(input)
print(result)

# 시간 복잡도
# 1. array의 길이 X array의 길이 X 비교 연산 1번
# 만큼의 시간이 필요합니다. 여기서 array(입력값)의 길이는 보통 N이라고 표현합니다. 그러면 위의 시간을 다음과 같이 표현할 수 있습니다.
# N x N
# 그러면 우리는 이제 이 함수는 N의 2승 만큼의 시간이 걸렸겠구나! 라고 말할 수 있습니다.

# 방법 1) 다른 숫자와 비교하기
      # 1. 하나하나 꺼내서 비교해야하므로 반복문을 사용한다. => for문 사용
      # 2. array에 있는 각각의 변수를 num이라는 변수에 담아준다 => for num in array
      # 3. 바교할 변수들을 뽑기위해 반복문을 한 번 더 사용한다 => for문 사용
      # 4. num과 compare_num을 사용하는 이중반복분 구조
      # 5. 만일 6이라면 6과 다른 배열 안의 숫자들을 비교했을 떄 6보다 큰 수를 발견하지 못했다면 if의 break에 걸리지 않고 else로 num에 6을 리턴!