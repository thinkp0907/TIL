# 숫자형

# print(5)
# print(-10)
# print(3.14)
# print(10000)
# print(5+3)
# print(5*3)
# print(3*(3+1))

# 문자형

# print('풍선')
# print("나비")
# print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
# print("ㅋ" * 9)

# boolean
# 참 과 거짓

# print(5>10)
# print(5<10)
# print(True)
# print(False)
# print(not True)
# print(not False)
# print(not 5 > 10)

# 변수
# 애완동물을 소개해주세요

# animal = "강아지"
# name = "연탄이"
# age = 4
# hobby = "산책"
# is_adult = age >= 3

# print("우리집" + animal + "의 이름은 " + name + "예요")
# print(name, "는 " , age , " 살이며,", hobby ,"을 아주 좋아해요")
# print(name + "는 어른일까요? " + str(is_adult) )


# station = "사당"
# print(station + "행 열차가 들어오고 있습니다. ")
# station = "신도림"
# print(station + "행 열차가 들어오고 있습니다. ")
# station = "인천공항"
# print(station + "행 열차가 들어오고 있습니다. ")


# 연산자
# print(1+1)
# print(3-2)
# print(5*3)
# print(6/3)

# print(2**3)
# print(5%3)
# print(10%3)
# print(5//3)
# print(10//3)

# print(10 > 3)
# print(4 >= 7)
# print(10 <= 3)
# print(5 <= 5)

# print(3 == 3)
# print(4 == 3)
# print(3+4 == 7)

# print(1 != 3) 
# print(not(1 != 3))

# print((3 > 0 ) and (3 < 5))
# print((3 > 0) & (3 < 5))

# print((3 > 0) or (3 > 5))
# print((3 > 0) | (3 > 5))

# print(5 > 4 > 3)
# print(5 > 4 > 7)


# 간단한 수식
# print(2 + 3 * 4)    # 14
# print((2 + 3) * 4)  # 20
# number = 2 + 3 * 4  # 14
# print(number)
# number = number + 2 # 16
# print(number)
# number += 2         # 18
# print(number)
# number *= 2         # 36
# print(number)
# number /= 2         # 18
# print(number)
# number -= 2         # 16
# print(number)       
# number %= 2         # 0
# print(number)


# 숫자처리 함수
# print(abs(-5))  # 5
# print(pow(4, 2)) # 4^2 = 4*4 = 16
# print(max(5, 12)) # 12
# print(min(5, 12)) # 5
# print(round(3.14)) # 3
# print(round(4.99)) # 5

# from math import *
# print(floor(4.99)) # 내림. 4
# print(ceil(3.14)) # 올림. 4
# print(sqrt(16)) # 제곱근. 4


# 랜덤 함수
from random import *

# print(random())  # 0.0 ~ 1.0 미만의 임의의 값 생성
# print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
# print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
# print(int(random() * 10))
# print(int(random() * 10))
# print(int(random() * 10 + 1)) # 1 ~ 10 이하의 임의의 값 생성
# print(int(random() * 45 + 1)) # 1 ~ 45 이하의 임의의 값 생성
# print(int(random() * 45 + 1)) # 1 ~ 45 이하의 임의의 값 생성
# print(int(random() * 45 + 1)) # 1 ~ 45 이하의 임의의 값 생성
# print(int(random() * 45 + 1)) # 1 ~ 45 이하의 임의의 값 생성
# print(int(random() * 45 + 1)) # 1 ~ 45 이하의 임의의 값 생성
# print(int(random() * 45 + 1)) # 1 ~ 45 이하의 임의의 값 생성


# print(randrange(1, 45)) # 1 ~ 45 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성

# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성

# offline_1 = randint(4, 28) # 4 ~ 28 이하의 임의의 값 생성

# print("오프라인 스터디 모임 날짜는 매월" + str(offline_1) +  "일로 선정되었습니다.")



# 문자열
# sentence = '나는 소년입니다'
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)
# sentence3 = """
# 나는 소년이고, 
# 파이썬은 쉬워요 
# """
# print(sentence3)


# 슬라이싱
# jumin = "920907-1155715"

# print("성별 : " + jumin[7])
# print("연 : " +jumin[0:2]) # 0 ~ 2 직전까지 (0, 1)
# print("월 : " + jumin[2:4])
# print("일 : " +jumin[4:6])

# print("생년월일 : " +jumin[:6])
# print("뒤 7자리 : " +jumin[7:])
# print("뒤 7자리 (뒤에서부터) " +jumin[-7:])
# 맨 뒤에서 7번째 부터  끝까지


# 문자열 처리 함수
# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python", "Java"))

# index = python.index("n")
# print(index)
# index = python.index("n", index + 1)
# print(index)
# print(python.find("n"))
# print(python.find("Java"))
# # print(python.index("Java"))

# print(python.count("n"))



# 문자열 포맷
# print("a" + "b")
# print("a" , "b")

# 방법 1
# print("나는 %d살입니다. " % 20)
# print("나는 %s을 좋아해요. " % "파이썬")
# print("Apple이라는 단어는 %c로 시작해요" %"A")

# %s
# print("나는 %s살입니다. " % 20)
# print("%s색과 %s색을 좋아해요" %("파란", "빨간"))


# 방법 2
# print("나는 {}살입니다. ".format(20))
# print("나는 {}색과 {}색을 좋아해요".format("파란", "빨간"))
# print("나는 {0}색과 {1}색을 좋아해요".format("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아해요".format("파란", "빨간"))


# 방법 3
# print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20, color  = "빨간"))
# print("나는 {age}살이며, {color}색을 좋아해요".format(color  = "빨간", age = 20))

# 방법 4 (python v3.6 이상)
# age = 20
# color = "빨간"

# print(f"나는 {age}살이며, {color}색을 좋아해요")


# 탈출 문자(escape)
# print("백문이 불여일견 \n백견이 불여일타")

# \" \' : 문장 내에서 따옴표
# 저는 "나도코딩" 입니다
# print("저는 '나도코딩' 입니다.")
# print('저는 "나도코딩" 입니다.')
# print("저는 \"나도코딩\" 입니다.")
# print("저는 \'나도코딩\' 입니다.")

# \\ : 문장 내에서 \
# print("C:\\Users\\Think\\TIL\\Python>")

# \r : 커서를 맨앞으로 이동
# print("Red Apple\rPine")

# \b : 백스페이스 (한 글자 삭제)
# print("Redd\bApple")

# \t : 탭
# print("Red\tApple")


# 예) http://www.naver.com
# site = "http://daum.net"
# sites = site[7:]
# print(sites)
# index = sites.index(".")
# sites = sites[:index]
# password = sites[:3] + str(len(sites)) + str(sites.count("e")) + "!"
# print(password)


# 리스트 [] : 순서를 가지는 객체의 집합

# 지하철 칸별로 10 , 20, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10, 20, 30]
# print(subway)

# subway = ['유재석' , '조세호' , '박명수']
# print(subway)
# print(subway.index("조세호"))
# subway.append("하하")
# print(subway)
# subway.insert(1, "정형돈")
# print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# # 같은 사람이 몇명인지 확인하기
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# 정렬도 가능
# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list)

# # 순서 뒤집기
# num_list.reverse()
# print(num_list)

# # 모두 지우기
# num_list.clear()
# print(num_list)

# 다양한 자료형 함께 사용
# num_list = [5,2,4,3,1]
# mix_list = ["조세호", 20, True]
# print(mix_list)

# # 리스트 확장
# num_list.extend(mix_list)
# print(num_list)


# 사전(Dictionary)
# cabinet = {3 : "유재석", 100 : "김태호"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# print(cabinet[5])
# print(cabinet.get(5))
# print(cabinet.get(5, "사용 가능"))

# print(3 in cabinet) # True
# print(5 in cabinet) # False

# cabinet = {"A-3" : "유재석", "B-100" : "김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# # 새 손님
# print(cabinet)
# cabinet["A-3"] = "김종국"
# cabinet["C-20"] = "조세호"
# print(cabinet)


# # 간 손님
# del cabinet["A-3"]
# print(cabinet)


# # key 들만 출력
# print(cabinet.keys())

# # value 들만 출력
# print(cabinet.values())

# # key, value 쌍으로 출력
# print(cabinet.items())

# # 목욕탕 폐점
# cabinet.clear()
# print(cabinet)


# 튜플(tuple)
# 내용 변경 x, 추가 x, 속도는 리스트보다 빠름

# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# menu.add("생선까스")

# name = "김종국"
# age = 20
# hobby  = "코딩"
# print(name, age, hobby)

# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name, age, hobby)


# 세트(set)
# 중복 x, 순서 x
# my_set = {1, 2, 3, 3, 3}
# print(my_set)

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

# # 교집합 (java 와 python 을 둘다 할 수 있는 개발자)
# print(java & python)
# print(java.intersection(python))

# # 합집합 (java 할 수 있거나 python 할 수 있는 개발자)
# print(java | python)
# print(java.union(python))

# # 차집합 (java 할 수 있지만 python 은 할 줄 모르는 개발자)
# print(java - python)
# print(java.difference(python))

# # python 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)

# # java를 까먹었어요
# java.remove("김태호")
# print(java)


# # 자료구조의 변경
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))



# Quiz
comment = list(range(1, 21))
shuffle(comment)
winners = sample(comment, 4)

print("-- 당첨자 발표 --")
print(" 치킨 당첨자 :  {0}".format(winners[0]))
print(" 커피 당첨자 :  {0}".format(winners[1:]))
print("-- 축하합니다 -- ")
 