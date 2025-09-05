N , value = map(int,input().split())

num_arr = list(map(int, input().split()))

for i in range(0,N) :
    if value > num_arr[i] :
        print(f"{num_arr[i]} ")


# N, value = map(int, input().split())

# numbers = list(map(int, input().split()))

# # numbers 리스트에서 값을 하나씩 num에 담아 반복
# for num in numbers:
#     if value > num:
#         print(num, end=' ')