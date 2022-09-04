import sys

from PyQt5 import QtWidgets, QtCore,QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from PyUi3.FWidgets import FTitleBar, FToggleButton, FAccentButton, FHomeStack, FShowCase, FWindow, FPage

class home_page(FPage):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.installEventFilter(self)
        layout = QVBoxLayout(self)
        txt=QLabel(text="Windows 11 PyUi3")
        txt.setMaximumSize(1000000,40)
        txt.setAlignment(Qt.AlignCenter)
        frm=QFrame()
        btn=QPushButton("Start",parent)
        btn.setMaximumSize(120, 31)
        layout.addWidget(txt)
        layout.addWidget(btn)
        self.setLayout(layout)
    def eventFilter(self, obj, event):
        if event.type() == QEvent.Resize:
            self.setGeometry(0,0,self.width(),self.height())

        return super(home_page, self).eventFilter(obj, event)





class Window(FWindow):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.resize(700,700)
        self.setTitleBar(FTitleBar(self.main))
        self.windowEffect.setMicaEffect(self.winId(), True)
        self.installEventFilter(self)

        self.stack = FHomeStack(self.main)
        self.homepage = home_page()
        self.sidebar = QFrame(self.main)
        self.btn = QPushButton("btn", self)

        self.buttonpage = FPage(self.main)

        toggle = QSlider(Qt.Orientation.Horizontal, self.buttonpage)
        toggle.setFixedSize(111,31)
        self.buttonshowcase = FShowCase(title="Toggle Button",widget=toggle,min_size=QSize(130,50),parent=self.buttonpage)

        self.stack.addWidget(self.homepage)
        self.stack.addWidget(self.buttonpage)


    def eventFilter(self, obj, event):
        if event.type() == QEvent.Resize:


            if self.width() > 807:
                self.sidebar.setGeometry(0,48, 291, self.height()-48)
                self.stack.setGeometry(291, 48, self.width()-291, self.height()-48)

            else:
                self.sidebar.setGeometry(0,48, 0, self.height()-48)
                self.stack.setGeometry(0, 48, self.width(), self.height()-48)

            self.buttonshowcase.setGeometry(20,20, self.main.width()-40, 100)
            self.homepage.setGeometry(0,0,self.main.width(),self.main.height())

        return super(Window, self).eventFilter(obj, event)


if __name__ == "__main__":
    # enable dpi scale
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    # run app
    app = QApplication(sys.argv)
    demo = Window()
    demo.show()
    sys.exit(app.exec_())