import sys

from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QTextCursor
from PyQt6.QtCore import QTimer


class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi("speed_test_ui.ui", self)

        # TIMER
        self.time_label = self.findChild(QtWidgets.QLabel, 'time_label')
        self.time_left = 60
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

        # START
        self.start_label = self.findChild(QtWidgets.QPushButton, "start_button")
        self.start_label.clicked.connect(self.start_button_activated)

        # TEXT_ENTRY
        self.text_entry = self.findChild(QtWidgets.QTextEdit, "text_entry")
        self.text_entry.textChanged.connect(self.scores)

        # TEXT_BROWSER
        # self.text_browser = (self.findChild(QtWidgets.QTextBrowser, "textBrowser")
        #                      .toMarkdown().replace(".", "").split())
        self.text_browser = self.findChild(QtWidgets.QTextBrowser, "textBrowser").toMarkdown().lower()



    def set_cursor_position(self):
        cursor = self.text_entry.textCursor()
        cursor.setPosition(0)
        self.text_entry.setTextCursor(cursor)
        self.text_entry.setFocus()

    def start_timer(self):
        self.timer.start(1000)

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.time_label.setText(f'{self.time_left:02d}')
        else:
            self.timer.stop()

    def start_button_activated(self):
        self.text_entry.clear()
        self.time_left = 61
        self.start_timer()
        QtWidgets.QApplication.processEvents()
        self.set_cursor_position()
        self.start_label.setText("Restart")

    def scores(self):

        # Source chars count
        src_chars = len(self.text_browser)
        # Source words in a list
        src_words = self.text_browser.replace(".", "").replace(",", "").split()

        words = self.text_entry.toPlainText().lower().split()
        chars = len(self.text_entry.toPlainText())
        score = 0

        for word in src_words:
            if word in words:
                print("Yes")
                score += 1

                self.your_wpm.setText(str(score))
                print(f"wpm: {score}")

                self.your_cpm.setText(str(chars))
                print(f"Chars: {chars}")

            else:
                print("no")



def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.setWindowTitle("Typing Speed Test")
    window.setFixedSize(600, 483)
    window.show()

    app.exec()


if __name__ == '__main__':
    main()
