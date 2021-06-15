def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    # 1. for문을 이용해 문자열을 모은다. => for char in string:
    # char에는 각각의 문자열이 담겨있다.
      # 1-1. 문자열이 알파벳인지 확인하는 방법 => 파이썬 내장함수 str.isalpha()
        # 1print("a".isalpha())    # True
        # 1print("1".isalpha())    # False
        # s = "abcdefg"
        # print(s[0].isalpha())   # True
    # 2. 알파벳안지 확인하여 알파벳인 경우에만 실행되도록 한다. => if not char.isalpha():
    # 3. 내장 함수 ord() 이용해서 아스키 값 받기
      # 3-1. 우선 알파벳 별 빈도수를 저장하기 위한 길이가 26인 0으로 초기화된 배열을 만듭니다. => alphabet_occurrence_array = [0] * 26
      # 3-2. 이 배열의 각 원소에 알파벳마다 빈도수를 추가 
        # => a일 때는 0번째 원소에 1을 추가하고, b일 때는 1번째 원소에 1을 추가 
        # => 아스키 (ASCII) 코드 이용 (python char to ascii code)
          # 구분 | 아스키 (ASCII) | index
          # a   | 97           | 97-97 -> 0
          # b   | 98           | 98-97 -> 1
          # c   | 99           | 99-97 -> 2
          
          # print(ord('a'))               # 97
          # print(ord('a') - ord('a'))    # 97-97 -> 0
          # print(ord('b') - ord('a'))    # 98-97 -> 1
    # 4. 초기값을 알파벳의 첫 시작인 a로 잡고 빼준다.
    # 5. 알파벳이 아니라면 다음 문자열 검사를 계속한다 => if not char.isalpha(): continue
    # 6. 알파벳이라면 이것을 실행한다 => 내장함수 ord 이용해 아스키 값 구하기. => ord
    # 7. 배열의 각 원소에 1 추가 => ord(char) - ord("a");

    for char in string:
      if not char.isalpha():
        continue
      arr_index = ord(char) - ord("a")
      alphabet_occurrence_array[arr_index] += 1


    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))
