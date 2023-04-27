# 영어 단어와 그에 해당하는 한글 뜻을 저장하는 딕셔너리 dictionary를 생성하고, 
# 영어 단어를 입력받아 해당하는 한글 뜻을 출력하는 프로그램을 작성하시오.

# 입력한 영어 단어가 딕셔너리에 없는 경우에는 ‘사전에 단어가 없습니다’라고 출력하시오.
# 딕셔너리의 내용은 자유롭게 하되 3개 이상의 단어로 구성하시오

# TODO 딕셔너리 생성
dictionary = { "apple":"사과","banana":"바나나","cherry":"체리" }

word = input("영어 단어를 입력하세요: ")

# TODO 사전에 단어가 있는지 검사하고, 있는 경우 한글  뜻을 출력하는 문장 완성
if word in dictionary:
    meaning = dictionary[word]
    print(f"{word}의 의미는 {meaning}입니다")
else:
    print(f"사전에 {word}가 없습니다")