# Реализовать два скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

from itertools import count, cycle

my_var = "HelpMe"
step = 0
# a
for i in count(5, 10):
    if i > 100:
        break
    print(i, end=' ')

# b
for i in cycle(my_var):
    step += 1
    if step > 50:
        break
    print(i, end='')


