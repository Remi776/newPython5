num1, num2 = int(input()), int(input())

def exponentiation(a, b):
    if b == 0:
        return 1
    return exponentiation(a, b - 1) * a

print(exponentiation(num1, num2))
