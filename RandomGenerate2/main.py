import sys
import random
from PyQt5.QtWidgets import *


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.lineEdit1 = QLineEdit()
        self.textEdit2 = QTextEdit()

        lbl0 = QLabel("Cases:")
        lbl1 = QLabel("Output")
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()

        lbl_cb = QLabel("Choose:")
        self.cb = QComboBox()
        self.cb.addItems(["Remove Duplicate"])
        self.cb.addItem("Original")
        # self.cb.currentIndexChanged.connect(self.cb_changed)
        hbox1.addWidget(lbl_cb)
        hbox1.addWidget(self.cb)

        btn1 = QPushButton("OK")
        btn1.clicked.connect(self.button_clicked)

        hbox2.addWidget(lbl0)
        hbox2.addWidget(self.lineEdit1)
        hbox2.addWidget(btn1)

        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(lbl1)
        vbox.addWidget(self.textEdit2)

        self.setLayout(vbox)
        self.resize(250, 150)
        self.center()

        self.setWindowTitle('Text Edit')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def button_clicked(self):
        n = int(self.lineEdit1.text())
        lst = ''
        for i in range(n):
            a = random.randint(0, 10)
            text = str(a)
            self.textEdit2.append(text)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())