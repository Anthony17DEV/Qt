from conexao import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(386, 161)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_excluir = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_excluir.setObjectName("pushButton_excluir")
        self.pushButton_excluir.clicked.connect(self.excluir)
        self.gridLayout.addWidget(self.pushButton_excluir, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_codigo = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_codigo.setObjectName("lineEdit_codigo")
        self.gridLayout.addWidget(self.lineEdit_codigo, 0, 1, 1, 1)
        self.pushButton_2_abrir = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2_abrir.setObjectName("pushButton_2_abrir")
        self.pushButton_2_abrir.clicked.connect(self.abrir)
        self.gridLayout.addWidget(self.pushButton_2_abrir, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2_nome = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2_nome.setObjectName("lineEdit_2_nome")
        self.gridLayout.addWidget(self.lineEdit_2_nome, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Excluir"))
        self.pushButton_excluir.setText(_translate("MainWindow", "Excluir"))
        self.label.setText(_translate("MainWindow", "Código:"))
        self.pushButton_2_abrir.setText(_translate("MainWindow", "Abrir"))
        self.label_2.setText(_translate("MainWindow", "Nome:"))

    def abrir(self):
        codigo = self.lineEdit_codigo.text()
        sql = "SELECT * FROM cliente WHERE codigo =" + codigo
        cursor.execute(sql)
        dados = cursor.fetchall()
        qtd = len(dados)

        if qtd > 0:
            self.lineEdit_2_nome.setText(dados[0][1])
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Aviso")
            msg.setText("Código não encontrado.")
            msg.exec_()
            self.lineEdit_2_nome.setText("")


    def excluir(self):
        msg = QMessageBox()
        msg.setWindowTitle("Confirmação")
        msg.setIcon(QMessageBox.Question)
        msg.setText("Tem certeza que deseja excluir-lo?")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        resposta = msg.exec_()
        if resposta == QMessageBox.Ok:
            codigo = self.lineEdit_codigo.text()
            sql = "DELETE FROM cliente WHERE codigo =" + codigo
            cursor.execute(sql)
            conexao.commit()
            msg2 = QMessageBox()
            msg2.setWindowTitle("Confirmação")
            msg2.setText("Excluido com sucesso")
            msg2.exec_()
            self.lineEdit_2_nome.setText("")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
