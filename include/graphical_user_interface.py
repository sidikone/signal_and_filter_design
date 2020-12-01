import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):

    def __init__(self, title='my window', *args, **kwargs):

        self.window_title = title
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle(self.window_title)

        label = QLabel('this is awesome!!!')
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)


class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Second windows')


def main():
    app = QApplication(sys.argv)

    # gui = GUI()
    gui = MainWindow(title='Signal processing')
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
