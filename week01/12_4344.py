C = int(input())

for i in range(0,C) :
    result = 0
    avg = 0
    sum = 0
    cnt = 0

    N = int(input())

    score_arr = list(map(int, input().split()))
    
    for j in range(0,N) :
        sum+=score_arr[j]

    avg = sum / N

    for j in range(0,N) :
        if score_arr[j]>avg :
            cnt+=1
    
    result = N/cnt

    print(f"{result:.3f}")

    C = int(input())

for _ in range(C):
    # 1. 한 줄 입력을 받아 N과 점수 리스트를 분리합니다.
    data = list(map(int, input().split()))
    N = data[0]
    scores = data[1:]
    
    # 평균을 계산합니다. (sum 변수명 대신 sum() 함수 사용)
    average = sum(scores) / N
    
    # 평균보다 높은 점수를 받은 학생 수를 셉니다.
    above_average_count = 0
    for score in scores:
        if score > average:
            above_average_count += 1
            
    # 2. 올바른 공식으로 비율을 계산합니다.
    ratio = (above_average_count / N) * 100
    
    # 3. 올바른 형식으로 출력합니다.
    print(f'{ratio:.3f}%')

    

        