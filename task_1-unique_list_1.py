# (RUS) Напишите функцию, которая получает 4 списка чисел и выводит количество уникальных.
# Например, если ввод:
# 1,2,3
# 1,2,3
# 3,4,5
# 3,2,1
# тогда результат должен быть 3.

# (ENG) Write a function that takes 4 lists of numbers and outputs the number of unique ones.
# For example, if the input is:
# 1,2,3
# 1,2,3
# 3,4,5
# 3,2,1
# then the result should be 3.

# Option 1
# def func(*args):
#     return len(set([tuple(x) for x in args]))

# Option 2
# def func(*args):
#     return len(set(map(tuple, args)))

# Option 3
# print(len(set(__import__('sys').stdin.read().split('\n'))))

# Option 4
def func(*args):
    res = []
    for lst in args:
        if lst not in res:
            res.append(lst)
    return len(res)


a = [1, 2, 3]
b = [1, 2, 3]
c = [3, 4, 5]
d = [3, 2, 1]
print(func(a, b, c, d))
