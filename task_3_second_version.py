def third_task():
    """Составить алгоритм: на входе есть числовой массив, необходимо вывести элементы массива кратные 3"""
    arr = list(map(int, input("Введите массив чисел: ").split()))
    new_arr = []
    for i in arr:
        if i % 3 == 0:
            new_arr.append(i)
    print(new_arr)


third_task()