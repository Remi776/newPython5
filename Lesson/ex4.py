def Replace(num):
    if num == 0:
        return ''
    bar = input()
    return Replace(num - 1) + bar
print(Replace(int(input())))