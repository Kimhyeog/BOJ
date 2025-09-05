cnt = int(input())
for i in range(0, cnt) :
    # 결과값 , 연산 변수값 초기세팅
    result =0
    num = 0 
    # 문자열입력
    str = input()

    for i in range(0,len(str)) :
        #문자열 끝인덱스 아닐떄, 문자열 끝인덱스 일떄, 처리
        if(i<len(str)-1) : 
            if (str[i]=="O") and (str[i+1]=="O") :
                #연속 O일 떄,
                #순서1 : 연산 변수 
                num+=1
                #순서2 : 결과값에 적용
                result =result +num
 
            elif (str[i]=="O") and (str[i+1]=="X") :
                # X가 나타날경우 연산 후, 초기화
                num+=1
                result = result +num
                num=0
        else :
            #마지막 문자 처리
            if(str[i]=="O") :
                num +=1
                result += num
    # 각 한문장 결과값 출력
    print(result)


# cnt = int(input())

# for _ in range(cnt):
#     ox_string = input()
    
#     total_score = 0
#     consecutive_score = 0 # 연속 점수를 저장하는 변수
    
#     # 입력받은 문자열을 한 글자씩 순회
#     for char in ox_string:
#         if char == 'O':
#             consecutive_score += 1      # 'O'를 만나면 연속 점수 1 증가
#             total_score += consecutive_score # 증가된 점수를 총점에 더함
#         else: # 'X'를 만나면
#             consecutive_score = 0       # 연속 점수를 0으로 초기화
            
#     print(total_score)


            

