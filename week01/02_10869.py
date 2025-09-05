import sys

# 입력을 빠르게 받기 위한 설정 (옵션)
# input = sys.stdin.readline 

# 한 줄에 있는 두 숫자를 공백으로 구분하여 입력받고, 정수로 변환합니다.
a, b = map(int, sys.stdin.readline().split())

# 각 연산의 결과를 순서대로 출력합니다.
print(a + b)
print(a - b)
print(a * b)
print(a // b) # 몫을 구하는 정수 나눗셈 연산자
print(a % b)