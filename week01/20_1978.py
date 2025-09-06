N = int(input())

numList = list(map(int , input().split()))

count = 0

for num in numList :

    if num ==1 :
        continue
    
    is_prime = True

    for i in range(2,num) :
        
        if num % i==0 :
            is_prime = False
            break
    
    if is_prime :
        count+=1

print(count)
