team1 = 'Мастера кода'
team2 = 'Волшебники данных'
team1_num = 5            # кол-во участников в первой команде
team2_num = 6            # кол-во участников во второй команде
score_1 = 40              # кол-во задач решенных командой №1
score_2 = 42             # кол-во задач решенных командой №2
team1_time = 1552.512           # время за которое 1 команда решила задачи
team2_time = 2153.31451           # время за которое 2 команда решила задачи
challenge_result = str  # исход соревнований
tasc_total = score_1 + score_2           # количество задач
time_avg = (team1_time + team2_time) / tasc_total            # среднее время решения задач


if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера Кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'


''' Использование %'''
print('В команде %(team)s участников: %(team_num)s!' % {'team': team1, 'team_num': team1_num})
print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))
''' Использование format()'''
print('Команда {team} решила задач: {tasc}!'.format(team=team2, tasc=score_2))
print('{team} решили задачи за {time} c!'.format(team=team2, time=team2_time))
'''использование f-строк'''
print(f'Команды решили {score_1} и {score_1} задач.')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {tasc_total} задач, в среднем по {time_avg} секунды за задачу!')