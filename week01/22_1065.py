# 한 수 판정 함수
def is_hansoo(N) : 
	
	# 두 자리수이내면 무조건 True
	if N < 100 :
		return True
	
	# 💊입력된 수를 분해 작업 (암기)
	digitArr = list(map(int , str(N)))
	
	# 둘째 자리 - 첫째 자리 를 공차라고 정함
	difference = digitArr[1]- digitArr[0]
	
	# 순회 시작 : 둘째 자리수 부터
	for i in range(1,len(digitArr)-1) :
		# 공차랑 다르다면 종료
		if difference != digitArr[i+1] - digitArr[i] :
			return False
	return True

N = int(input())
                
for i in range(N , 0 , -1) :
    if is_hansoo(i) :
        print(i)
        break
