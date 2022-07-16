#031Q~040Q
# 031 문자열 합치기
# 아래 코드의 실행 결과를 예상해보세요.

# >> a = "3"
# >> b = "4"
# >> print(a + b)
# My solution
from re import A


print("34") #새로운 문자열이 생기는 것이다.

# 032 문자열 곱하기
# 아래 코드의 실행 결과를 예상해보세요.
# >> print("Hi" * 3)
# My solution

print("HiHiHi")

# 033 문자열 곱하기
# 화면에 '-'를 80개 출력하세요.

# 실행 예:
# --------------------------------------------------------------------------------
# My solution

print('-' * 80)

# 034 문자열 곱하기
# 변수에 다음과 같은 문자열이 바인딩되어 있습니다.

# >>> t1 = 'python'
# >>> t2 = 'java'
# 변수에 문자열 더하기와 문자열 곱하기를 사용해서 아래와 같이 출력해보세요.

# 실행 예:
# python java python java python java python java
# My solution

t1 = 'python'
t2 = 'java'
print((t1 + ' ' + t2 + ' ') * 4)

# 035 문자열 출력
# 변수에 다음과 같이 문자열과 정수가 바인딩되어 있을 때 % formatting을 사용해서 다음과 같이 출력해보세요.

# name1 = "김민수" 
# age1 = 10
# name2 = "이철희"
# age2 = 13
print("35번은 다시 풀어보세요.")
# 이름: 김민수 나이: 10
# 이름: 이철희 나이: 13
# My solution
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s나이: %d" % (name1, age1))
print("이름: %s나이: %d" % (name2, age2))

# 036 문자열 출력
# 문자열의 format( ) 메서드를 사용해서 035번 문제를 다시 풀어보세요.
print("36번은 다시 풀어보세요.")
# My solution
print("이름: {}나이: {}".format(name1, age1))
print("이름: {}나이: {}".format(name2, age2))

# 037 문자열 출력
# 파이썬 3.6부터 지원하는 f-string을 사용해서 035번 문제를 다시 풀어보세요.
print("37번은 다시 풀어보세요.")
# My solution
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")

# 038 컴마 제거하기
# 삼성전자의 상장주식수가 다음과 같습니다. 컴마를 제거한 후 이를 정수 타입으로 변환해보세요.

# 상장주식수 = "5,969,782,550"
# My solution
상장주식수 = "5,969,782,550"
상장주식수 = 상장주식수.replace(',','')
print(int(상장주식수))

# 039 문자열 슬라이싱
# 다음과 같은 문자열에서 '2020/03'만 출력하세요.

# 분기 = "2020/03(E) (IFRS연결)"
# My solution
분기 = "2020/03(E) (IFRS연결)"
print(분기[0:7]) #print(분기[:7])

# 040 strip 메서드
# 문자열의 좌우의 공백이 있을 때 이를 제거해보세요.
print("40번은 다시 풀어보세요.")
# data = "   삼성전자    "
# My solution
data = "   삼성전자    "
print(data)
print(data.strip())