# Вариант 22
# Определить количество детей(<18) на борту в возрастном интервале
# медиана +- 3 позиции и сколько из них выжило


import csv

# Считываем файл csv и переводим его в список
file = open("titanic.csv", "r")
reader = list(csv.reader(file))


counter_child = 0
counter_mediana = []

for i in reader:
    if i[1] == "1":
        if i[5] != "" and i[5] != " ":
            if float(i[5]) < 18.0:
                counter_mediana.append([float(i[5])])
n = len(counter_mediana); index = n // 2
mediana_l = sorted(counter_mediana)[index-3]
mediana_r = sorted(counter_mediana)[index+3]

for i in counter_mediana:
    if mediana_l <= i <= mediana_r:
        counter_child += 1

print(f"Детей выжило:", counter_child)
