
class Company:
    levels = {1: "junior", 2: "middle", 3: "senior", 4: "lead"}
    def __init__(self, index):
        self._index = index
        self._level = Company.levels[index]
    def _level_up(self):
        if self._index < len(Company.levels):
            self._index += 1
            self._level = Company.levels[self._index]
            print(f'Программист достиг уровня {self._index}: {self._level}')
    def is_lead(self):
        return self._index == len(Company.levels)

class Programmer(Company):
    def __init__(self, name, age, level):
        super().__init__(level)
        self.name = name
        self.age = age
    def work(self):
        self._level_up()
    def info(self):
            print(
                f'Имя: {self.name}, '
                f'Возраст: {self.age},'
                f'Квалификация: {self._level}'
            )

    @staticmethod
    def knowledge_base():
        print('Программирование — это процесс создания компьютерных программ.')

Programmer.knowledge_base()
Programmer_1 = Programmer('Иван', 30, 1)

while not Programmer_1.is_lead():
    Programmer_1.work()

Programmer_1.info()


