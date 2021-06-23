# Q.  다음과 같은 문자열을 입력받았을 때, 어떤 알파벳이 가장 많이 포함되어 있는지 반환하시오

input = "hello my name is sparta"

def find_alphabet_occurrence_array(string):
  alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
  
  max_occurrence = 0
  max_alphabet = alphabet_array[0]

  for alphabet in alphabet_array: 
    occurrence = 0

    for char in string:
      if char == alphabet:
        occurrence += 1
    if occurrence > max_occurrence:
      max_occurrence = occurrence
      max_alphabet = alphabet
  return max_alphabet

result = find_max_occurred_alphabet(input)
print(result)

# 1. 알파벳을 담은 전체 배열을 생성하여, 각각의 알파벳을 넣어준다. => alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# 2. 최고로 많이 나온 알파벳 변수 => max_occurrence = 0
# 3. 가장 많이 나온 횟수 변수 => max_alphabet = alphabet_array[0]
# 4. for 문을 통해 알파벳 문자열을 변수에 담는다. => for alphabet in alphabet_array: 
# 5. 초기값 설정 / 비교값 설정
    # occurrence = 0
# 6. 알파벳과 입력값을 비교해야 한다.