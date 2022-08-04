from PyQt5 import QtCore, QtGui, QtWidgets

import mysql.connector

conexao = mysql.connector.connect(host="localhost" ,user="root" ,password="", database="banco1")

cursor = conexao.cursor()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(270, 135)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.EditNome = QtWidgets.QLineEdit(self.centralwidget)
        self.EditNome.setObjectName("EditNome")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.EditNome)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.EditFone = QtWidgets.QLineEdit(self.centralwidget)
        self.EditFone.setObjectName("EditFone")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.EditFone)
        self.ButtonSalvar = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonSalvar.setObjectName("ButtonSalvar")
        self.ButtonSalvar.clicked.connect(self.salvar)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.ButtonSalvar)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "CADASTRO DE CLIENTE"))
        self.label_2.setText(_translate("MainWindow", "NOME"))
        self.label_3.setText(_translate("MainWindow", "TELEFONE"))
        self.ButtonSalvar.setText(_translate("MainWindow", "Salvar"))

    def salvar(self):
        nome = self.EditNome.text()
        fone = self.EditFone.text()
        sql = "INSERT INTO cliente VALUES(null, %s, %s)"
        cursor.execute(sql, (nome, fone))
        conexao.commit()
        print("Inserido com sucesso")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
