def calc():
    try:
        a = int(input('Введите число: '))
        b = int(input('Введите число: '))
        с = input('Введите оператор: ')
        if с == '+':
            print(a+b)
        elif с == '-':
            print(a-b)
        elif с == ('*'):
            print(a*b)
        elif с == ('/'):
            print(a/b)
    except ValueError:
        print('Вы ввели неккоретное значение')
    except ZeroDivisionError:
        print('Ошибка деления на ноль')
calc()
