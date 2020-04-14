"""6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}"""

from functools import reduce

with open('6.txt','r') as file_strings:
    strings_line = file_strings.readlines()

subject = list()
count_hours = list()
dict_subject = dict()

for i in strings_line:
    s_for_parser = i.replace('\n', '')
    subject.append(s_for_parser.split(':')[0])
    count_hours.append(s_for_parser.split(":")[1].
                       replace('—','').replace('(л)','').replace('(пр)','').replace('(лаб)','').replace('.',''))

count_hours_list = [i.split() for i in count_hours]

for i in range(len(count_hours_list)):
    sum = 0
    sum = reduce(lambda el_1, el_2: int(el_1)+int(el_2), count_hours_list[i])
    dict_subject[subject[i]] = sum

print(dict_subject)
