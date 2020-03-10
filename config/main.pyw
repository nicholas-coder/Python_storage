import sys
from PyQt5.QtWidgets import *
from Config_GUI import *

data_chan = {"ВЧ": "01", "ВОЛС": "02", "МУЛЬТИПЛЕКСОР": "03", "ВЧ-ВОЛС": "04", "ВЧ-МУЛЬТИПЛЕКСОР": "05",
             "ВОЛС-МУЛЬТИПЛЕКСОР": "06"}
data_vect = {"ПРМ": "01", "ПРД": "02", "ПРМ/ПРД": "03"}
data_chan_type = {"ПРМ32Ф": "01", "ПРМ16В": "02", "ПРД32Ф": "03", "ПРД16В": "04", "ПРМ64Ф": "05", "ПРМ32В": "06",
                  "ПРД64Ф": "07", "ПРД32В": "08", "ПРМ32Ф/ПРД32Ф": "09", "ПРМ32В/ПРМ32В": "10"}

data_type_fiz_channel = {"100BASETX(\"ЦКК1\")": "01", "100BASEFX(\"ЦКК2\")": "02","RS-485(\"ЦКК1\")": "03",
                         "100BASETX(\"ЦКК1\")/100BASEFX(\"ЦКК1\")": "04",
                         "100BASETX(\"ЦКК1\")/100BASETX(\"ЦКК1\")": "05",
                         "100BASEFX(\"ЦКК1\")/100BASETX(\"ЦКК2\")": "06"}

data_protection_class = {"IP20": "01", "IP21": "02"}

data_LF = {"ЛФ1": "01", "ЛФ2": "02", "ЛФ3": "03", "ЛФ4": "04", "ЛФ5": "05", "ЛФ6": "06"}

data_SFS = {"без ТМ": "01", "с ТМ": "02"}

data_cks = {"Медь": "001", "Оптика": "002"}


def choise(val, dict):
    if val in dict:
        print(dict[val])


class MyWin(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.Config_Button.clicked.connect(self.get_param)

    def mbox(self, body, title='Error'):
        dialog = QMessageBox(QMessageBox.Information, title, body)
        dialog.exec_()

    def get_param(self):
        configuration = []
        val_1 = self.ui.comboBox.currentText()
        val_2 = self.ui.comboBox_2.currentText()
        val_3 = self.ui.comboBox_3.currentText()
        val_4 = self.ui.comboBox_4.currentText()
        val_5 = self.ui.comboBox_5.currentText()
        val_6 = self.ui.comboBox_6.currentText()
        val_7 = self.ui.comboBox_7.currentText()
        val_8 = self.ui.comboBox_8.currentText()
        chosen = [val_1, val_2, val_3, val_4, val_5, val_6, val_7, val_8]
        freq = self.ui.Freq_line.text()
        #print(chosen, freq)

        if freq != None and freq.isdigit():
            configuration = ["УНЦА.465129", data_chan[val_1], data_vect[val_2], data_chan_type[val_3],
                             data_type_fiz_channel[val_4],
                             data_protection_class[val_5], data_LF[val_6], "(" + freq + ")", data_SFS[val_7],
                             data_cks[val_8]]
            #print(configuration)
            conf = ((".").join(configuration[0:6]) + " - " + (".").join(configuration[6:]))
            self.ui.Config_number_line.clear()
            self.ui.Config_number_line.insert(conf)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
