s = input('введите фразу: ')
a = s.split(' ')
stroka = []
for x in a:
    stroka.append(x)
hash = ''
key = input('Введите ключ: ')
while key != '':
    for i in range(len(stroka)):
        hash += str(int(key) % len(stroka[i]))

    print(hash)
    hash = ''
    key = input('Введите ключ: ')