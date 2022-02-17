def main(str_1, str_2):

    if str_1 != str(str_1) and str_2 != str(str_2):
        return 0
    elif str_1 == str_2 :
        return 1
    else :
        if len(str_1) > len(str_2):
            return 2
        elif str_2 == 'learn':
            return 3
        else :
            raise ValueError ('Введённые данные не соответсвуют заявленным требованиям')

print(main(1, 1))
print(main('python', 'python'))
print(main('visual_studio', 'python'))
print(main('we', 'learn'))