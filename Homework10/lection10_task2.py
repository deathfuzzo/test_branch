# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

# print(all_division(100,1,2,3,4,5,6))

@pytest.mark.smoke
def test_smoke():
    assert all_division(6, 2) == 3

@pytest.mark.acceptance
def test_min_zero1():
    assert all_division(0, 1) == 0

@pytest.mark.acceptance
def test_zero2():
    with pytest.raises(ZeroDivisionError):
        all_division(1, 0)

@pytest.mark.acceptance
def test_wrong_type():
    with pytest.raises(TypeError):
        all_division("1", 1)

@pytest.mark.production
def test_many_args():
    assert all_division(1021020, 2, 3, 5, 7, 11, 13, 17) == 2





