from PyQt5 import QtCore, QtGui, QtWidgets
from conexao import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(347, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_nome = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.gridLayout.addWidget(self.lineEdit_nome, 0, 1, 1, 1)
        self.pushButton_pesquisar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_pesquisar.setObjectName("pushButton_pesquisar")
        self.pushButton_pesquisar.clicked.connect(self.pesquisar)
        self.gridLayout.addWidget(self.pushButton_pesquisar, 1, 1, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pesquisar"))
        self.label.setText(_translate("MainWindow", "Nome:"))
        self.pushButton_pesquisar.setText(_translate("MainWindow", "Pesquisar"))

    def pesquisar(self):
        nome = self.lineEdit_nome.text()
        sql = "SELECT * FROM cliente WHERE nome LIKE %s"
        cursor.execute(sql, ("%" + nome + "%",))
        dados = cursor.fetchall()
        qtd = len(dados)

        resultado = ""

        if qtd > 0:
            for linha in dados:
                resultado += "Código: " + str(linha[0]) + "\n"
                resultado += "Nome: " + linha[1] + "\n"
                resultado += "Telefone: " + linha[2] + "\n"
                resultado += "=======================================\n"
        resultado += str(qtd) + " Registro(s) encontrado(s)."
        self.textEdit.setPlainText(resultado)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
