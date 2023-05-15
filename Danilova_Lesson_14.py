sign = str(input('Операция: '))
if sign == '0':
    print('Выход')
elif sign == '+':
    def summa(a, b):
        return a + b
    print(summa(float(input('Введите первое число: ')), float(input('Введите второе число: '))))
elif sign == '-':
    def difference(a, b):
        return a - b
    print(difference(float(input('Введите первое число: ')), float(input('Введите второе число: '))))
elif sign == '*':
    def multiplication(a, b):
        return a * b
    print(multiplication(float(input('Введите первое число: ')), float(input('Введите второе число: '))))
elif sign == '/':
    def division(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print('На ноль делить нельзя')
    print(division(float(input('Введите первое число: ')), float(input('Введите второе число: '))))
else:
    print('Нет такой операции')
    #