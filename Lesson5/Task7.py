# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
# среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список.
# Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

import json

companies = {}
total_sum = 0
count = 0

with open('Task7.txt') as file:
    for line in file.readlines():
        company = line.split()
        companies[company[0]] = int(company[2]) - int(company[3])
for i in companies:
    if companies[i] > 0:
        total_sum += companies[i]
        count += 1

with open("Task7.json", 'w') as file:
    json.dump([companies, {'average_profit': int(total_sum / count)}], file)




