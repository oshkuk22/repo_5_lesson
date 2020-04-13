"""1. Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка."""


with open("1.txt", 'w') as text_file:
    while True:
        string_line = input('Enter - Exit\nInput string : ')
        if string_line == '':
            break
        else:
            text_file.write(string_line+'\n')

print('Recording is complete')