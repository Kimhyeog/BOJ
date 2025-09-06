
num1, num2 = input().split()

rev_num1 = int(num1[::-1])
rev_num2 = int(num2[::-1])

if rev_num1 > rev_num2 :
    print(rev_num1)
else :
    print(rev_num2)