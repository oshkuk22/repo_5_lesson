"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке."""

with open('2.txt','r') as file_strings:
    strings_lines = file_strings.readlines()

print(f'Count strings in file {file_strings.name} : {len(strings_lines)}\n')

for i in strings_lines:
    s_for_print = i.replace('\n', '')
    s = s_for_print.replace('.', ' ').replace(',', ' ').replace('  ', ' ').split()
    print(f'File : {file_strings.name}\nString : {s_for_print}\nCount words : {len(s)}')
