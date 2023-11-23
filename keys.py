from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QPushButton, QHBoxLayout, QWidget, QMenu, QAction
from PyQt5.QtGui import QPixmap, QDesktopServices
from PyQt5.QtCore import Qt, QUrl
from default_window import WindowDetails #import default window settings
from layout import AddLayoutWindow, ViewLayoutTemplatesWindow # Import layout

#GUI Main window
class KeyboardUI(QMainWindow):
    def __init__(self):
        super(KeyboardUI, self).__init__()

        self.WindowDetails = None
        self.add_layout_window = None
        self.view_layout_templates_window = ViewLayoutTemplatesWindow()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('AirKeys') # window title
        self.setGeometry(100, 100, 1200, 800) # window size
        self.setStyleSheet("background-color: #222; color: #fff;") # window style sheet
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)


        header_label = QLabel(self)
        header_label.setText('AirKeys Logo') #  header, for intended logo
        header_label.setPixmap(QPixmap("AirLogo.png"))
        header_label.setAlignment(Qt.AlignCenter)

        nav_layout = QHBoxLayout()
        nav_layout.setSpacing(20) # spacing between labels and buttons

        menu_button = QPushButton('Menu', self)
        layout_button = QPushButton('Layout', self)
        guide_button = QPushButton('Guide', self)
        about_button = QPushButton('About Us', self)

        for btn in [menu_button, layout_button, guide_button, about_button]:
            btn.setStyleSheet(
                "padding: 10px; background-color: #2ecc71; color: white; font-size: 20px; border: none; border-radius: 5px;")

        nav_layout.addWidget(menu_button)
        nav_layout.addWidget(layout_button)
        nav_layout.addWidget(guide_button)
        nav_layout.addWidget(about_button)

        content_layout = QVBoxLayout()
        content_layout.addSpacing(150)

        # text label 
        text_label = QLabel(
            'Experience the effortless Airkeys Keyboard!', self)
        text_label.setStyleSheet('font-size: 20px; color: #ddd; margin-bottom: 20px;')

        # Create learn more button and adds style to button
        learn_more_button = QPushButton('Learn More', self)
        learn_more_button.setStyleSheet(
            'padding: 15px; background-color: #2ecc71; color: white; font-size: 20px; border: none; border-radius: 5px;')

        layouts_layout = QHBoxLayout()
        layouts_layout.setSpacing(20)
        layouts_menu = QMenu(self)

        # add action buttons to layout menu
        add_layout_action = QAction('Add Layout', self)
        view_layout_templates_action = QAction('View Layout Templates', self)

        # action triggers to display add layout window
        add_layout_action.triggered.connect(self.show_add_layout_window)

        # action triggers to display layout template window
        view_layout_templates_action.triggered.connect(self.show_view_layout_templates_window)

        layouts_menu.addAction(add_layout_action)
        layouts_menu.addAction(view_layout_templates_action)
        layouts_menu.setStyleSheet(
                "padding: 20px; background-color: #2ecc71; color: white; font-size: 20px; border: none; border-radius: 50px;")

        layout_button.setMenu(layouts_menu)

        # add contents of layoud window: text, widget and layout
        content_layout.addWidget(text_label)
        content_layout.addWidget(learn_more_button)
        content_layout.addLayout(layouts_layout)
        
        footer_label = QLabel('© 2023 AirKeys Keyboard', self)

        # center align label
        footer_label.setAlignment(Qt.AlignCenter)
        footer_label.setStyleSheet('margin-top: 20px; font-size: 14px; color: #ddd;')

        main_layout = QVBoxLayout(central_widget)
        main_layout.addWidget(header_label, alignment=Qt.AlignCenter)
        main_layout.addLayout(nav_layout)
        main_layout.addLayout(content_layout)
        main_layout.addWidget(footer_label, alignment=Qt.AlignCenter)

        # add window detail default for undeveloped windows
        learn_more_button.clicked.connect(self.show_window_details)
        menu_button.clicked.connect(lambda: self.open_window_details('Menu'))
        guide_button.clicked.connect(lambda: self.open_window_details('Guide'))
        
        # action to open url with button
        about_button.clicked.connect(self.open_about_us_url)
    
    # open website url as action for about us button
    def open_about_us_url(self):
        # Open the website URL when the 'About Us' button is clicked
        QDesktopServices.openUrl(QUrl("https://helloworldseniorproject.github.io"))

    # display contents of specified window 
    def show_window_details(self):
        if not self.WindowDetails or not self.WindowDetails.isVisible():
            self.WindowDetails = WindowDetails('Learn More')
            self.WindowDetails.show()

    # open specified window
    def open_window_details(self, window_name):
        if not self.WindowDetails or not self.WindowDetails.isVisible():
            self.WindowDetails = WindowDetails(window_name)
            self.WindowDetails.show()

    # display add layout window
    def show_add_layout_window(self):
        if not self.add_layout_window or not self.add_layout_window.isVisible():
            self.add_layout_window = AddLayoutWindow()
            self.add_layout_window.layout_added.connect(self.view_layout_templates_window.add_layout_template)  # Connect the signal
            self.add_layout_window.show()

    # display layout template window
    def show_view_layout_templates_window(self):
        if not self.view_layout_templates_window.isVisible():
            self.view_layout_templates_window.show()
