def hello_user():
    how_r_u = input('Как дела? ')
    return (how_r_u)

while True:
    try:
        if hello_user() == 'Хорошо':
            break
        else:
            print('А если подумать?')
    except(KeyboardInterrupt):
        print('Пока')
        break