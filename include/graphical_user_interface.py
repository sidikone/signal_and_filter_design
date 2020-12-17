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


def set_label(label, font='Times New Roman', size=11):
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
                                    font: bold 24px Helvetica;
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

class CustomPushButton(QWidget):

    def __init__(self, name='&Click'):
        super().__init__()
        self.unit_button = QPushButton()
        self.__create_button(name=name)
        # print(self.unit_button)

    def __create_button(self, name):
        self.unit_button.setText(name)
        return None

    def customize_button(self, color='black', font='Arial', size=20, background_clr=None, active=False):

        border_style = "outset"
        border_width = 2.5
        border_radius = 2.5
        local_style = "color: " + color + ";"
        if background_clr is not None:
            local_style += "background-color: " + background_clr + ";"
        local_style += "border-style :" + border_style + ";"
        local_style += "border-width :" + str(border_width) + ";"
        local_style += "border-radius :" + str(border_radius) + ";"
        local_style += "font: " + str(size) + "px" + font + ";"
        local_style += "qproperty - alignment: AlignCenter" + ";"

        if active:
            self.unit_button.setStyleSheet(local_style)
        return None

    def get_button(self):
        return self.unit_button


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

    def __init__(self, shape=(2, 2), option="default"):
        super().__init__()
        (self.nb_rows, self.nb_cols) = shape
        self.option = option
        self.grid_layout = QGridLayout()
        self.__create_a_grid()

    def __create_a_grid(self):
        count = 0
        row_span, col_span = 1, 1
        for line in range(self.nb_rows):
            for col in range(self.nb_cols):
                if self.option is not "default":
                    obj_number = CustomTileLabel(text=str(count))
                    local_obj = obj_number.get_layout()
                else:
                    local_obj = QWidget()
                self.grid_layout.addWidget(local_obj, line, col, row_span, col_span)
                count += 1
        return None

    def get_layout(self):
        return self.grid_layout

    def set_unit_widget(self, widget_in, row, col):
        row_span, col_span = 1, 1
        self.grid_layout.addWidget(widget_in, row, col, row_span, col_span)
        return None

    def set_unit_layout(self, layout_in, row, col):
        row_span, col_span = 1, 1
        self.grid_layout.addLayout(layout_in, row, col, row_span, col_span)
        return None

    def set_multiple_widget(self, widget_in, row, col, row_span=1, col_span=1):
        self.grid_layout.addWidget(widget_in, row, col, row_span, col_span)
        return None


class CustomColor(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class CustomPushButtonBox(QWidget):

    def __init__(self, title="my_title", dtype="VBOX"):
        super().__init__()

        self.my_title = title
        self.my_layout = CustomLayout(dtype=dtype)
        self.__initializer()
        # self.my_layout = self.my_layout.get_layout()

    def __initializer(self):
        my_title = set_label(label=self.my_title)
        self.my_layout.update_layout(my_title)
        return None

    def add_button(self, name="my_button"):
        unit_button = CustomPushButton(name=name)
        self.my_layout.update_layout(unit_button.get_button())
        return None

    def get_layout(self):
        return self.my_layout.get_layout()


class MainDisplay(QMainWindow):

    def __init__(self):
        super().__init__()
        self.main_grid = None
        self.__initializeUI()

        self.__signal_generator_setup(False)
        self.__setup_example_1(False)
        self.__setup_example_2(True)

        self.__run_application()

    def __signal_generator_setup(self, display=True):
        """
        Signal generator bloc implementation
        :return: Vertical layout
        """
        signal_gen_box = CustomPushButtonBox(title="Signal generation")
        signal_gen_box.add_button(name="&Single signal")
        signal_gen_box.add_button(name="&Multiple signal")
        signal_gen_box.add_button(name="Set &noise")

        if display:
            self.__grid_layout_setup_for_layout(signal_gen_box.get_layout(), row=0, col=4)

        return None

    def __grid_layout_setup_for_layout(self, layout_in, row, col, row_span=1, col_span=1, dtype="default"):
        """
        Function used to set up a layout on the ain grid
        :param layout_in:
        :param row:
        :param col:
        :param row_span:
        :param col_span:
        :param dtype: change between a single layout or multiple size layout
        :return: None
        """
        if dtype is "default":
            self.main_grid.set_unit_layout(layout_in, row, col)

        else:
            self.main_grid.set_multiple_layout(layout_in, row, col, row_span, col_span)
        return None


    def __grid_layout_setup_for_widet(self, widget_in, row, col, row_span=1, col_span=1, dtype="default"):
        """
        Function used to set up a widget on the main grid
        :param widget_in:
        :param row:
        :param col:
        :param row_span:
        :param col_span:
        :param dtype: change between a single layout or multiple size layout
        :return: None
        """
        if dtype is "default":
            self.main_grid.set_unit_widget(widget_in, row, col)

        else:
            self.main_grid.set_multiple_widget(widget_in, row, col, row_span, col_span)
        return None

    def __setup_example_1(self, display=True):
        """
        Example of grid configuration
        :return: Vertical layout
        """
        layout_widget = CustomLayout(dtype='VBOX')
        but_1 = CustomPushButton(name='&Play')
        but_2 = CustomPushButton(name='&Stop')
        layout_widget.update_layout(widget_in=but_1.get_button())
        layout_widget.update_layout(widget_in=but_2.get_button())

        if display:
            self.__grid_layout_setup_for_layout(layout_widget.get_layout(), row=0, col=5)

        return None


    def __setup_example_2(self, display=True):
        """
        Example of grid configuration
        :return: Grid layout
        """
        blue_widget = CustomColor(color='skyblue')
        red_widget = CustomColor(color='magenta')
        salmon_widget = CustomColor(color='burlywood')
        aqua_widget = CustomColor(color='aquamarine')
        grey_light_widget = CustomColor(color='lightgrey')
        grey_widget = CustomColor(color='darkgrey')

        if display:
            self.__grid_layout_setup_for_widet(blue_widget, row=0, col=4)
            self.__grid_layout_setup_for_widet(red_widget, row=0, col=5)
            self.__grid_layout_setup_for_widet(salmon_widget, row=1, col=4)
            self.__grid_layout_setup_for_widet(aqua_widget, row=1, col=5)

            self.__grid_layout_setup_for_widet(aqua_widget, row=1, col=5)
            self.__grid_layout_setup_for_widet(grey_light_widget, row=0, col=0, row_span=3,
                                               col_span=4, dtype="multiple")
            self.__grid_layout_setup_for_widet(grey_widget, row=2, col=4, row_span=1,
                                               col_span=2, dtype="multiple")

        return None


    def __initializeUI(self):

        self.__init_main_window(geometry=True)
        self.main_grid = CustomGridLayout(shape=(3, 6))

        # vbox = QVBoxLayout()
        # # vbox.addStretch()

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

    def __run_application(self):
        widget = QWidget()
        widget.setLayout(self.main_grid.get_layout())
        self.__update_central_widget(widget_in=widget)
        return None

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
