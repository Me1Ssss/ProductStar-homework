'''
# 1
list = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
list_2 = list[::2]
print(f'Итоговый список: {list_2}')
proiz = 1
for i in list_2:
    proiz *= i
print(f'Произведенние полученного списка: {proiz}')
print(f'Сумма всех чисел списка: {sum(list_2)}')
list_2_2 = []
list_2_2.append(proiz)
list_2_2.append(sum(list_2))
for j in list_2:
    list_2_2.append(j)
list_2_2.sort(reverse=True)
print(f'Отсортированный список: {list_2_2}')
string = ''
for s in list_2_2:
    string = string + '='.join(str(s))
print(f'Итоговая строка: {string}')
# 2
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 5, 9, -7, -10]
for i in a:
    if i < 5:
        print(i, end=', ')
# 3
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 11]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 34, 11, 12, 13]
ab = [x for x in a if x in b]
ab.sort()
print(ab)
# 4
s = "kafka python course stack flow dict list \
python stack course star product star product\
analytics flow star kafka stack flow ython \
list set ist fit predict dict list python \
ourse ython ourse star product ist fit predict \
analytics kafka stack flow product ist fit\
predict analytics star flow dict flow \
list python course stack flow dict list\
python stack course"
list = []
dict = {}
list.append(s.split())
for i in list:
    for x in i:
        dict.update({x: i.count(x)})


def get(d, value):
    for k, v in d.items():
        if v == value:
            return k


print(get(dict, max(dict.values())), ':', max(dict.values()))
#6
names = ['igor', 'dasha', 'martin', 'vladimir', 'rishat',
         'maria', 'marat', 'petr', 'dima', 'polina', 'katya', 'elena']
occupations = ['smm', 'developer', 'analyst', 'president', 'analyst',
               'ceo', 'customer development', 'founder', 'developer', 'ml engineer', 'product manager', 'cmo']
dict = {}
j = 0
for i in names:
    for j in range(len(occupations)):
        dict.update({i: occupations[j]})
        j = +1

print(dict)
# 7
dict1 = {1: 10, 2: 20, 3901: 11, 384: 13, 8489: 1, 48: 10}

dict2 = {3: 30, 4: 40, 93: 12, 91: 41, 95: 1, 841: 11, 584: 11}

dict3 = {5: 50, 6: 60, 9: 90, 3: 13, 7: 11}

dict1.update(dict2)
dict1.update(dict3)
print(len(sorted(dict1)))
'''
from operator import itemgetter
dict1 = {}
list = []
given_string = 'Python Star Course for beginners and\
experts for data science and analytics without sql with code'
given_string = given_string.replace(' ', '')
for x in given_string:
    dict1.update({x: given_string.count(x)})
sorted_dict = dict(sorted(dict1.items(), key=lambda x: x[1]))
# print(sorted_dict)
t = 0
for k, v in sorted_dict.items():
    print(k, v)
    t += 1
    if t == 8:
        break
