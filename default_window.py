from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt

# Presaved window details for undeveloped windows
class WindowDetails(QWidget):
    def __init__(self, window_name):
        super(WindowDetails, self).__init__()

        self.init_ui(window_name)

    def init_ui(self, window_name):
        self.setWindowTitle(f'{window_name} Details') # Window title
        self.setGeometry(200, 200, 600, 400) # Window Size

        layout = QVBoxLayout()
        
        # creates a default window with a default text message
        details_label = QLabel(f'{window_name} details go here...', self)
        details_label.setStyleSheet('font-size: 18px; color: #333;')

        close_button = QPushButton('Close', self)
        close_button.setStyleSheet(
            'background-color: #e74c3c; color: white; font-size: 16px; padding: 10px; border-radius: 5px;')
        close_button.clicked.connect(self.close)

        layout.addWidget(details_label, alignment=Qt.AlignCenter)
        layout.addWidget(close_button, alignment=Qt.AlignCenter)

        self.setLayout(layout)
