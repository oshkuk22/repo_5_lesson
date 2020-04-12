"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""

with open('3.txt','r') as file_strings:
    strings_lines = file_strings.readlines()

print(f'Count employees in file {file_strings.name} : {len(strings_lines)}')

salary = []
employees = []

for i in strings_lines:
    s_for_parser = i.replace('\n', '')
    salary.append(float(s_for_parser.split(':')[1]))
    employees.append(s_for_parser.split(":")[0])

salary_less = [employees[i] for i in range(len(salary)) if salary[i] < 20000]

print(f'List of employees with a salary less than 20000 : {salary_less}\n'
      f'Count list of employees less:{len(salary_less)}')
print(f'Average  salary is: {(sum(salary)/len(salary)):.3f}')
