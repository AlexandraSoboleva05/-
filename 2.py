import csv
with open('space.txt','r',encoding='utf8') as f: #открываем файл и добавляем каждому кораблю его пароль
    read=csv.reader(f,delimiter='*',quotechar='"')
    sp=list(read)[1:]
    for i in range(1,len(sp)-1):
        j=i-1
        k=sp[i]

        while int((sp[j][0].split('-'))[1])<int((sp[j][0].split('-'))[1]):
            sp[j+1]=sp[j]
            j-=1
            sp[j+1]=k
    for i in sp:
        print(i)