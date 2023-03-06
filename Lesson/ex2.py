from random import randint

n = int(input('Enter the num: '))
list_marks = [randint(1, 5) for i in range(n)]

new_list = list_marks.copy()
new_list = [min(new_list) if value == max(new_list) else value for i, value in enumerate(new_list)]

print(list_marks)
print(new_list)