def prime(num):
    count = 0
    for i in range(1,num+1):
        if num%i == 0:
            count += 1

    result = "Prime" if count==2 else "Not prime"
    print(result)

prime(8)