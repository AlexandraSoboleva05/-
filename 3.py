import csv

with open('space.txt', 'r', encoding='utf8') as f:  # открываем файл
    read = csv.reader(f, delimiter='*', quotechar='"')
    sp = list(read)[1:]
    q = input()

    while q != 'stop':  # программа принимает q - введённый запрос и ищет совпадения в файле.
        for i in sp:
            if i[0] == q:
                pl = i[1]
                d = i[-1]
                print(
                    f'Корабль {i[0]} был отправлен с планеты: {pl} и его направление движения было: {d}')  # если совпадения есть - выводит результат в необходимом формате
                break
        else:
            print('error.. er.. ror..')  # иначе- сообщает  о том. что совпадений нет

        q = input()
