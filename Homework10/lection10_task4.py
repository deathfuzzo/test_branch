# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.


import time


class Test:
    def test1(self):
        time.sleep(1)
        assert 1 + 2 == 3

    def test2(self):
        assert 3 + 4 == 7
        time.sleep(1)

    def test3(self, print_time_process):
        assert 5 + 6 == 11
        time.sleep(3)
