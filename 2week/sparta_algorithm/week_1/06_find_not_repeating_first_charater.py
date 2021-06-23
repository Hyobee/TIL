input = "abacabade"

def find_not_repeating_first_character(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1

    not_repeating_character_array = []
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]

        if alphabet_occurrence == 1:
            not_repeating_character_array.append(chr(index + ord("a")))
            
    for char in string:
        if char in not_repeating_character_array:
            return char
result = find_not_repeating_first_character(input)
print(result)



# 빈도수가 1개 이상 나오는 값들을 변수(not_repeating_character_array)에 담는다. => not_repeating_character_array = []
# 알파벳의 길이만큼 반복을 해준다. => for index in range(len(alphabet_occurrence_array))
# 알파벳 배열에서 index의 값을 빼서 변수(alphabet_occurrence)에 저장한다. => alphabet_occurrence = alphabet_occurrence_array[index]
# 이렇게 함으로서 a~z의 빈도까지 저장가능!
# 이 빈도수가 만약 1일 때 => if alphabet_occurrence == 1:
# 변수(not_repeating_character_array)에 해당 알파벳을 넣어준다. => not_repeating_character_array.append(chr(index+ ord("a")))
  # 아스키 코드를 인덱스에 더해 입력값의 인덱스를 알아낸뒤 숫자이기 떄문에 문자열로 변환하기 위해 chr로 감싸 숫자를 알파벳으로 변환해 준다.
