def main(age):
    age=int(age)
    if age<7 and age>0:
        return('Не плачь. Мама отведёт тебя в садик')
    elif age<0:
        raise ValueError ('Добрый вечер,мистер Баттон! Пожалуйста, запустите программу ещё раз, и введите настоящий возраст.')
    elif age>=7 and age<18:
        return('Пора собираться в школу!')
    elif age>=18 and age<23:
        return('Тебе к первой. Вставай!')
    else:
        return('Вставай! деньги сами себя не заработают.')

print(main(input('Сколько вам лет? ')))