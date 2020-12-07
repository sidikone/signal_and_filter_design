import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QLabel,
                             QHBoxLayout, QVBoxLayout, QButtonGroup, QCheckBox,
                             QPushButton, QLineEdit, QAction)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap


def _create_unit_button(name_in, obj_in):
    unit_but = QPushButton(text=name_in,
                           parent=obj_in)
    return unit_but


def _update_layout(layout_obj, widget_obj):
    layout_obj.addStretch()
    layout_obj.addWidget(widget_obj)
    layout_obj.addStretch()
    return None


# class MainWindow(QMainWindow):
#
#     def __init__(self, title='my window', *args, **kwargs):
#         self.window_title = title
#         super(MainWindow, self).__init__(*args, **kwargs)
#         self.setWindowTitle(self.window_title)
#
#         label = QLabel('this is awesome!!!')
#         label.setAlignment(Qt.AlignCenter)
#         self.setCentralWidget(label)
#
#
# class GUI(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle('Image viewer')
#         self.setGeometry(100, 100, 400, 400)
#         self.displayLabels()
#         # self.show()
#
#     def displayLabels(self):
#         text = QLabel(self)  # We create a QLabel object
#         text.setText('We tip a message')
#         text.move(105, 15)
#
#         image = "data/world.jpg"
#
#         try:
#             with open(image):
#                 world_image = QLabel(self)
#                 pixmap = QPixmap(image)
#                 world_image.setPixmap(pixmap)
#                 world_image.move(25, 40)
#         except FileNotFoundError:
#             print("Image not found.")
#
#
# class ButtonWindow(QWidget):
#
#     def __init__(self):
#         super().__init__()
#         self.initializeUI()
#
#     def initializeUI(self):
#         self.setGeometry(100, 100, 200, 200)
#         self.setWindowTitle('PushButton Widget')
#         self.displayButton()
#         self.show()
#
#     def displayButton(self):
#         name_label = QLabel(self)
#         name_label.setText("Don't push the button.")
#         name_label.move(60, 30)
#         button = QPushButton('Push me', self)
#         button.move(80, 70)
#         button.clicked.connect(self.buttonClicked)
#         # button.clicked(self.buttonClicked)
#
#     def buttonClicked(self):
#         self.close()
#
#
# class EntryWindow(QWidget):
#
#     def __init__(self):
#         super().__init__()
#         self.clear_button = QPushButton('Clear', self)
#         self.name_entry = QLineEdit(self)
#         self.initializeUI()
#
#     def initializeUI(self):
#         self.setGeometry(100, 100, 400, 200)
#         self.setWindowTitle('QLineEdit Widget')
#         self.displayWidgets()
#         self.show()
#
#     def displayWidgets(self):
#         QLabel("Please enter your name below.", self).move(100, 10)
#         name_label = QLabel("Name:", self)
#         name_label.move(70, 50)
#
#         self.name_entry.setAlignment(Qt.AlignLeft)
#         self.name_entry.move(130, 50)
#         self.name_entry.resize(200, 20)
#
#         self.clear_button.clicked.connect(self.clearEntries)
#         self.clear_button.move(160, 100)
#         return None
#
#     def clearEntries(self):
#         sender = self.sender()
#         if sender.text() == 'Clear':
#             self.name_entry.clear()
#         return None


class MainDisplay(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        # self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle('Signal generator & filterer')
        self.__create_layout(dtype='HBOX', spacing=10)



        # but_1 = self.__create_button(name='Mama', obj=self)
        # button_1 = QPushButton('Push Me', self)
        # self.createMenu()
        self.show()

    def __create_button(self, name, obj):
        unit_but = QPushButton(text=name,
                               parent=obj)
        return unit_but

    def __set_label(self, label, font='Arial', size=12):
        unit_label = QLabel(label)
        unit_label.setFont(QFont=QFont(font, size))
        return unit_label

    def __create_layout(self, dtype='VBOX', spacing=False):

        layout = None
        if dtype is 'VBOX':
            layout = QVBoxLayout()

        elif dtype is 'HBOX':
            layout = QVBoxLayout()

        if spacing is not False:
            layout.setSpacing(spacing)
        return layout

    def __update_layout(self, layout_obj, widget_obj):
        layout_obj.addStretch()
        layout_obj.addWidget(widget_obj)
        layout_obj.addStretch()
        return None
        # button_1 = QPushButton('Push Me', self)

    # def createMenu(self):
    #     exit_act = QAction('Exit', self)
    #     exit_act.setShortcut('Ctrl+Q')
    #     exit_act.triggered.connect(self.close)
    #
    #     menu_bar = self.menuBar()
    #     menu_bar.setNativeMenuBar(False)
    #
    #     file_menu = menu_bar.addMenu('File')
    #     file_menu.addAction(exit_act)
    #
    #     file_menu = menu_bar.addMenu('View')
    #
    #     file_menu = menu_bar.addMenu('Run')
    #
    #     file_menu = menu_bar.addMenu('Help')


def main():
    app = QApplication(sys.argv)
    gui = MainDisplay()
    # gui = MainWindow(title='Signal processing')
    # gui.show()

    # gui_2 = GUI()
    # gui_2.show()

    # gui_3 = ButtonWindow()
    # gui_4 = EntryWindow()
    # gui_5 = BasicMenu()
    # gui_5.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
