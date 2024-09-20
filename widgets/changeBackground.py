import os


class Main:
    name = "更换背景"
    def __init__(self,data,Qt):
        self.data = data
        self.Qt = Qt
        self.getArgsQt()
    def getArgsQt(self):
        self.getArgs_qt = self.Qt.QtWidgets.QWidget()
        self.getArgs_qt.setWindowFlags(self.Qt.QtCore.Qt.WindowMinMaxButtonsHint|self.Qt.QtCore.Qt.WindowStaysOnTopHint)
        self.getArgs_qt.setWindowTitle("参数设置")
        vlayout = self.Qt.QtWidgets.QVBoxLayout()
        self.getArgs_qt.setLayout(vlayout)
        vlayout.addWidget(self.Qt.QtWidgets.QLabel("图片路径："))
        entry = self.Qt.QtWidgets.QLineEdit()
        vlayout.addWidget(entry)
        buttons = self.Qt.QtWidgets.QWidget()
        vlayout.addWidget(buttons)
        hlayout = self.Qt.QtWidgets.QHBoxLayout()
        buttons.setLayout(hlayout)
        lB = self.Qt.QtWidgets.QPushButton("取消")
        lB.clicked.connect(self.delQt)
        hlayout.addWidget(lB)
        rB = self.Qt.QtWidgets.QPushButton("继续")
        rB.clicked.connect(lambda:self.loadQt(entry.text()))
        hlayout.addWidget(rB)
        self.getArgs_qt.show()
        self.getArgs_qt.closeEvent = lambda e:self.getArgsQt()
    def loadQt(self,img):
        self.getArgs_qt.destroy()
        self.img = img
        if not os.path.isfile(self.img):
            return
        self.data.data["bg"] = self.img
        self.pm = self.Qt.QtGui.QPixmap(self.img).scaled(self.data.scrW,self.data.scrH)
        self.data.bg = self.Qt.QtWidgets.QLabel()
        self.data.bg.setGeometry(0,0,self.data.scrW,self.data.scrH)
        self.data.bg.setWindowFlags(self.Qt.QtCore.Qt.FramelessWindowHint|self.Qt.QtCore.Qt.WindowStaysOnBottomHint|self.Qt.QtCore.Qt.SplashScreen)
        self.data.bg.setAttribute(self.Qt.QtCore.Qt.WA_TranslucentBackground)
        self.data.bg.setPixmap(self.pm)
        self.data.bg.show()
    def delQt(self):
        self.getArgs_qt.destroy()
