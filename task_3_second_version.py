def third_task():
    """Составить алгоритм: на входе есть числовой массив, необходимо вывести элементы массива кратные 3"""
    arr = list(map(int, input("Введите массив чисел: ").split()))
    new_arr = [i for i in arr if i % 3 == 0]
    print(new_arr)


third_task()