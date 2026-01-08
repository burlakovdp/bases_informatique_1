def ératosthène(n):
    numbers = [True]*n
    for i in range(n+1):
        for j in range(1, n):
            if i != 0 and i != 1:
                if j % i == 0:
                    if numbers[j] != False:
                        numbers[j] = False
    print(numbers)

ératosthène(100)
