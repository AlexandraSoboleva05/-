import csv


def passw(a):  # passw(a) - функция для создания пароля, a- все информация о корабле
    pl = a[1][-3:]  # по кусочкам собираем пароль. pl- 3 последние буквы названия планеты
    k = (a[0].split('-'))[0][2:0:-1]  # k - 2 среддние буквы кода корабля
    pl2 = (a[1][:3])[::-1]  # pl2 - 3 буквы планеты в обратном порядке
    return (pl + k + pl2).upper()


import csv

with open('space.txt', 'r', encoding='utf8') as f:  # открываем файл и добавляем каждому кораблю его пароль
    read = csv.reader(f, delimiter='*', quotechar='"')
    sp = list(read)[1:]
    for i in sp:
        i.append(passw(i))
with open('space_uniq_password.csv', 'w', encoding='utf8',
          newline='') as f:  # создаём новый файл записываем туда данные о кораблях с внесёнными паролями
    W = csv.writer(f, delimiter='*')
    W.writerow(['ShipName*planet*coord_place*direction*password'])
    W.writerows(sp)
