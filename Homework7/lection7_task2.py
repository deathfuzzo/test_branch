# Напишите класс PersonInfo
# Экземпляр класса создается из следующих атрибутов:
# 1. Строка - "Имя Фамилия"
# 2. Число - возраст сотрудника
# 3. Подразделения от головного до того, где работает сотрудник.
# Реализуйте методы класса:
# 1. short_name, который возвращает строку Фамилия И.
# 2. path_deps, возвращает путь "Головное подразделение --> ... --> Конечное подразделение"
# 3. new_salary, Директор решил проиндексировать зарплаты, и новая зарпалата теперь вычисляет по формуле:
# 1337*Возраст*суммарное кол-во вхождений трех наиболее часто встречающихся букв из списка подразделений
# (регистр имеет значение "А" и "а" - разные буквы)
# Например (Ввод --> Вывод) :
# PersonInfo('Александр Шленский',
#            32,
#            'Разработка', 'УК', 'Автотесты').short_name() --> 'Шленский А.'
# PersonInfo('Александр Шленский',
#            32,
#            'Разработка', 'УК', 'Автотесты').path_deps() -->
#            'Разработка --> УК --> Автотесты'
# PersonInfo('Александр Шленский', 32, 'Разработка', 'УК', 'Автотесты').new_salary() --> 385056 т.к.
# т.к. буква "т" встречается 4 раза, "а" 3 раза, 'о' 2 раза, остальные по одной. Сумма трёх самых частых букв 4+3+2 = 9.
# 1337*32*9 = 385056

class PersonInfo:

    def __init__(self, name, age, department1, department2="", department3="", department4=""): # инициализация объектов класса PersonInfo по имени, возрасту, узлам подразделений
        self.name = name
        self.age = age
        self.department1 = department1
        self.department2 = department2
        self.department3 = department3
        self.department4 = department4

    def short_name(self):  # функция форматирования фамилии/имени
        return (
                self.name.split(' ')[1] + " " + self.name[0].split(' ')[0] + "."  #  сплитом режем фамилию/имя на 2 части, переворачиваем, у имени берём первый символ имени + точка
        )

    def path_deps(self):  # функция создания путей подразделений
        if self.department4 != "":  # через проверку с конца наличия подразделений сращиваем в путь подразделения
            return (
                    self.department1 + " --> " + self.department2 + " --> " + self.department3 + " --> " + self.department4
            )
        elif self.department4 == "" and self.department3 != "":
            return (
                    self.department1 + " --> " + self.department2 + " --> " + self.department3
            )
        elif self.department3 == "" and self.department2 != "":
            return (
                    self.department1 + " --> " + self.department2
            )
        else:
            return self.department1

    def new_salary(self):  # функция вычисления новой зарплаты
        lst = self.department1 + self.department2 + self.department3 + self.department4  # сращиваем подразделения в список
        dict_frequency = ([(lst.count(i), i) for i in lst])  # создаем словарь вхождений символов из срощенного списка
        top3 = (sorted(set(dict_frequency))[::-1][:3])  # сортируем словарь по топ3 максимального количества вхождений
        sum_top3 = top3[0][0] + top3[1][0] + top3[2][0]  # суммируем ключи (макс кол-во вхождений) из словаря топ3
        return 1337 * self.age * sum_top3  #  функция возвращает вычисление по формуле: 1337*Возраст*суммарное кол-во вхождений трех наиболее часто встречающихся букв

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


first_person = PersonInfo('Александр Шленский', 32, 'Разработка', 'УК', 'Автотесты')
fourth_person = PersonInfo('Иван Иванов', 26, 'Разработка')
second_person = PersonInfo('Пётр Валерьев', 47, 'Разработка', 'УК')
third_person = PersonInfo('Макар Артуров', 51, 'Разработка', 'УК', 'Нефункциональное тестирование', 'Автотестирование')

data = [first_person.short_name,
        second_person.short_name,
        third_person.short_name,
        fourth_person.short_name,

        first_person.path_deps,
        second_person.path_deps,
        third_person.path_deps,
        fourth_person.path_deps,

        first_person.new_salary,
        second_person.new_salary,
        third_person.new_salary,
        fourth_person.new_salary
        ]


test_data = ['Шленский А.', 'Валерьев П.', 'Артуров М.', 'Иванов И.',

             'Разработка --> УК --> Автотесты',
             'Разработка --> УК',
             'Разработка --> УК --> Нефункциональное тестирование --> Автотестирование',
             'Разработка',
             385056, 314195, 1227366, 173810]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')