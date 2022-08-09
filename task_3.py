import random


def third_task(arr):
    """Составить алгоритм: на входе есть числовой массив, необходимо вывести элементы массива кратные 3"""
    new_arr = []
    for i in arr:
        if i % 3 == 0:
            new_arr.append(i)
    print(new_arr)


array = [random.randint(0,100) for x in range(10)]

print(array)
third_task(array)
