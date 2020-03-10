import os
import datetime
import utility_files
import tempfile


def Path(number, name):
    default = "C:\\Users\\" + os.environ.get("USERNAME") + "\\Desktop\\"
    way = default + number + ")" + name + "\\" + number + ")" + name
    return way


def CreateFolder(data):
    destination = data + "_inc"
    destination1 = data + "_scr"
    print('Созданы папки по следующему пути: ')
    print(destination)
    print(destination1)
    os.makedirs(destination)
    os.makedirs(destination1)
    return destination, destination1


def MakeFiles(source_code, dest, exp):
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
        file1 = open(way + exp + dest.lower() + est[ground:point] + est[point:point + 2], 'w')
        mas1[3] = mas[3]
        mas1[3] += now.strftime(" %d.%m.%Y ")
        for i in mas1:
            file1.write(i)
            file1.write("\n")
        file1.close()


def Choice(param, codec, codeh, codecext, codehext, n, m):
    if param == "yes" or param == "y":
        codec.append(codecext[n])
        codeh.append(codehext[m])
        return codec, codeh
    elif param == "no" or param == "n":
        return codec, codeh


def AddToSource(source_codec, source_codeh):
    folders = {"gpio": [1, 2], "spi": [3, 1], "adc": [0, 0], "uart": [5, 3], "tim": [4, 4], "it": [2, 5]}
    for index in folders:
        par = input("Добавить " + index + "? Y/N:   ").lower()
        values = folders.get(index)
        cn = values[0]
        cm = values[1]
        Choice(par, source_code_c, source_code_h, source_code_c_ext, source_code_h_ext, cn, cm)
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
way = Path(number, place)
CreateFolder(way)
inc = '_inc\\'
scr = '_scr\\'
cfil, hfil = AddToSource(source_code_c, source_code_h, )
MakeFiles(hfil, place, inc)
MakeFiles(cfil, place, scr)