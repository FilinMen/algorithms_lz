import random as ran
#сортировка пузырьком
list_1 = [ran.randint(0, 1000000) for t in range(100)]
intermediate1 = 0
stop_flag = True
while stop_flag:
    stop_flag = False
    for i in range(len(list_1) - 1):
        if list_1[i] < list_1[i + 1]:
            a = list_1[i]
            list_1[i] = list_1[i + 1]
            list_1[i + 1] = a
            stop_flag = True
        intermediate1 += 1
    print(list_1)       
print(intermediate1)
#сортировка выбором
list_2 = [ran.randint(0, 1000000) for u in range(100)]
intermediate = 0
for i in range(0 ,len(list_2)):
    min = i
    for j in range(i + 1,len(list_2)):
        intermediate += 1
        if list_2[j] > list_2[min]:
            min = j
    b = list_2[i]
    list_2[i] = list_2[min]
    list_2[min] = b
    print(list_2) 
print(intermediate)