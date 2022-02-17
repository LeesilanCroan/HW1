def hello_user():
    how_r_u = input('Как дела? ')
    return (how_r_u)

while True:
    if hello_user() == 'Хорошо':
        break
    else:
        print('А если подумать?')