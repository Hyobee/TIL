# Q.  다음과 같은 문자열을 입력받았을 때, 어떤 알파벳이 가장 많이 포함되어 있는지 반환하시오

# 주어진 문지열 
# "hello my name is sparta"

  # 어떤 알파벳 => 알파벳의 개수만큼 배열을 생성
  # 가장 많은빈도수 => index값을 구한다. => 초기값을 0으로 시작하여 문자열을 돌려서 나올 떄마다 1씩 추가

def find_alphabet_occurrence_array(string):
  alphabet_occurrence_array = [0] * 26

  for in char string:
    if not char.isalpha():
      continue
    alpha_index = ord(char) - ord(a);
    alphabet_occurrence_array[alpha_index] += 1
  return alphabet_occurrence_array
print(find_alphabet_occurrence_array())


  # 1. 함수를 생성하는데 입력값을 받을 수 있는 파라미터와 함께 생성해준다. => def find_alphabet_occurrence_array(string):
  # 2. 알파벳의 개수 만큼의 초기값이 0 26개인 배열을 생성한다. => alphabet_occurrence_array = [0] * 26
  # 3. for문을 통해 문자열을 변수에 저장한다. => for in char array:
  # 4. if조건문을 통해 입력값이 알파벳인지 확인한다. => if not char.isalpha()
  # 5. 인덱스를 알아낸다 => alpha_index = ord(char) - ord(a);
  # 6. 각 배열의 빈도수를 알아내어 더해준다 => alphabet_occurrence_array[alpha_index] += 1
  # 7. 결과값을 되돌려준다. => return(alphabet_occurrence_array)

# Tip
  # 1) 문자열인지 확인하는 방법 => 배열 내 공백 즉 스페이스 바 띄어쓰기를 제외하기 위함.
    # 1-1. 문자열이 알파벳인지 확인하는 방법 => 파이썬 내장함수 str.isalpha()
      # 1print("a".isalpha())    # True
      # 1print("1".isalpha())    # False
      # s = "abcdefg"
      # print(s[0].isalpha())   # True
  # 2) 알파벳 별로 빈도수를 리스트에 저장하기
    # 내장 함수 ord() 이용해서 아스키 값 받기
      # 2-1. 우선 알파벳 별 빈도수를 저장하기 위한 길이가 26인 0으로 초기화된 배열을 만듭니다. => alphabet_occurrence_array = [0] * 26
      # 2-2. 이 배열의 각 원소에 알파벳마다 빈도수를 추가 
        # => a일 때는 0번째 원소에 1을 추가하고, b일 때는 1번째 원소에 1을 추가 
        # => 아스키 (ASCII) 코드 이용 (python char to ascii code)
          # 구분 | 아스키 (ASCII) | index
          # a   | 97           | 97-97 -> 0
          # b   | 98           | 98-97 -> 1
          # c   | 99           | 99-97 -> 2
          
          # print(ord('a'))               # 97
          # print(ord('a') - ord('a'))    # 97-97 -> 0
          # print(ord('b') - ord('a'))    # 98-97 -> 1
    
