import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from conexao import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(414, 355)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBox_manha = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_manha.setChecked(True)
        self.checkBox_manha.setObjectName("checkBox_manha")
        self.horizontalLayout_3.addWidget(self.checkBox_manha)
        self.checkBox_tarde = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_tarde.setObjectName("checkBox_tarde")
        self.horizontalLayout_3.addWidget(self.checkBox_tarde)
        self.checkBox_noite = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_noite.setObjectName("checkBox_noite")
        self.horizontalLayout_3.addWidget(self.checkBox_noite)
        self.gridLayout.addLayout(self.horizontalLayout_3, 13, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_salvar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_salvar.setObjectName("pushButton_salvar")
        self.horizontalLayout_4.addWidget(self.pushButton_salvar)
        self.pushButton_salvar.clicked.connect(self.salvar)
        self.pushButton_cancelar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cancelar.setObjectName("pushButton_cancelar")
        self.pushButton_cancelar.clicked.connect(self.cancelar)
        self.horizontalLayout_4.addWidget(self.pushButton_cancelar)
        self.gridLayout.addLayout(self.horizontalLayout_4, 14, 0, 1, 1)
        self.dateEdit_nasc = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_nasc.setCalendarPopup(True)
        self.dateEdit_nasc.setObjectName("dateEdit_nasc")
        self.gridLayout.addWidget(self.dateEdit_nasc, 3, 0, 1, 1)
        self.comboBox_curso = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_curso.setObjectName("comboBox_curso")
        self.comboBox_curso.addItem("")
        self.comboBox_curso.addItem("")
        self.comboBox_curso.addItem("")
        self.comboBox_curso.addItem("")
        self.comboBox_curso.addItem("")
        self.gridLayout.addWidget(self.comboBox_curso, 9, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.lineEdit_nome = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.gridLayout.addWidget(self.lineEdit_nome, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 8, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 12, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_masc = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_masc.setChecked(True)
        self.radioButton_masc.setObjectName("radioButton_masc")
        self.horizontalLayout_2.addWidget(self.radioButton_masc)
        self.radioButton_fem = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_fem.setObjectName("radioButton_fem")
        self.horizontalLayout_2.addWidget(self.radioButton_fem)
        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit_nome, self.dateEdit_nasc)
        MainWindow.setTabOrder(self.dateEdit_nasc, self.radioButton_masc)
        MainWindow.setTabOrder(self.radioButton_masc, self.radioButton_fem)
        MainWindow.setTabOrder(self.radioButton_fem, self.comboBox_curso)
        MainWindow.setTabOrder(self.comboBox_curso, self.checkBox_manha)
        MainWindow.setTabOrder(self.checkBox_manha, self.checkBox_tarde)
        MainWindow.setTabOrder(self.checkBox_tarde, self.checkBox_noite)
        MainWindow.setTabOrder(self.checkBox_noite, self.pushButton_salvar)
        MainWindow.setTabOrder(self.pushButton_salvar, self.pushButton_cancelar)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cadastro de alunos"))
        self.label_5.setText(_translate("MainWindow", "Sexo:"))
        self.checkBox_manha.setText(_translate("MainWindow", "Matutino"))
        self.checkBox_tarde.setText(_translate("MainWindow", "Vespertino"))
        self.checkBox_noite.setText(_translate("MainWindow", "Notuno"))
        self.pushButton_salvar.setText(_translate("MainWindow", "Salvar"))
        self.pushButton_cancelar.setText(_translate("MainWindow", "Cancelar"))
        self.comboBox_curso.setItemText(0, _translate("MainWindow", "Informática"))
        self.comboBox_curso.setItemText(1, _translate("MainWindow", "Edificações"))
        self.comboBox_curso.setItemText(2, _translate("MainWindow", "Eletrotécnica"))
        self.comboBox_curso.setItemText(3, _translate("MainWindow", "Matemática"))
        self.comboBox_curso.setItemText(4, _translate("MainWindow", "Mecânica"))
        self.label.setText(_translate("MainWindow", "Nome:"))
        self.label_2.setText(_translate("MainWindow", "Data Nasc.:"))
        self.label_3.setText(_translate("MainWindow", "Curso:"))
        self.label_4.setText(_translate("MainWindow", "Turno:"))
        self.radioButton_masc.setText(_translate("MainWindow", "Masculino"))
        self.radioButton_fem.setText(_translate("MainWindow", "Feminino"))

    def salvar(self):
        nome = self.lineEdit_nome.text()

        nasc = self.dateEdit_nasc.text()
        nasc = datetime.datetime.strptime(nasc, "%d/%m/%Y").strftime("%Y-%m-%d")

        sexo = ""
        if self.radioButton_masc.isChecked():
            sexo = "Masculino"
        else:
            sexo = "Feminino"

        curso = self.comboBox_curso.currentText()

        turno = ""
        if self.checkBox_manha.isChecked():
            turno += "Manhã "
        if self.checkBox_tarde.isChecked():
            turno += "Tarde "
        if self.checkBox_noite.isChecked():
            turno += "Noite"

        sql = "INSERT INTO aluno VALUES(null, %s, %s, %s, %s, %s)"
        cursor.execute(sql,(nome,nasc,curso,sexo,turno))
        conexao.commit()

        msg = QMessageBox()
        msg.setText("Gravado com sucesso")
        msg.exec_()

        self.lineEdit_nome.setText("")
        self.dateEdit_nasc.setDate(QtCore.QDate(2000, 1, 1))
        self.radioButton_masc.setChecked(True)
        self.comboBox_curso.setCurrentIndex(0)
        self.checkBox_manha.setChecked(False)
        self.checkBox_tarde.setChecked(False)
        self.checkBox_noite.setChecked(False)

    def cancelar(self):
        self.lineEdit_nome.setText("")
        self.dateEdit_nasc.setDate(QtCore.QDate(2000, 1, 1))
        self.radioButton_masc.setChecked(True)
        self.comboBox_curso.setCurrentIndex(0)
        self.checkBox_manha.setChecked(False)
        self.checkBox_tarde.setChecked(False)
        self.checkBox_noite.setChecked(False)
        sys.exit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
