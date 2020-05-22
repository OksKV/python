# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# Dictionary method
seasons = {'winter': {12: 'December', 1: 'January', 2: 'February'}, 'spring': {3: 'March', 4: 'April', 5: 'May'},
           'summer': {6: 'June', 7: 'July', 8: 'August'}, 'autumn': {9: 'September', 10: 'October', 11: 'November'}}


def which_season():
    month = int(input('Please insert a number from 1 to 12'))
    if 1 <= month <= 12:
        for item, season in seasons.items():
            if month in season:
                print(f'{season[month]} is a month of {item}')
                break
            else:
                continue
    else:
        print('Incorrect number, please try again!')
        which_season()


which_season()

# List method

seasons = {'winter': [12, 1, 2], 'spring': [3, 4, 5], 'summer': [6, 7, 8], 'autumn': [9, 10, 11]}
month = int(input('Please insert a number from 1 to 12'))
for season in seasons:
    if month in seasons[season]:
        print(f'It is a month of {season}')
        break
    else:
        continue
