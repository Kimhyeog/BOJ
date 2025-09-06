
import math


A, B, V = map(int, input().split())

#아니 근데 올림처리를 했는데, 소수처리되서 런
cnt = int(math.ceil((V-A) / (A-B)) + 1)

print(cnt)