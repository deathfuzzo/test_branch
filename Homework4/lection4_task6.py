# Напишите функцию, которая принимает кортеж num_tuple из 10 цифр num_tuple,
# и возвращает строку этих чисел в виде номера телефона str_phone.
# Например (Ввод --> Вывод) :
# (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)  => "(123) 456-7890"

def create_phone_number(num_tuple):
    tel_code, tel_first_part, tel_second_part = "", "", ""  # создаем строчные переменные под каждую часть тел. номера
    for x in num_tuple[0:3]:  # циклом пробегаем первый срез кортежа с кодом оператора
        tel_code += str(num_tuple[x - 1])  # записываем каждую из цифр среза в переменную tel_code
    for y in num_tuple[3:6]:  # по аналогии с первым циклом
        tel_first_part += str(num_tuple[y - 1])
    for z in num_tuple[6:10]:  # по аналогии с первым циклом
        tel_second_part += str(num_tuple[z - 1])
    str_phone = "(" + tel_code + ") " + tel_first_part + "-" + tel_second_part -  # из полученных частей составляем требуемую маску телефона
    return str_phone

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [
    (1, 2, 3, 4, 5, 6, 7, 8, 9, 0),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (0, 2, 3, 0, 5, 6, 0, 8, 9, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
]

test_data = [
    "(123) 456-7890", "(111) 111-1111", "(023) 056-0890", "(000) 000-0000"
]


for i, d in enumerate(data):
    assert create_phone_number(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')