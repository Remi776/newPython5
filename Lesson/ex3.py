
n = int(input())

def isPrime(num, count = 0):
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            count += 1
    if count == 0:
        print("true")
    else:
        print("false")

isPrime(n)