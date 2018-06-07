# -*- coding: utf-8 -*-
import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWebEngineWidgets import *

class webengineDemo(QWidget):
    def __init__(self):
        super(webengineDemo, self).__init__()
        self.__ui__()

    def __ui__(self):
        self.setWindowTitle("WebEngine Demo")
        t_lay_parent = QVBoxLayout()
        t_lay_bottom = QHBoxLayout()
        t_lay_bottom.setSpacing(10)
        self.m_webengineView = QWebEngineView()
        self.m_editUrl = QLineEdit("https://xingkong.io")
        self.m_buttonGo = QPushButton("Go")
        self.m_buttonGo.connect(SIGNAL("clicked()"), self.slt_go)
        t_lay_bottom.addWidget(self.m_editUrl)
        t_lay_bottom.addWidget(self.m_buttonGo)
        t_lay_parent.addWidget(self.m_webengineView)
        t_lay_parent.addLayout(t_lay_bottom)
        self.setLayout(t_lay_parent)

    def slt_go(self):
        t_url = self.m_editUrl.text()
        if t_url.strip() != "":
            try:
                self.m_webengineView.load(t_url)
            except Exception, e:
                print unicode(e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    webengine = webengineDemo()
    webengine.show()
    sys.exit(app.exec_())
