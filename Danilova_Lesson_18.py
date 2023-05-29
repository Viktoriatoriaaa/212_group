class BankAccount:
    default_name = 'unknown'
    default_last_name = None
    def __init__(self, name = default_name, last_name = default_last_name):
        self.name = name
        self.last_name = last_name
        self.__accont_number = input('Номер счета: ')
        self.__balance = float(input('Начальный депозит: '))
    def info (self):
        print(
            f'Имя:{self.name},'
            f'Фамилия:{self.last_name},'
            f'Номер счета:{self.__accont_number},'
            f'Баланс:{self.__balance}'
        )
    @staticmethod
    def default_info():
        print(
            f'Имя по умолчанию:{BankAccount.default_name},'
            f'Фамилия по умолчанию:{BankAccount.default_last_name}'
        )
    def __deposit (self, plus):
        self.__balance+=plus
        print(f'Счет пополнен на {plus} рублей. На счету сейчас {self.__balance} рублей')
    def deposit(self, plus):
        self.__deposit(plus)
    def __withdraw (self, minus):
        self.__balance+=minus
        print(f'Счет пополнен на {minus} рублей. На счету сейчас {self.__balance} рублей')
    def withdraw(self, minus):
        self.__withdraw(minus)

BankAccount.default_info()
BankAccount1 = BankAccount('Ivan', 'Ivanov')
BankAccount1.info()
BankAccount1.deposit(500)
BankAccount1.info()
BankAccount1.withdraw(2000)
BankAccount1.info()