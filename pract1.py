score = 0

while score == 0:
    print('Какая версия языка сейчас актуальна?')
    q_ans1 = 'python3'
    ans1 = input('Введите ваш ответ ').lower()
    if ans1 == q_ans1:
        print('Верно ,вы получаете очко!')
        score += 1
while score == 1:
    print('Какая кодировка используется в строках?')
    q_ans2 = 'utf8'
    ans2 = input('Введите ваш ответ ').lower()
    if ans2 == q_ans2:
        print('Верно ,вы получаете очко!')
        score += 1
    exit
print()
while score == 2:
    print('Сколько значений есть у bool?')
    q_ans3 = '2'
    ans3 = input('Введите ваш ответ ').lower()
    if ans3 == q_ans3:
        print('Верно ,вы получаете очко!')
        score += 1
    exit
print()
while score == 3:
    print('Набор рекомендаций,о том,как сделать код Python более читабельным это ...')
    q_ans4 = 'pep8'
    ans4 = input('Введите ваш ответ ').lower()
    if ans4 == q_ans4:
        print('Верно ,вы получаете очко!')
        score += 1
    exit
print()
while score == 4:
    print('Python — это ... язык. Заполните пропуск')
    q_ans5 = 'интерпретируемый'
    ans5 = input('Введите ваш ответ ').lower()
    if ans5 == q_ans5:
        print('Верно ,вы получаете очко!')
        score += 1
    exit
print()
while score == 5:
    print('Какой тип данных:List,Dict,Sets?')
    q_ans6 = 'мутируемый'
    ans6 = input('Введите ваш ответ ').lower()
    if ans6 == q_ans6:
        print('Верно ,вы получаете очко!')
        score += 1
    exit
print()
while score == 6:
    print('Какой тип данных:strings,tuples,numbers?')
    q_ans7 = 'неизменный'
    ans7 = input('Введите ваш ответ ').lower()
    if ans7 == q_ans7:
        print('Верно ,вы получаете очко!')
        score += 1
    exit
print()
while score == 7:
    print('Анонимная функция с одним выражением, часто используемая в качестве inline функции это...')
    q_ans8 = 'лямбда'
    ans8 = input('Введите ваш ответ ').lower()
    if ans8 == q_ans8:
        print('Верно ,вы получаете очко!')
        score += 1
    exit
print()
while score == 8:
    print('Механизм выбора ряда элементов из типов последовательности, таких как список, кортеж, \
          строки и т.д., известен как...(на английском)?')
    q_ans9 = 'slicing'
    ans9 = input('Введите ваш ответ ').lower()
    if ans9 == q_ans9:
        print('Верно ,вы получаете очко!')
        score += 1
    exit
print()
while score == 9:
    print('Специфическое изменение, которое мы делаем в синтаксисе Python, чтобы легко изменять функции это...')
    q_ans10 = 'декоратор'
    ans10 = input('Введите ваш ответ ').lower()
    if ans10 == q_ans10:
        print('Верно ,вы получаете очко!')
        score += 1
    exit
print()
print('Вы набрали 10/10 очков!')
