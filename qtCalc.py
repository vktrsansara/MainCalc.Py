from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(252, 222)
        MainWindow.setMinimumSize(QtCore.QSize(252, 222))
        MainWindow.setMaximumSize(QtCore.QSize(252, 222))
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Button_7 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_7.setGeometry(QtCore.QRect(10, 100, 51, 23))
        self.Button_7.setObjectName("Button_7")
        self.Button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_4.setGeometry(QtCore.QRect(10, 130, 51, 23))
        self.Button_4.setObjectName("Button_4")
        self.Button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_1.setGeometry(QtCore.QRect(10, 160, 51, 23))
        self.Button_1.setObjectName("Button_1")
        self.Button_Comma = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Comma.setGeometry(QtCore.QRect(10, 190, 51, 23))
        self.Button_Comma.setObjectName("Button_Comma")
        self.Button_C = QtWidgets.QPushButton(self.centralwidget)
        self.Button_C.setGeometry(QtCore.QRect(10, 70, 51, 23))
        self.Button_C.setObjectName("Button_C")
        self.Button_8 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_8.setGeometry(QtCore.QRect(70, 100, 51, 23))
        self.Button_8.setObjectName("Button_8")
        self.Button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_5.setGeometry(QtCore.QRect(70, 130, 51, 23))
        self.Button_5.setObjectName("Button_5")
        self.Button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_2.setGeometry(QtCore.QRect(70, 160, 51, 23))
        self.Button_2.setObjectName("Button_2")
        self.Button_0 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_0.setGeometry(QtCore.QRect(70, 190, 51, 23))
        self.Button_0.setObjectName("Button_0")
        self.Button_BracketOut = QtWidgets.QPushButton(self.centralwidget)
        self.Button_BracketOut.setGeometry(QtCore.QRect(190, 190, 51, 23))
        self.Button_BracketOut.setObjectName("Button_Per")
        self.Button_DEL = QtWidgets.QPushButton(self.centralwidget)
        self.Button_DEL.setGeometry(QtCore.QRect(70, 70, 51, 23))
        self.Button_DEL.setObjectName("Button_DEL")
        self.Button_9 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_9.setGeometry(QtCore.QRect(130, 100, 51, 23))
        self.Button_9.setObjectName("Button_9")
        self.Button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_6.setGeometry(QtCore.QRect(130, 130, 51, 23))
        self.Button_6.setObjectName("Button_6")
        self.Button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_3.setGeometry(QtCore.QRect(130, 160, 51, 23))
        self.Button_3.setObjectName("Button_3")
        self.Button_BracketIn = QtWidgets.QPushButton(self.centralwidget)
        self.Button_BracketIn.setGeometry(QtCore.QRect(130, 190, 51, 23))
        self.Button_BracketIn.setObjectName("Button_PM")
        self.Button_Div = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Div.setGeometry(QtCore.QRect(190, 160, 51, 23))
        self.Button_Div.setObjectName("Button_Div")
        self.Button_Equity = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Equity.setGeometry(QtCore.QRect(130, 70, 51, 23))
        self.Button_Equity.setObjectName("Button_Equity")
        self.Button_Plus = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Plus.setGeometry(QtCore.QRect(190, 70, 51, 23))
        self.Button_Plus.setObjectName("Button_Plus")
        self.Button_Minus = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Minus.setGeometry(QtCore.QRect(190, 100, 51, 23))
        self.Button_Minus.setObjectName("Button_Minus")
        self.Button_Mult = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Mult.setGeometry(QtCore.QRect(190, 130, 51, 23))
        self.Button_Mult.setObjectName("Button_Mult")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 231, 51))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("border: 1px solid black;    /* Параметры границы */\n"
                                 "background: #ffffff;    /* Цвет фона */\n"
                                 "letter-spacing: 2px;      /* Расстояние между буквами */\n"
                                 "color:#008080;    /* Цвет текста */\n"
                                 "font-size: 12pt;    /* Размер шрифта в пунктах */")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainCalc.Py"))
        self.Button_1.setText(_translate("MainWindow", "1"))  # Выводим текст на кнопки
        self.Button_1.clicked.connect(self.activNumOne)  # Регистрируем нажатие на кнопку и выполняем функцию
        self.Button_2.setText(_translate("MainWindow", "2"))
        self.Button_2.clicked.connect(self.activNumTwo)
        self.Button_3.setText(_translate("MainWindow", "3"))
        self.Button_3.clicked.connect(self.activNumThree)
        self.Button_4.setText(_translate("MainWindow", "4"))
        self.Button_4.clicked.connect(self.activNumFour)
        self.Button_5.setText(_translate("MainWindow", "5"))
        self.Button_5.clicked.connect(self.activNumFive)
        self.Button_6.setText(_translate("MainWindow", "6"))
        self.Button_6.clicked.connect(self.activNumSix)
        self.Button_7.setText(_translate("MainWindow", "7"))
        self.Button_7.clicked.connect(self.activNumSeven)
        self.Button_8.setText(_translate("MainWindow", "8"))
        self.Button_8.clicked.connect(self.activNumEight)
        self.Button_9.setText(_translate("MainWindow", "9"))
        self.Button_9.clicked.connect(self.activNumNine)
        self.Button_0.setText(_translate("MainWindow", "0"))
        self.Button_0.clicked.connect(self.activNumNull)
        self.Button_C.setText(_translate("MainWindow", "C"))
        self.Button_C.clicked.connect(self.activClear)
        self.Button_DEL.setText(_translate("MainWindow", "DEL"))
        self.Button_DEL.clicked.connect(self.activDel)
        self.Button_Comma.setText(_translate("MainWindow", ","))
        self.Button_Comma.clicked.connect(self.activComma)
        self.Button_Plus.setText(_translate("MainWindow", "+"))
        self.Button_Plus.clicked.connect(self.activPlus)
        self.Button_Minus.setText(_translate("MainWindow", "-"))
        self.Button_Minus.clicked.connect(self.activMinus)
        self.Button_Mult.setText(_translate("MainWindow", "*"))
        self.Button_Mult.clicked.connect(self.activMult)
        self.Button_Div.setText(_translate("MainWindow", "/"))
        self.Button_Div.clicked.connect(self.activDiv)
        self.Button_BracketOut.setText(_translate("MainWindow", ")"))
        self.Button_BracketOut.clicked.connect(self.activBracketOut)
        self.Button_BracketIn.setText(_translate("MainWindow", "("))
        self.Button_BracketIn.clicked.connect(self.activBracketIn)
        self.Button_Equity.setText(_translate("MainWindow", "="))
        self.Button_Equity.clicked.connect(self.activEquity)

    def activNumOne(self):
        var = self.label.text()
        self.label.setText(var + "1")

    def activNumTwo(self):
        var = self.label.text()
        self.label.setText(var + "2")

    def activNumThree(self):
        var = self.label.text()
        self.label.setText(var + "3")

    def activNumFour(self):
        var = self.label.text()
        self.label.setText(var + "4")

    def activNumFive(self):
        var = self.label.text()
        self.label.setText(var + "5")

    def activNumSix(self):
        var = self.label.text()
        self.label.setText(var + "6")

    def activNumSeven(self):
        var = self.label.text()
        self.label.setText(var + "7")

    def activNumEight(self):
        var = self.label.text()
        self.label.setText(var + "8")

    def activNumNine(self):
        var = self.label.text()
        self.label.setText(var + "9")

    def activNumNull(self):
        var = self.label.text()
        self.label.setText(var + "0")

    def activClear(self):
        self.label.setText("")

    def activDel(self):
        var = self.label.text()
        self.label.setText(var[:len(var) - 1])

    def activComma(self):
        var = self.label.text()
        self.label.setText(var + ".")

    def activPlus(self):
        var = self.label.text()
        self.label.setText(var + "+")

    def activMinus(self):
        var = self.label.text()
        self.label.setText(var + "-")

    def activMult(self):
        var = self.label.text()
        self.label.setText(var + "*")

    def activDiv(self):
        var = self.label.text()
        self.label.setText(var + "/")

    def activBracketIn(self):
        var = self.label.text()
        self.label.setText(var + "(")

    def activBracketOut(self):
        var = self.label.text()
        self.label.setText(var + ")")

    def activEquity(self):
        equity = self.label.text()
        try:
            colcVal = eval(equity)
            self.label.setText(str(colcVal))
        except:
            self.label.setText("Error")
