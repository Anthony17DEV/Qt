from PyQt5 import QtCore, QtGui, QtWidgets

from conexao import *
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(540, 210)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 131, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 140, 47, 13))
        self.label_4.setObjectName("label_4")
        self.lineEdit_codigo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_codigo.setGeometry(QtCore.QRect(80, 60, 301, 20))
        self.lineEdit_codigo.setObjectName("lineEdit_codigo")
        self.lineEdit_nome = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nome.setGeometry(QtCore.QRect(80, 100, 301, 20))
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.lineEdit_telefone = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_telefone.setGeometry(QtCore.QRect(80, 140, 301, 20))
        self.lineEdit_telefone.setObjectName("lineEdit_telefone")
        self.pushButton_abrir = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_abrir.setGeometry(QtCore.QRect(400, 60, 75, 23))
        self.pushButton_abrir.setObjectName("pushButton_abrir")
        self.pushButton_abrir.clicked.connect(self.abrir)
        self.pushButton_cancelar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cancelar.setGeometry(QtCore.QRect(400, 100, 75, 23))
        self.pushButton_cancelar.setObjectName("pushButton_cancelar")
        self.pushButton_alterar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_alterar.setGeometry(QtCore.QRect(400, 140, 75, 23))
        self.pushButton_alterar.setObjectName("pushButton_alterar")
        self.pushButton_alterar.clicked.connect(self.alterar)
        self.pushButton_alterar.setEnabled(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Alterar cadastro"))
        self.label.setText(_translate("MainWindow", "ALTERAR CADASTRO"))
        self.label_2.setText(_translate("MainWindow", "C??DIGO"))
        self.label_3.setText(_translate("MainWindow", "NOME:"))
        self.label_4.setText(_translate("MainWindow", "TELEFONE:"))
        self.pushButton_abrir.setText(_translate("MainWindow", "Abrir"))
        self.pushButton_cancelar.setText(_translate("MainWindow", "Cancelar"))
        self.pushButton_alterar.setText(_translate("MainWindow", "Alterar"))

    def abrir(self):
        codigo = self.lineEdit_codigo.text()
        sql = "SELECT * FROM cliente WHERE codigo = " + codigo
        cursor.execute(sql)
        dados = cursor.fetchone()
        if dados == None :
            aviso = QMessageBox()
            aviso.setWindowTitle("Aviso")
            aviso.setText("Registro n??o encontrado.")
            aviso.exec_()

            self.lineEdit_nome.setText("")
            self.lineEdit_telefone.setText("")
        else :
            self.lineEdit_nome.setText(dados[1])
            self.lineEdit_telefone.setText(dados[2])
            self.lineEdit_codigo.setEnabled(False)
            self.pushButton_alterar.setEnabled(True)

    def alterar(self):
        codigo = self.lineEdit_codigo.text()
        nome = self.lineEdit_nome.text()
        telefone = self.lineEdit_telefone.text()

        sql = "UPDATE cliente SET nome = %s, fone = %s WHERE codigo = %s"

        cursor.execute(sql, (nome, telefone, codigo))
        conexao.commit()

        aviso = QMessageBox()
        aviso.setWindowTitle("Aviso")
        aviso.setText("Alterado com sucesso.")
        aviso.exec_()

        self.lineEdit_codigo.setEnabled(True)
        self.lineEdit_nome.setText("")
        self.lineEdit_telefone.setText("")
        self.pushButton_alterar.setEnabled(False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
