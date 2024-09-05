import sys

from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QTimer


class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi("speed_test_ui.ui", self)

        self.time_label = self.findChild(QtWidgets.QLabel, 'time_label')

        self.time_left = 61
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)

        # BEST SCORE
        self.your_best_score = self.findChild(QtWidgets.QLabel, 'your_best_score')
        self.best_score = 0
        self.your_best_score.setText(str(self.best_score))

        # CPM
        self.your_cpm = self.findChild(QtWidgets.QLabel, 'CPM')
        self.cpm_score = 0
        self.your_cpm.setText(str(self.cpm_score))

        # WPM
        self.your_wpm = self.findChild(QtWidgets.QLabel, 'WPM')
        self.wpm_score = 0
        self.your_wpm.setText(str(self.wpm_score))

        # RESTART
        self.restart_label = self.findChild(QtWidgets.QPushButton, "restart_button")
        self.restart_label.clicked.connect(self.restart)

        # START
        self.start_label = self.findChild(QtWidgets.QPushButton, "start_button")
        self.start_label.clicked.connect(self.start_button_activated)

        # TEXT_ENTRY
        self.text_entry = self.findChild(QtWidgets.QTextEdit, "text_entry")
        self.text_entry.textChanged.connect(self.your_best)



    def start_timer(self):
        self.timer.start(1000)


    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.time_label.setText(f'{self.time_left:02d}')
        else:
            self.timer.stop()

    def restart(self):
        self.text_entry.clear()
        self.time_left = 60


    def start_button_activated(self):
        self.start_timer()


    def your_best(self):
        text = []
        text = self.text_entry.toPlainText().split()
        print(len(text))

    def wpm(self):
        pass

    def cpm(self):
        pass




def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.setWindowTitle("Typing speed test")
    window.setFixedSize(600, 483)
    window.show()

    app.exec()


if __name__ == '__main__':
    main()
