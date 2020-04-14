"""7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать
данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста."""
import json

with open('7.txt', 'r') as file_strings:
    strings_line = file_strings.readlines()

firm_name = list()
form_ownership = list()
firm_revenue = list()
firm_costs = list()
firm_profit = list()
firm_name_profit = dict()
firm_name_loss = dict()
average_profit = dict()

for i in strings_line:
    s_for_parser = i.replace('\n', '').replace('.', '')
    firm_name.append(s_for_parser.split()[0])
    form_ownership.append(s_for_parser.split()[1])
    firm_revenue.append(s_for_parser.split()[2])
    firm_costs.append(s_for_parser.split()[3])

firm_profit = [int((int(firm_revenue[i]) - int(firm_costs[i]))) for i in range(len(firm_revenue))]

for i in range(len(firm_name)):
    if firm_profit[i] > 0:
        firm_name_profit[firm_name[i]] = firm_profit[i]
    else:
        firm_name_loss[firm_name[i]] = abs(firm_profit[i])

average_profit['average_profit'] = sum(firm_name_profit.values()) / len(firm_name_profit)

with open('7.json', 'w') as file_json:
    json.dump((firm_name_profit, average_profit, firm_name_loss), file_json)
# pull_requests
