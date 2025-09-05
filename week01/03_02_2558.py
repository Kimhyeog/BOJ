a = int(input())
b = input() # "32567"


# for 반복문에서 i는 인덱스가 아닌 '문자' 그 자체입니다
for num_char in reversed(b) : # "76523"
    # num : "3" , "2" , "5" , "6" , "7"
    num = int(num_char) # "3" -> 3
    print(a * num)

print(a*int(b))
