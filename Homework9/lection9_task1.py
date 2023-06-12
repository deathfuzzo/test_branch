# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt
import re
from pathlib import Path

path_origin = Path("test_file", "task1_data.txt")  # описываем путь к исходному файлу task1_data.txt
path_convert = Path("test_file", "task1_answer.txt")  # описываем путь к изменённому файлу task1_answer.txt
origin = open(path_origin, mode='r', encoding='utf-8')  # задаём переменную открытия исходного файла на чтение
convert_create = open(path_convert, "w", encoding='utf-8')  #  создаём пустой task1_answer.txt, в который будем добавлять изменённые строки
for one_line in origin.readlines():  # пробегаем по списку строк циклом
    convert_add = open(path_convert, "a+", encoding='utf-8')  #  задаём переменную открытия изменённого файла в режиме дополнения
    one_line_nodig = re.sub(r"\d+", "", one_line)  # удаляем построчно цифры из текста
    convert_add.writelines(one_line_nodig)  # пишем изменённые строки без цифр в созданный файл task1_answer.txt
    convert_add.close()  # закрываем изменённый файл

# далее необязательный кусок кода для проверки получившегося изменённого файла
convert_read = open(path_convert, mode='r', encoding='utf-8') # задаём открытия изменённого файла на чтение
print(convert_read.read())  # вывод содержимого изменённого файла task1_answer.txt

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')