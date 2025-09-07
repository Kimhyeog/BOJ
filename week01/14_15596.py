#이건 문제에 요구조건이 인자를 리스트로 하라고 했기떄문에
#재귀로 풀수 없다.

def solve(a: list) :
    sum =0
    
    for i in range(0,len(a)) :
        sum +=a[i]
    return sum

