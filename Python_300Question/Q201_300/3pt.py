# 221
# 입력된 문자열을 역순으로 출력하는 print_reverse 함수를 정의하라.

# print_reverse("python")
# nohtyp
# 정답확인

#revers()는 리스트만 가능하다.
def print_reverse(pri):
  
  return pri[::-1]

print(print_reverse("python"))

# 222
# 성적 리스트를 입력 받아 평균을 출력하는 print_score 함수를 정의하라.

# print_score ([1, 2, 3])
# 2.0
# 정답확인

def print_score(score = []) :
  sum_sco = 0
  for sco in score :
    sum_sco += sco
  return sum_sco / len(score)

def print_score(score = []) :
  
  return sum(score) / len(score)

print(print_score([1,2,3]))

# 223
# 하나의 리스트를 입력받아 짝수만 화면에 출력하는 print_even 함수를 정의하라.

# print_even ([1, 3, 2, 10, 12, 11, 15])
# 2
# 10
# 12
# 정답확인

def print_even(evenlist) :
  for num in evenlist :
#    print(num%2)
    #return num
    if num%2 == 0 :
      print("num = ", num)
  return num
      
  

print(print_even ([1, 3, 2, 10, 12, 11, 15]))

# 224
# 하나의 딕셔너리를 입력받아 딕셔너리의 key 값을 화면에 출력하는 print_keys 함수를 정의하라.

# print_keys ({"이름":"김말똥", "나이":30, "성별":0})
# 이름
# 나이
# 성별
# 정답확인

def print_keys(dict_list):
  return dict_list.keys()

print(print_keys ({"이름":"김말똥", "나이":30, "성별":0}))



# 225
# my_dict에는 날짜를 키값으로 OHLC가 리스트로 저장돼 있다.

# my_dict = {"10/26" : [100, 130, 100, 100],
#            "10/27" : [10, 12, 10, 11]}
# my_dict와 날짜 키값을 입력받아 OHLC 리스트를 출력하는 print_value_by_key 함수를 정의하라.

# print_value_by_key  (my_dict, "10/26")
# [100, 130, 100, 100]
# 정답확인


def print_value_by_key(dict_list, dict_key) :
  print(dict_list[dict_key])
  return 0

my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}

print(print_value_by_key  (my_dict, "10/26"))
#print하면 반환값이 호출 된다.

print("-"*16)
# 226
# 입력 문자열을 한 줄에 다섯글자씩 출력하는 print_5xn(string) 함수를 작성하라.

# print_5xn("아이엠어보이유알어걸")
# 아이엠어보
# 이유알어걸
# 정답확인

def print_5xn(string) :
  print(string.split('보'))

print_5xn("아이엠어보이유알어걸")

#solution
#for문을 사용했다.

# def print_5xn(line):
#     chunk_num = int(len(line) / 5)#10/5 =2
#     for x in range(chunk_num + 1) :#2+1 3(0,1,2)
#       print(x)
#       print(line[x * 5: x * 5 + 5])

# print_5xn("아이엠어보이알유어걸")

# 227
# 문자열과 한줄에 출력될 글자 수를 입력을 받아 한 줄에 입력된 글자 수만큼 출력하는 print_mxn(string) 함수를 작성하라.

# printmxn("아0이1엠2어3보4이5유6알7어8걸9", 3)
# 아0이엠2/3
# 어3보이5/6
# 유6알어8/9
# 걸9
# 정답확인

def print_mxn(mystr, num) :
  for i in range(num+1) :#4(0,1,2,3)4,6,8
    print(mystr[i*3:3+(i*3)]) #0:3,  3:6,  6:9,  9:

print_mxn("아이엠어보이유알어걸",3)

#아래와 같이 사용하면 for문은 오류가 난다.
# for i in 10 :
#   print(i)

# 228
# 연봉을 입력받아 월급을 계산하는 calc_monthly_salary(annual_salary) 함수를 정의하라. 회사는 연봉을 12개월로 나누어 분할 지급하며, 이 때 1원 미만은 버림한다.

# calc_monthly_salary(12000000)
# 1000000
# 정답확인

def calc_monthly_salary(annual_salary) :
  annual_salary = int(annual_salary/12)
  return annual_salary
calc_monthly_salary(120000000)


# 229
# 아래 코드의 실행 결과를 예측하라.

# def my_print (a, b) :
#     print("왼쪽:", a)
#     print("오른쪽:", b)

# my_print(a=100, b=200)
# 정답확인

"왼쪽: 100"
"오른쪽: 200"

# 230
# 아래 코드의 실행 결과를 예측하라.

# def my_print (a, b) :
#     print("왼쪽:", a)
#     print("오른쪽:", b)

# my_print(b=100, a=200)
# 정답확인

"왼쪽: 200"
"오른쪽: 100"
