num1, num2 = int(input()), int(input())

def summ(a, b):
    if a == 0 and b == 0:
        return 0
    if a == 0:
        return summ(0, b - 1) + 1
    if b == 0:
        return summ(a - 1, 0) + 1
    return summ(a - 1, b - 1) + 2

print(summ(num1, num2))