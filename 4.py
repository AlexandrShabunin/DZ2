"""
Задание 4. Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().

Пример:
Введите целые числа через пробел: 1 2 3 4
Результат: 2 1 4 3

Введите целые числа через пробел: 1 2 3
Результат: 2 1 3
"""
list_1 = input('Введите целые числа, через пробел: ').split()
for w in range(0, len(list_1)-1, 2):
    list_1[w], list_1[w+1] = list_1[w+1], list_1[w]
print('Результат:', list_1)