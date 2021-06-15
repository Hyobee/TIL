# Q. 다음과 같이 숫자로 이루어진 배열이 있을 때, 이 배열 내에서 가장 큰 수를 반환하시오.

input = [3, 5, 6, 1, 2, 4]

def find_max_num(array): 
    max_num = array[0]
    for num in array:
      if num > max_num:
        max_num = num

    return max_num

result = find_max_num(input)
print(result)


# 방법 2) 지정변수 max_num을 지정하여 가장 큰 값을 기록!
      # 배열의 첫번째 값을 초기값으로 설정해 준다. 기준점을 단순히 첫번쨰로 잡은 것!
      # 반복문을 사용하여 값을 하나하나 꺼내 비교해 본다 => for문
      # 만일 num이 max_num보다 크면 max_num을 num으로 갈아 끼워준다.
      # 반복문이 끝났다면 비교 후 가장 큰 값이 max_num에 저장되었기 떄문에 max_num을 반환하면 된다.

# 결론 1) 차이첨 - 방법 1과 2의 차이는 비교군을 이중포문으을 통한 배열로 바교 VS 최대값을 담을 변수를 통해 비교를 한것인지에 대한 차이
# 결론 2) 공통점 - 비교군이 있어야 한다는 것! 비교군을 어떻게 측정을 할지는 선택? 무엇이 효울 적일까?
