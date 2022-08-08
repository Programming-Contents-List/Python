# 116
# 사용자로부터 입력 받은 시간이 정각인지 판별하라.

# >> 현재시간:02:00
# 정각 입니다.
# >> 현재시간:03:10
# 정각이 아닙니다
# 정답확인


# 117
# 사용자로 입력받은 단어가 아래 fruit 리스트에 포함되어 있는지를 확인하라. 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.

# fruit = ["사과", "포도", "홍시"]
# >> 좋아하는 과일은? 사과
# 정답입니다.
# 정답확인


# 119
# 아래와 같이 fruit 딕셔너리가 정의되어 있다. 사용자가 입력한 값이 딕셔너리 키 (key) 값에 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.

# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# >> 제가좋아하는계절은: 봄
# 정답입니다.
# 정답확인


# 121
# 사용자로부터 문자 한 개를 입력 받고, 소문자일 경우 대문자로, 대문자 일 경우, 소문자로 변경해서 출력하라.
# >> a
# A
# 힌트-1 : islower() 함수는 문자의 소문자 여부를 판별합니다. 만약 소문자일 경우 True, 대문자일 경우 False를 반환합니다. 힌트-2 : upper() 함수는 대문자로, lower() 함수는 소문자로 변경합니다.
# 정답확인

# 123
# 사용자로부터 달러, 엔, 유로, 또는 위안 금액을 입력받은 후 이를 원으로 변환하는 프로그램을 작성하라. 각 통화별 환율은 다음과 같다. 사용자는 100 달러, 1000 엔, 13 유로, 100 위안과 같이 금액과 통화명 사이에 공백을 넣어 입력한다고 가정한다.

# 통화명	환율
# 달러	1167
# 엔	1.096
# 유로	1268
# 위안	171
# >> 입력: 100 달러
# 116700.00 원
# 정답확인

# 124
# 사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하라.
# >> input number1: 10
# >> input number2: 9
# >> input number3: 20
# 20
# 정답확인


# 125
# 휴대폰 번호 앞자리에 따라 통신사는 아래와 같이 구분된다. 사용자로부터 휴대전화 번호를 입력 받고, 통신사를 출력하는 프로그램을 작성하라.
# 번호	통신사
# 011	SKT
# 016	KT
# 019	LGU
# 010	알수없음
# >> 휴대전화 번호 입력: 011-345-1922
# 당신은 SKT 사용자입니다.
# 정답확인


# 126
# 우편번호는 5자리로 구성되는데, 앞의 세자리는 구를 나타낸다. 예를들어, 강북구의 경우 010, 011, 012 세 자리로 시작한다.

# -	0	1	2	3	4	5	6	7	8	9
# 01	강북구	강북구	강북구	도봉구	도봉구	도봉구	노원구	노원구	노원구	노원구
# 사용자로 부터 5자리 우편번호를 입력받고 구를 판별하라

# >> 우편번호: 01400
# 도봉구
# 정답확인

# 128
# 주민등록번호의 뒷 자리 7자리 중 두번째와 세번째는 지역코드를 의미한다. 주민 등록 번호를 입력 받은 후 출생지가 서울인지 아닌지 판단하는 코드를 작성하라

# 지역코드	출생지
# 00 ~ 08	서울
# 09 ~ 12	부산
# >> 주민등록번호: 821010-1635210
# 서울이 아닙니다.
# >> 주민등록번호: 861010-1015210
# 서울 입니다.
# 정답확인

# 129
# 주민등록번호는 13자리로 구성되는데 마지막 자리수는 주민등록번호의 유효성을 체크하는데 사용된다. 먼저 앞에서부터 12자리의 숫자에 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5를 차례로 곱한 뒤 그 값을 전부 더한다. 연산 결과 값을 11로 나누면 나머지가 나오는데 11에서 나머지를 뺀 값이 주민등록번호의 마지막 번호가 된다.

#   8 2 1 0 1 0 - 1 6 3 5 2 1 0
# x 2 3 4 5 6 7   8 9 2 3 4 5 
# -----------------------------
# 1차 계산: (8*2 + 2*3 + 1*4 + 0*5 + 1*6 + 0*7 + 1*8 + 6*9 + 3*2 + 5*3 + 2*4 + 1*5) = (128 % 11) = 7
# 2차 계산: 11 -7 = 4
# 위와 같이 821010-1635210에 대해서 계산을 해보면 마지막 자리는 4가 되어야 함을 알 수 있다. 즉, 821010-1635210은 유효하지 않은 주민등록번호임을 알 수 있다.

# 다음과 같이 사용자로부터 주민등록번호를 입력받은 후 주민등록번호가 유효한지를 출력하는 프로그램을 작성하라.

# >> 주민등록번호: 821010-1635210
# 유효하지 않은 주민등록번호입니다. 
# 정답확인

# 130
# 아래 코드는 비트코인의 가격 정보를 딕셔너리로 가져오는 코드이다.

# import requests
# btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
# btc 딕셔너리 안에는 시가, 종가, 최고가, 최저가 등이 저장되어 있다. 최고가와 최저가의 차이를 변동폭으로 정의할 때 (시가 + 변동폭)이 최고가 보다 높을 경우 "상승장", 그렇지 않은 경우 "하락장" 문자열을 출력하라.

# Key Name	Description
# opening_price	최근 24시간 내 시작 거래금액
# closing_price	최근 24시간 내 마지막 거래금액
# min_price	최근 24시간 내 최저 거래금액
# max_price	최근 24시간 내 최고 거래금액
# 정답확인

# 135
# for문을 풀어서 동일한 동작을 하는 코드를 작성하라.

# for 변수 in ["A", "B", "C"]:
#   b = 변수.lower()
#   print("변환:", b)
# 정답확인

# 145
# 리스트에 동물 이름 저장돼 있다.

# 리스트 = ['dog', 'cat', 'parrot']
# for문을 사용해서 동물 이름의 첫 글자만 출력하라.

# d
# c
# p
# 정답확인

# 148
# 리스트에는 네 개의 문자열이 바인딩돼 있다.
# 리스트 = ["가", "나", "다", "라"]
# for문을 사용해서 다음과 같이 출력하라.

# 나
# 다
# 라
# 정답확인

# 149
# 리스트에는 네 개의 문자열이 바인딩돼 있다.

# 리스트 = ["가", "나", "다", "라"]
# for문을 사용해서 다음과 같이 출력하라.

# 가
# 다
# 정답확인

# 150
# 리스트에는 네 개의 문자열이 바인딩돼 있다.

# 리스트 = ["가", "나", "다", "라"]
# for문을 사용해서 다음과 같이 출력하라.

# 라
# 다
# 나
# 가
# 정답확인

# 157
# 이름의 첫 글자를 대문자로 변경해서 출력하라.

# 리스트 = ['dog', 'cat', 'parrot']
# Dog
# Cat
# Parrot
# (참고) upper() 메서드는 문자열을 대문자로 변경합니다.

# >> 변수 = "a"
# >> a.upper()
# A
# >> 변수 = "abc"
# >> 변수.upper()
# ABC
# 정답확인


# 158
# 파일 이름이 저장된 리스트에서 확장자를 제거하고 파일 이름만 화면에 출력하라. (힌트: split() 메서드)

# 리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
# hello
# ex01
# intro
# 정답확인

# 164
# 99부터 0까지 1씩 감소하는 숫자들을, 한 라인에 하나씩 출력하라.

# 정답확인

# 165
# for문을 사용해서 아래와 같이 출력하라.

# 0.0
# 0.1
# 0.2
# 0.3
# 0.4
# 0.5
# ...
# 0.9
# 정답확인

# 172
# 아래와 같이 리스트의 데이터를 출력하라. 단, range문을 사용하지 말 것.

# price_list = [32100, 32150, 32000, 32500]
# 0 32100
# 1 32150
# 2 32000
# 3 32500
# 정답확인

# 174
# 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.

# price_list = [32100, 32150, 32000, 32500]
# 100 32150
# 110 32000
# 120 32500
# 정답확인

# 175
# my_list를 아래와 같이 출력하라.

# my_list = ["가", "나", "다", "라"]
# 가 나
# 나 다
# 다 라
# 정답확인

# 177
# 반복문과 range 함수를 사용해서 my_list를 아래와 같이 출력하라.

# my_list = ["가", "나", "다", "라"]
# 라 다
# 다 나
# 나 가
# 정답확인

# 183
# 아래 표를 stock 이름의 딕셔너리로 표현하라.시가를 key로 저장하고, 나머지 같은 열의 데이터를 리스트로 저장해서 value로 저장한다. 종가 역시 key로 저장하고 나머지 같은 열의 데이터를 리스트로 저장해서 value로 저장한다.

# 시가	종가
# 100	80
# 200	210
# 300	330
# 정답확인

# 185
# 리스트에 저장된 데이터를 아래와 같이 출력하라.

# apart = [ [101, 102], [201, 202], [301, 302] ]
# 101 호
# 102 호
# 201 호
# 202 호
# 301 호
# 302 호
# 정답확인

# 186
# 리스트에 저장된 데이터를 아래와 같이 출력하라. 단, reverse()함수는 사용하지 말것

# apart = [ [101, 102], [201, 202], [301, 302] ]
# 301 호
# 302 호
# 201 호
# 202 호
# 101 호
# 102 호
# 정답확인

# 187
# 리스트에 저장된 데이터를 아래와 같이 출력하라. 단, reverse()함수는 사용하지 말것

# apart = [ [101, 102], [201, 202], [301, 302] ]
# 302 호
# 301 호
# 202 호
# 201 호
# 102 호
# 101 호
# 정답확인