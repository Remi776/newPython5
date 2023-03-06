def summ(a, b):
    if a == 0:
        return b
    return summ(a - 1, b + 1)


num1, num2 = int(input()), int(input())
print(summ(num1, num2))
