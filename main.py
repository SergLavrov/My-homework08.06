
# 9.82. Дано предложение, в котором нет символа "-". Определить количество букв 'о'
#       в первом слове. Учесть, что в начале предложения могут быть пробелы

sent = input('Input sentence: ')
index = 0
cntSymbol = 0
lenSent = len(sent)

while index < lenSent:
    if sent[index] == 'o':
        cntSymbol += 1
    if sent[index] == ' ':
        break
    index += 1
print('There are ' + str(cntSymbol) + ' ' + 'lettes')


# 9.141. Дан текст, в котором имеются цифры.

#  а) Найти их сумму.

someString = input('Enter text: ')
index = 0
summ = 0
lenString = len(someString)

while index < lenString:
    if someString[index].isdigit():
        summ += int(someString[index])
    index += 1
print(summ)


#  б) Найти максимальную цифру.

someString = input('Enter text: ')
index = 0
maxNumber = 0
lenString = len(someString)

while index < lenString:
    if someString[index].isdigit():
        num = int(someString[index])
        if num > maxNumber:
            maxNumber = num
    index += 1

print('Maxnumber is: ',maxNumber)


# 9.166. Дано предложение. Поменять местами его первое и последнее слово.

someString = 'my favorite new game'

if ' ' in someString:
    index = someString.index((' '))
    wordFirst = someString[:index]

    index1 = someString.rindex((' '))
    wordLast = someString[index1:]

    midle = someString[index:index1+1]

    result = wordLast + midle + wordFirst

print(result)


# 9.178. Дано предложение. Напечатать все его слова, предварительно преобразовав
#        каждое из них по следующему правилу:

# а) заменить первую встреченную букву 'a' на 'о';

someString = 'My favorite game'
print(someString.replace('a', 'o'))


# б) удалить из слова все вхождения последней буквы (кроме нее самой);

someString = 'Palanga the best'
index = 0
lenStr = len(someString)
result = ''

while index < lenStr:
    index1 = someString.index(' ')
    lastLetter = someString[index1 - 1]
    if someString[index] == lastLetter:
        result += ''
    else:
        result += someString[index]

    index += 1

print(result)


# в) оставить в слове только первые вхождения каждой буквы;
# г) в самом длинном слове удалить среднюю (средние) буквы. Принять, что
#    такое слово — единственное.
