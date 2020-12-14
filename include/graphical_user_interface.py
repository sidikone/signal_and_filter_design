import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QMenuBar, QStatusBar, QWidget, )
from PyQt5.QtWidgets import (QLabel, QHBoxLayout, QVBoxLayout, QGridLayout, )
from PyQt5.QtWidgets import (QButtonGroup, QCheckBox, QPushButton, QLineEdit, QAction)

from PyQt5.QtGui import (QColor, QPalette, QFont)
from PyQt5.QtCore import (QRect, Qt)
from PyQt5.QtGui import QPixmap


def _update_layout(layout_obj, widget_obj):
    layout_obj.addStretch()
    layout_obj.addWidget(widget_obj)
    layout_obj.addStretch()
    return None


def set_label(label, font='Arial', size=12):
    unit_label = QLabel(label)
    unit_label.setAlignment(Qt.AlignCenter)
    unit_label.setFont(QFont(font, size))
    return unit_label


class CustomTileLabel:
    def __init__(self, text='text'):
        self.label = QLabel(text=text)
        self.__style_sheet()

    def __style_sheet(self):
        self.label.setStyleSheet("""background-color: skyblue;
                                    color: white;
                                    border-style: outset;
                                    border-width: 2.5px;
                                    border-radius: 5px;
                                    font: bold 24px 'Book Antiqua';
                                    qproperty-alignment: AlignCenter""")

        return None

    def get_layout(self):
        return self.label


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

class CustomLayout(QWidget):

    def __init__(self, dtype='VBOX'):
        super().__init__()
        self.layout = None
        self.__create_layout(dtype=dtype)

    def __create_layout(self, dtype, spacing=False):

        if dtype is 'VBOX':
            self.layout = QVBoxLayout()

        elif dtype is 'HBOX':
            self.layout = QHBoxLayout()

        if spacing is not False:
            self.layout.setSpacing(spacing)
        return None

    def update_layout(self, widget_in):
        self.layout.addWidget(widget_in)

    def get_layout(self):
        return self.layout


class CustomGridLayout(QWidget):

    def __init__(self, shape=(2, 2)):
        super().__init__()

        (self.nb_rows, self.nb_cols) = shape
        self.grid_layout = QGridLayout()
        self.__create_a_grid()

    def __create_a_grid(self):
        count = 0
        for line in range(self.nb_rows):
            for col in range(self.nb_cols):
                obj_number = CustomTileLabel(text=str(count))
                obj_number = obj_number.get_layout()
                self.grid_layout.addWidget(obj_number, line, col)
                count += 1
        return None

    def get_layout(self):
        return self.grid_layout


class CustomColor(QWidget):

    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


# class CustomPushButton(QWidget):
#
#     def __init__(self, name='button_name', color='None'):
#         super().__init__()
#         self.__create_button(name=name)
#
#     def __create_button(self, name):
#         unit_but = QPushButton(text=name,
#                                parent=self)
#         return unit_but

# def _create_unit_button(name_in, obj_in):
#     unit_but = QPushButton(text=name_in,
#                            parent=obj_in)
#     return unit_but


class MainDisplay(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):

        self.__init_main_window(geometry=True)

        # -------------------------------------
        mama = CustomGridLayout(shape=(2, 6))
        # mama = CustomTileLabel()

        # --------------------------------------
        red_widget = CustomColor(color='red')
        green_widget = CustomColor(color='green')
        blue_widget = CustomColor(color='blue')
        grey_widget = CustomColor(color='grey')

        # self.__update_central_widget(red_widget)

        layout_widget = CustomLayout(dtype='HBOX')
        layout_widget.update_layout(widget_in=red_widget)
        layout_widget.update_layout(widget_in=green_widget)
        layout_widget.update_layout(widget_in=blue_widget)
        layout_widget.update_layout(widget_in=grey_widget)

        widget = QWidget()
        #        widget.setLayout(layout_widget.get_layout())
        widget.setLayout(mama.get_layout())
        self.__update_central_widget(widget_in=widget)
        # self.setGeometry(100, 100, 400, 200)
        # self.setWindowTitle('Signal generator & filterer')
        #
        # self.__set_menu_bar(x_0=0, y_0=0, width=300, height=15)
        # self.__set_status_bar()
        # self.__set_central_widget()

        #
        # q1 = QPushButton('Abou')
        # q2 = QPushButton('Sidik')
        #
        # # vbox = QVBoxLayout()
        # hbox = QHBoxLayout()
        # vbox = QVBoxLayout()
        # # vbox.addStretch()
        #
        # vbox.addWidget(q1)
        # vbox.addWidget(q2)
        #
        # hbox.addLayout(vbox)
        # opt = QWidget()
        # vbox = self.QVBoxLayout()
        # for i1 in range(2):
        #     hbox = QHBoxLayout()
        #     hbox.setContentsMargins(0, 0, 0, 0)
        #     hbox.addStretch()
        #
        #     for i2 in range(2):
        #         bb = QPushButton(str(i2))
        #         hbox.addWidget(bb)
        #     vbox.addLayout(hbox)

        # my_layout = self.__create_layout(dtype='VBOX', spacing=100)
        # self.__update_layout(layout_obj=my_layout,
        #                      widget_obj=self.__create_button(name='Papa'))
        # self.__update_layout(layout_obj=my_layout,
        #                      widget_obj=self.__create_button(name='mama'))
        # my_layout.addStretch()

        # self.__create_button(name="but1", obj=my_layout)

        # self.__update_layout(layout_obj=my_layout,
        #                      widget_obj=QPushButton('Push Me', self))
        # self.__update_layout(layout_obj=my_layout,
        #                      widget_obj=QPushButton('Push Me again', self))

        # but_1 = self.__create_button(name='Mama')
        # button_1 = QPushButton('Push Me', self)
        # self.createMenu()
        # self.show()

    def __init_main_window(self, geometry=False):
        """
        Initialise the main window
        :param geometry: bool - Allows to fix the size of the window
        :return: None
        """
        if geometry:
            self.setGeometry(100, 100, 600, 400)  # define a fixed size of the window
        self.setWindowTitle('Signal generator & filterer')

        self.__set_menu_bar(x_0=0, y_0=0, width=300, height=15)
        self.__set_status_bar()
        return None

    def __set_menu_bar(self, x_0, y_0, width, height):
        """
        MenuBar definition
        :param x_0: int
        :param y_0: int
        :param width: int
        :param height: int
        :return: None
        """

        my_menu_bar = QMenuBar(self)
        my_menu_bar.setGeometry(QRect(x_0, y_0, width, height))
        self.setMenuBar(my_menu_bar)
        return None

    def __set_status_bar(self, apply=True):
        """
        SetBar definition
        :param apply: bool
        :return: None
        """

        if apply:
            my_status_bar = QStatusBar(self)
            self.setStatusBar(my_status_bar)
        return None

    def __update_central_widget(self, widget_in):
        """
        Update central widget with 'widget_in' object
        :param widget_in: Widget object
        :return: None
        """
        self.setCentralWidget(widget_in)
        return None

    def show_main_window(self, max_view_size=False, apply=True):
        """
        Allow you to set the main window in full screen mode
        :param max_view_size: bool
        :param apply: bool
        :return: None
        """
        if apply:
            if max_view_size is True:
                self.showMaximized()
            else:
                self.show()

    # @staticmethod
    # def __create_layout(dtype='VBOX', spacing=False):
    #
    #     layout = None
    #     if dtype is 'VBOX':
    #         layout = QVBoxLayout()
    #
    #     elif dtype is 'HBOX':
    #         layout = QHBoxLayout()
    #
    #     if spacing is not False:
    #         layout.setSpacing(spacing)
    #     return layout
    #
    # @staticmethod
    # def __update_layout(layout_obj, widget_obj):
    #     layout_obj.addStretch()
    #     layout_obj.addWidget(widget_obj)
    #     layout_obj.addStretch()
    #     return None
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
    gui.show_main_window(max_view_size=True)
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
