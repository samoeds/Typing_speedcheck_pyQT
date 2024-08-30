import sys
from PyQt6 import QtWidgets, uic


class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi("speed_test_ui.ui", self)



def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.setWindowTitle("Typing speed test")
    window.setFixedSize(600, 447)
    window.show()
    app.exec()


if __name__ == '__main__':
    main()