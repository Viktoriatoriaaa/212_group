import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton

class Calculator(QWidget): #наследовали готовый класс QWidget
    def __init__(self):
        super().__init__()
        self.initUI()
        #объявим переменные для хранения промежуточных значений калькулятора:
        self.my_input = 0 #промежуточное значение вычислений
        self.operand_1 = 0 #первое число
        self.operand_2 = 0 #второе
    def initUI(self):
        self.setGeometry(300, 300,325,370)
        self.setWindowTitle('Калькулятор')
        self.label = QLabel(self)
        self.label.resize(325,50)
        self.label.move(0,0)
        self.label.setText('Введите какие-то значения:')

        #Создаем кнопки-цифры:
        self.num_1 = QPushButton('1',self)
        self.num_1.resize(50,50)
        self.num_1.move(0,50)

        self.num_2 = QPushButton('2', self)
        self.num_2.resize(50, 50)
        self.num_2.move(50, 50)

        self.num_3 = QPushButton('3', self)
        self.num_3.resize(50, 50)
        self.num_3.move(100, 50)

        self.num_4  = QPushButton('4', self)
        self.num_4.resize(50, 50)
        self.num_4.move(0, 100)

        self.num_5 = QPushButton('5', self)
        self.num_5.resize(50, 50)
        self.num_5.move(50, 100)

        self.num_6 = QPushButton('6', self)
        self.num_6.resize(50, 50)
        self.num_6.move(100, 100)

        self.num_7 = QPushButton('7', self)
        self.num_7.resize(50, 50)
        self.num_7.move(0, 150)

        self.num_8 = QPushButton('8', self)
        self.num_8.resize(50, 50)
        self.num_8.move(50, 150)

        self.num_9 = QPushButton('9', self)
        self.num_9.resize(50, 50)
        self.num_9.move(100, 150)

        self.num_0 = QPushButton('0', self)
        self.num_0.resize(50, 50)
        self.num_0.move(0, 200)
        # Создаем кнопки-операции:
        self.plus = QPushButton('+', self)
        self.plus.resize(100, 50)
        self.plus.move(150, 50)

        self.minus = QPushButton('-', self)
        self.minus.resize(100, 50)
        self.minus.move(150, 100)

        self.mul = QPushButton('x', self)
        self.mul.resize(100, 50)
        self.mul.move(150, 150)

        self.div = QPushButton(':', self)
        self.div.resize(100, 50)
        self.div.move(150, 200)
        #Кнопки равно и очистить:
        self.ravno = QPushButton('=', self)
        self.ravno.resize(50, 50)
        self.ravno.move(50, 200)

        self.clear = QPushButton('C', self)
        self.clear.resize(50, 50)
        self.clear.move(100, 200)
        # Кнопка возведения в степень 2:
        self.step = QPushButton('**', self)
        self.step.resize(50, 50)
        self.step.move(0, 250)
        # Извлечение квадратного корня
        self.kor = QPushButton('v', self)
        self.kor.resize(50, 50)
        self.kor.move(50, 250)
        # Целочисленное деление:
        self.delenie_n = QPushButton('//', self)
        self.delenie_n.resize(50, 50)
        self.delenie_n.move(100, 250)
        # Остаток от деления:
        self.ostatok = QPushButton('ost', self)
        self.ostatok.resize(100, 50)
        self.ostatok.move(150, 250)

        #Привязка кнопок к их функциям:
        self.num_0.clicked.connect(self.zero)
        self.num_1.clicked.connect(self.one)
        self.num_2.clicked.connect(self.two)
        self.num_3.clicked.connect(self.three)
        self.num_4.clicked.connect(self.four)
        self.num_5.clicked.connect(self.five)
        self.num_6.clicked.connect(self.six)
        self.num_7.clicked.connect(self.seven)
        self.num_8.clicked.connect(self.eight)
        self.num_9.clicked.connect(self.nine)
        # Привязка операций к кнопкам:
        self.plus.clicked.connect(self.plus_f)
        self.minus.clicked.connect(self.minus_f)
        self.mul.clicked.connect(self.mul_f)
        self.div.clicked.connect(self.div_f)
        self.ravno.clicked.connect(self.ravno_f)
        self.clear.clicked.connect(self.clear_f)
        self.step.clicked.connect(self.step_f)
        self.kor.clicked.connect(self.kor_f)
        self.delenie_n.clicked.connect(self.delenie_n_f)
        self.ostatok.clicked.connect(self.ostatok_f)

    #Функции кнопок
    def enter_value(self):
        if self.label.text() == 'Введите какие-то значения:' or self.label.text() == 'Деление на ноль!': #если на экране все еще приветствие, то убираем его
            self.label.setText('')
        self.label.setText(self.label.text() + self.my_input)

    def one(self):
        self.my_input = '1'
        self.enter_value()
    def two(self):
        self.my_input = '2'
        self.enter_value()
    def three(self):
        self.my_input = '3'
        self.enter_value()
    def four(self):
        self.my_input = '4'
        self.enter_value()
    def five(self):
        self.my_input = '5'
        self.enter_value()
    def six(self):
        self.my_input = '6'
        self.enter_value()
    def seven(self):
        self.my_input = '7'
        self.enter_value()
    def eight(self):
        self.my_input = '8'
        self.enter_value()
    def nine(self):
        self.my_input = '9'
        self.enter_value()
    def zero(self):
        self.my_input = '0'
        self.enter_value()

    def plus_f(self):
        self.operation = '+'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def minus_f(self):
        self.operation = '-'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def mul_f(self):
        self.operation = '*'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def div_f(self):
        self.operation = '/'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def step_f(self):
        self.operation = '**'
        self.operand_1 = float(self.label.text())

    def kor_f(self):
        self.operation = 'v'
        self.operand_1 = float(self.label.text())

    def delenie_n_f(self):
        self.operation = '//'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def ostatok_f(self):
        self.operation = 'ost'
        self.operand_1 = float(self.label.text())
        self.label.setText('')


    def ravno_f(self):
        self.operand_2 = float(self.label.text())
        if self.operation == '+': self.label.setText(str(self.operand_1 + self.operand_2))
        elif self.operation == '*': self.label.setText(str(self.operand_1 * self.operand_2))
        elif self.operation == '-':self.label.setText(str(self.operand_1 - self.operand_2))
        elif self.operation == '/':
            if self.operand_2 == 0: self.label.setText('Деление на ноль!')
            else: self.label.setText(str(self.operand_1 / self.operand_2))
        elif self.operation == '**': self.label.setText(str(self.operand_1 ** 2))
        elif self.operation == 'v': self.label.setText(str(self.operand_1 ** (0.5)))
        elif self.operation == '//': self.label.setText(str(self.operand_1 // self.operand_2))
        elif self.operation == 'ost': self.label.setText(str(self.operand_1 % self.operand_2))
    def clear_f(self):
        self.label.setText('Введите какие-то значения:')

app = QApplication(sys.argv) #создаем экземпляр app класса QApplication с аргументом sys.argv, который представляет список аргументов командной строки
#QApplication отвечает за обработку событий и управление основным циклом приложения

my_calculator = Calculator()
my_calculator.show() #показать объект калькулятор
sys.exit(app.exec())

#ДЗ на четверг: (отправляем скринами)
# Операции привязаить к кнопкам
# Добавить функции:
# 1. Возведение в любую степень
# 2. Извлечение корня второй степени
# 3. Целочисленное деление
# 4. Остаток от деления

