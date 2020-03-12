import os
import datetime
import utility_files
import tempfile

def get_path(number, name):
    """Функция возвращает путь, по которому будут созданы папки с именем и номером, которые задает пользователь"""
    default = ("{0}" + os.environ.get("USERNAME") + "{1}").format("C:\\Users\\", "\\Desktop\\")
    direction = (default + number + "{0}" + name + "{1}" + number + "{2}" + name).format(")", "\\", ")")
    return direction


def create_folder(data):
    """Функция создает папки. Аргументом функции является путь."""
    destination = data + "_inc"
    destination1 = data + "_scr"
    print('Созданы папки по следующему пути: ')
    print(destination)
    print(destination1)
    os.makedirs(destination)
    os.makedirs(destination1)
    return destination, destination1


def make_files(source_code, dest, exp):
    """Функция генерирует файлы, заменяет шаблонное имя на имя, выбранное пользователем"""
    for objects in source_code:
        mas = objects
        now = datetime.datetime.today()
        path = os.getcwd()
        mas1 = []
        for element in mas:
            element = element.replace("new_utility", dest.lower())
            element = element.replace("NEW_UTILITY", dest.upper())
            mas1.append(element)
        est = objects[2]
        ground = est.rfind("_")
        point = est.rfind(".")
        file1 = open(direct + exp + dest.lower() + est[ground:point] + est[point:point + 2], 'w')
        mas1[3] = mas[3]
        """Ставим дату"""
        mas1[3] += now.strftime(" %d.%m.%Y ")
        for i in mas1:
            file1.write(i)
            file1.write("\n")
        file1.close()


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
    for index in folders:
        par = input("Добавить " + index + "? Y/N:   ").lower()
        values = folders.get(index)
        cn = values[0]
        cm = values[1]
        choice_files(par, source_code_c, source_code_h, source_code_c_ext, source_code_h_ext, cn, cm)
    return source_codec, source_codeh


source_code_h = [utility_files.def_h, utility_files.main_h, utility_files.state_h, utility_files.init_h,
                 utility_files.sett_h]
source_code_h_ext = [utility_files.adc_h, utility_files.spi_h, utility_files.gpio_h,
                     utility_files.uart_h, utility_files.tim_h, utility_files.it_h]

source_code_c = [utility_files.main_c, utility_files.init_c]
source_code_c_ext = [utility_files.adc_c, utility_files.gpio_c, utility_files.it_c, utility_files.spi_c,
                     utility_files.tim_c, utility_files.uart_c]

place = input("введите имя: ")
number = input("Введите номер: ")
direct = get_path(number, place)
create_folder(direct)
inc = '_inc\\'
scr = '_scr\\'
cfil, hfil = add_to_source(source_code_c, source_code_h)
make_files(hfil, place, inc)
make_files(cfil, place, scr)
