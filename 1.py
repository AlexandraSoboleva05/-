import csv

with open('space.txt', 'r',
          encoding='utf8') as f:  # открываем файл, ищем координаты 0 0 и заменяем их в соответствии с формулой.
    read = csv.reader(f, delimiter='*', quotechar='"')
    sp = list(read)[1:]
    for i in sp:
        n = int((i[0].split('-'))[1][0])
        m = int((i[0].split('-'))[1][1])
        t = len(i[1])
        xd = int((i[-1].split())[0])
        yd = int((i[-1].split())[1])

        if i[2] == '0 0':
            if n > 5:
                i[2] = str(n + xd) + ' ' + '0'
            else:
                i[2] = str(-(n + xd) * 4 + t) + ' ' + '0'
            if m > 3:
                i[2] = i[2][:i[2].index(' ') + 1] + str(m + t + yd)
            else:
                i[2] = i[2][:i[2].index(' ') + 1] + str(-(n + yd) * m)
with open('space_new.txt', 'w', encoding='utf8',
          newline='') as f:  # создаём новый файл записываем туда изменённые координаты
    W = csv.writer(f, delimiter='*')
    W.writerow(['ShipName*planet*coord_place*direction'])
    W.writerows(sp)
with open('space_new.txt', 'r',
          encoding='utf8') as f1:  # открываем новый файл и ищем корабли с V последним элементом кода
    read = csv.reader(f1, delimiter='*', quotechar='"')
    Sp = list(read)[1:]
    for i in Sp:
        if (i[0].split('-'))[0][-1] == 'V':
            print(i)
