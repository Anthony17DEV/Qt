from PyQt5 import QtCore, QtGui, QtWidgets
from conexao import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(343, 509)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.botao_listar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_listar.setObjectName("botao_listar")
        self.botao_listar.clicked.connect(self.listagem)
        self.verticalLayout.addWidget(self.botao_listar)
        self.textEdit_listagem = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_listagem.setObjectName("textEdit_listagem")
        self.verticalLayout.addWidget(self.textEdit_listagem)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Listagem de clientes"))
        self.botao_listar.setText(_translate("MainWindow", "Listar"))

    def listagem(self):
        sql = "SELECT * FROM cliente"
        cursor.execute(sql)
        dados = cursor.fetchall()
        qtd = len(dados)
        resultado = ""
        for linha in dados:
            resultado += "Código: " + str(linha[0]) + "\n"
            resultado += "Nome: " + linha[1] + "\n"
            resultado += "Telefone: " + linha[2] + "\n"
            resultado += "=======================================\n"
        resultado += str(qtd) + "Registro(s) encontrado(s)."
        self.textEdit_listagem.setPlainText(resultado)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
