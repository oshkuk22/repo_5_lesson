"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

string_numbers = input('Input numbers separated by spaces:')

with open('5.txt','w') as file_write:
    file_write.writelines(string_numbers)


with open('5.txt','r') as file_read:
    list_numbers = file_read.readlines()[0].split()

sum = 0

for i in list_numbers:
    sum = sum + int(i)

print(f"Sum number in file : {sum}")
