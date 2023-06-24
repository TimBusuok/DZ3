# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

n = int(input('введите размер массива'))
x = int(input('введите число ')) 
array = list(map(int, input().split()))
print(array) 
  

closest = array[0]
min_diff = abs(closest - x)

for i in range(1, n):
    diff = abs(array[i] - x)
    

    if diff < min_diff:
        closest = array[i]
        min_diff = diff


print(closest)


