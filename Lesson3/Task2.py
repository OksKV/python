# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def describe_person(name, surname, birth_year, city, mail, phone):
    titles = ['name', 'last name', 'year of birth', 'city of living', 'e-mail', 'phone number']
    info = [name, surname, birth_year, city, mail, phone]
    return dict(zip(titles, info))


print(describe_person(name='Oksana', surname='Velichko', birth_year=1991, city='Moscow', mail='hdwh@mail.ru',
                      phone=8289898))
