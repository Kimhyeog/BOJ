result = 1
digit_cnt = [0] * 10  # 0부터 9까지 숫자 개수 저장

# 3개의 숫자를 입력받아 곱하기
for _ in range(3):
    result *= int(input())

# 곱한 결과를 문자열로 변환
result = str(result)

# 각 숫자(문자)를 순회하면서 digit_cnt 배열 업데이트
for ch in result:
    digit = int(ch)
    digit_cnt[digit] += 1

# 결과 출력
for count in digit_cnt:
    print(count)


digit_num = ['0','1','2','3','4','5','6','7','8','9']
digit_cnt = [0,0,0,0,0,0,0,0,0,0]

num = 1

for i in range(0,3) :
    num *= int(input())

num = str(num)

#숫자 길이만큼 순회
for i in range(0,len(num)) :
    for j in range(0,10) :
        if num[i] == digit_num[j] :
            digit_cnt[j]+=1


for i in range(0,10) :
    print(digit_cnt[i])
