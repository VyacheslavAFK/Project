print("результат:", 1, 2, 3, 14, 354, sep=", ", end="<=\n")

print("Iphon (Вячеслав)")

print(round((32 + 46) / 14))

print (pow(2, 7)) #или print(2 ** 7)

#input("напишите своё имя:")

number = "25" #int (integer)
insert = 25.235403456 #float
word = "результат:" #string (str)

#print(word + insert) - ошибка
print(word + str(insert)) #задаём значение str для файла формата float или int

boolean = True

#print(number + insert) - ошибка
print(number + str(insert)) #как строка
print(insert + int(number)) #как число
print(word + str((insert + int(number))))

#name = input("введите ваше имя: ")
print('Введите вашу дату рождения:')
a = int(input('День:'))
b = int(input('Месяц:'))
c = int(input('Год:'))
v = [a, b, c]
hd = [10, 3, 2023]


if v[0] > hd[0]:
    hd[1] -= 1
    if v[1] == 4 or 6 or 9 or 11:
        p = 30
        v[0] = ((p + hd[0]) - a)
        hd[1] -= 1
        print(v[0])
        print(v)
    elif v[1] == 1 or 3 or 5 or 7 or 8 or 10 or 12:
        p = 31
        v[0] = ((p + hd[0]) - a)
        hd[1] -= 1
        print(v[0])
        print(v)
    else:
        p = 28
        v[0] = ((p + hd[0]) - a)
        hd[1] -= 1
        print(v[0])
        print(v)
if v[0] < hd[0]:
    v[0] = hd[0] - a
    print(v[0])
    print(v)


if v[1] > hd[1]:
    t = 12
    v[1] = ((t + hd[1]) - v[1])
    hd[2] -= 1
    print(v[1])
    print(v)
if v[1] < hd[1]:
    v[1] = hd[1] - b
    print(v[1])
    print(v)
v[2] = hd[2] - c
print(v)
print(p)
