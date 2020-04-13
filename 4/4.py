"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен
записываться в новый текстовый файл."""

string_list = list()

with open('4.txt', 'r') as file_strings:
    strings_lines = file_strings.readlines()


for i in strings_lines:
    s_for_print = i.replace('\n', '')
    if i.find('One') != -1:
        string_list.append(i.replace('One', u'Один'))
    elif i.find('Two') != -1:
        string_list.append(i.replace('Two', u'Два'))
    elif i.find('Three') != -1:
        string_list.append(i.replace('Three', u'Три'))
    elif i.find('Four') != -1:
        string_list.append(i.replace('Four', u'Четыре'))


with open('4_rus.txt', 'w') as file_rus:
    file_rus.writelines(string_list)
