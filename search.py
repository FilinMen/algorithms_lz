import random 
#линейный поиск
list_1 = random.sample(range(1000001), 100)#sample позволяет выбрать случайные элементы из указанного диапазона 100 без дубликатов.
print(list_1)

element = int(input('искомый элемент:'))
score = 0 #начинаем подсчет с 0 количество сравнений
if element in list_1: #если эле-т находится в list_1
    for i in range(0, len(list_1)):
        score = score + 1 #прибавляем каждый цикл +1
        if list_1[i] == element:
            break 
    print(f'индекс искомого эл-та:{i}')
else:
    print("элемент не найден")
print(f'количество сравнений:{score}')
'''
#бинарный поиск
lys = [10,20,30,40,50]
val = 20

first = 0
last = len(lys)-1
index = -1
while (first <= last) and (index == -1):
    mid = (first+last)//2
    if lys[mid] == val:
        index = mid
    else:
        if val<lys[mid]:
            last = mid -1
        else:
            first = mid +1

print(index)
'''