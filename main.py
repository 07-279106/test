import PyQt5.QtWidgets,PyQt5.QtCore,PyQt5.QtGui
import widgets
from sys import argv
from sys import exit
app = PyQt5.QtWidgets.QApplication(argv)
class Img:
    def __init__(self,img):
        self.img = img
        self.moving = 0
        self.qt = PyQt5.QtWidgets.QLabel()
        self.qt.setAttribute(PyQt5.QtCore.Qt.WA_TranslucentBackground)
        self.qt.setWindowFlags(PyQt5.QtCore.Qt.FramelessWindowHint|PyQt5.QtCore.Qt.WindowStaysOnTopHint|PyQt5.QtCore.Qt.SplashScreen)
        self.qt.mousePressEvent = self.prs
        self.qt.mouseMoveEvent = self.mov
        self.qt.mouseReleaseEvent = self.rel
        self.qt.mouseDoubleClickEvent = self.dbl
        self.qt.closeEvent = self.reload
        self.loadImg()
        self.ui = UI()
    def loadImg(self):
        pm = PyQt5.QtGui.QPixmap(self.img)
        self.qt.setPixmap(pm)
        self.width,self.height = pm.width(),pm.height()
        self.qt.setScaledContents(1)
        self.qt.setGeometry(0,0,self.width,self.height)
        self.qt.show()
    def reload(self,e):
        self.__init__(self.img)
        self.loadImg()
    def prs(self,e):
        btn = e.button()
        if btn == 1:
            self.ui.update()
        elif btn == 2:
            self.moving = 1
    def mov(self,e):
        if self.moving:
            mX,mY = e.globalPos().x(),e.globalPos().y()
            self.qt.setGeometry(min(mX,data.scrW - self.width),min(mY,data.scrH - self.height),self.width,self.height)
    def rel(self,e):
        btn = e.button()
        if btn == 2:
            self.moving = 0
    def dbl(self,e):
        btn = e.button()
        if btn == 2:
            exit()
class UI:
    def __init__(self):
        self.load()
    def load(self):
        self.qt = PyQt5.QtWidgets.QWidget()
        self.qt.setWindowFlags(PyQt5.QtCore.Qt.FramelessWindowHint|PyQt5.QtCore.Qt.WindowStaysOnTopHint)
        vlayout = PyQt5.QtWidgets.QVBoxLayout()
        self.qt.setLayout(vlayout)
        lists = PyQt5.QtWidgets.QWidget()
        buttons = PyQt5.QtWidgets.QWidget()
        exitButton = PyQt5.QtWidgets.QPushButton("关闭")
        exitButton.clicked.connect(self.qt.hide)
        vlayout.addWidget(lists)
        vlayout.addWidget(buttons)
        vlayout.addWidget(exitButton)
        hlayout1 = PyQt5.QtWidgets.QHBoxLayout()
        lists.setLayout(hlayout1)
        self.list1 = PyQt5.QtWidgets.QListWidget()
        self.list2 = PyQt5.QtWidgets.QListWidget()
        hlayout1.addWidget(self.list1)
        hlayout1.addWidget(PyQt5.QtWidgets.QLabel("==》"))
        hlayout1.addWidget(self.list2)
        hlayout2 = PyQt5.QtWidgets.QHBoxLayout()
        buttons.setLayout(hlayout2)
        btn1 = PyQt5.QtWidgets.QPushButton("删除")
        btn2 = PyQt5.QtWidgets.QPushButton("添加/运行")
        btn1.clicked.connect(self.remove)
        btn2.clicked.connect(self.add)
        hlayout2.addWidget(btn1)
        hlayout2.addWidget(btn2)
        self.qt.closeEvent = self.reload
        self.list1.addItems(data.widgets[0])
        self.list2.addItems(data.modules.keys())
    def remove(self):
        index = self.list1.currentRow()
        if index < 0:
            return
        data.widgets[0].pop(index)
        data.widgets[1][index].destroy()
        data.widgets[1].pop(index)
        self.list1.takeItem(index)
        self.list1.setCurrentRow(-1)
    def add(self):
        self.qt.hide()
        index = self.list2.currentRow()
        if index < 0:
            return
        content = self.list2.currentItem().text()
        self.list2.setCurrentRow(-1)
        data.modules[content](data,PyQt5)
    def update(self):
        self.list1.clear()
        self.list1.addItems(data.widgets[0])
        self.qt.show()
    def reload(self,e):
        self.__init__()
        self.qt.show()
class Data:
    def __init__(self):
        self.modules = {}
        self.widgets = [[],[]]
        self.data = {}
        self.scrW,self.scrH = app.desktop().width(),app.desktop().height()
data = Data()
for name in widgets.__dir__():
    if name.startswith("_"):
        continue
    exec("widget = widgets.{}".format(name))
    data.modules[widget.Main.name] = widget.Main
main = Img("img.png")
app.exec()
