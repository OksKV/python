# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

workers = []
salaries = 0
total_wage = 0
with open('salaries.txt') as f:
    for line in f.readlines():
        salaries += 1
        wage = float(line.split()[1])
        total_wage += wage
        if wage > 20000:
            workers.append(line.split()[0])
        else:
            continue
average_salary = total_wage / salaries
print(f'В нашей компании больше 20 000 рублей получают: {", ".join(workers)}.\n'
      f'Средняя заработная плата по компании: {average_salary}')

