import os
import datetime
import utility_files


def get_path(number, name):
    """Функция возвращает путь, по которому будут созданы папки с именем и номером, которые задает пользователь"""
    default = ("{0}" + os.environ.get("USERNAME") + "{1}").format("C:\\Users\\", "\\Desktop\\")
    direction = (default + number + '{bracket}' + name + \
                 '{backslash}' + number + '{bracket}' + name).format(bracket=")", backslash="\\")
    return direction


def create_folder(data):
    """Функция создает папки. Аргументом функции является путь."""
    destination = data + "_inc"
    destination1 = data + "_scr"
    print('Созданы папки по следующему пути: \n', destination + '\n', destination1 + '\n')
    os.makedirs(destination)
    os.makedirs(destination1)
    return destination, destination1


def make_files(source_code, dest, exp):
    """Функция генерирует файлы, заменяет шаблонное имя на имя пользователя"""
    for line in source_code:
        now = datetime.datetime.today()
        reduced_obj = []

        for element in line:
            element = element.replace("new_utility", dest.lower()).replace("NEW_UTILITY", dest.upper())
            reduced_obj.append(element)

        symbols = line[2]
        ground = symbols.rfind("_")
        point = symbols.rfind(".")
        template_file = open(direct + exp + dest.lower() + symbols[ground:point] + symbols[point:point + 2], 'w')
        reduced_obj[3] = line[3]

        """Ставим дату"""
        reduced_obj[3] += now.strftime(" %d.%m.%Y ")

        for line in reduced_obj:
            template_file.write(line)
            template_file.write("\n")
        template_file.close()


def choice_files(param, codec, codeh, codecext, codehext, n, m):
    """Функция добавляет выбранные файлы"""
    if param == "yes" or param == "y":
        codec.append(codecext[n])
        codeh.append(codehext[m])

        return codec, codeh
    elif param == "no" or param == "n":
        return codec, codeh


def add_to_source(source_codec, source_codeh):
    """Функция выбора создания файлов, которые идут не по умолчанию"""
    folders = {"gpio": [1, 2], "spi": [3, 1], "adc": [0, 0], "uart": [5, 3], "tim": [4, 4], "it": [2, 5]}
    print("Добавить папки из списка: gpio, spi, adc, uart, tim, it")
    for index in folders:
        par = input("Добавить " + index + "? Y/N:   ").lower()
        values = folders.get(index)
        c_code = values[0]
        h_code = values[1]
        choice_files(par, source_code_c, source_code_h, source_code_c_ext, source_code_h_ext, c_code, h_code)
    return source_codec, source_codeh


source_code_h = [
    utility_files.def_h,
    utility_files.main_h,
    utility_files.state_h,
    utility_files.init_h,
    utility_files.sett_h
]

source_code_h_ext = [
    utility_files.adc_h,
    utility_files.spi_h,
    utility_files.gpio_h,
    utility_files.uart_h,
    utility_files.tim_h,
    utility_files.it_h
]

source_code_c = [utility_files.main_c, utility_files.init_c]

source_code_c_ext = [
    utility_files.adc_c,
    utility_files.gpio_c,
    utility_files.it_c,
    utility_files.spi_c,
    utility_files.tim_c,
    utility_files.uart_c
]

place = input("введите имя: ")

if not place.isalpha():
    raise ValueError("Имя должно состоять из букв!")

number = input("Введите номер: ")

if not number.isdigit():
    raise ValueError("Номер должен быть целочисленным значением!")

direct = get_path(number, place)
create_folder(direct)

inc = '_inc\\'
scr = '_scr\\'

c_file, h_file = add_to_source(source_code_c, source_code_h)
make_files(h_file, place, inc)
make_files(c_file, place, scr)
