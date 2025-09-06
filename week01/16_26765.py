cnt = int(input())

for i in range(0,cnt) :
    # 반복 횟수 , 문자열 입력
    data = input().split()

    # 분리
    N = int(data[0]) # 반복횟수

    # 반복할 대상 문자열
    input_string = data[1]

    # 가공 후의 문자열
    result_string = ""

    # 제작 시작
    for j in range(len(input_string)) :
        result_string +=input_string[j]*N
    
    print(result_string)
