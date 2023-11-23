from PyQt5.QtWidgets import QLabel, QVBoxLayout, QPushButton, QWidget, QLineEdit, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, pyqtSignal 

# Creates Layout window
class AddLayoutWindow(QWidget):
    layout_added = pyqtSignal(dict)  # Signal to notify the addition of a layout

    def __init__(self):
        super(AddLayoutWindow, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Add Layout') # Window title
        self.setGeometry(300, 300, 400, 200) # window size

        layout = QVBoxLayout() # set window layout

        # Crates label to save layout name
        name_label = QLabel('Layout Name:', self)
        self.name_edit = QLineEdit(self)

        # Insert Layout from device
        image_label = QLabel('Select Image:', self)
        self.image_path = None
        self.image_label = QLabel(self)

        # create browse button
        browse_button = QPushButton('Browse', self)
        browse_button.clicked.connect(self.browse_image) # action when clicked

        add_button = QPushButton('Add Layout', self)
        add_button.clicked.connect(self.add_layout) # action when clicked

        layout.addWidget(name_label)
        layout.addWidget(self.name_edit)
        layout.addWidget(image_label)
        layout.addWidget(self.image_label)
        layout.addWidget(browse_button)
        layout.addWidget(add_button, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    # Using QFileDialog package to browse for files on device
    def browse_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.bmp *.jpeg *.gif)", options=options)
        if file_name:
            self.image_path = file_name
            pixmap = QPixmap(file_name)
            self.image_label.setPixmap(pixmap.scaledToHeight(100))
    
    # Saves layout in layout templates
    def add_layout(self):
        layout_name = self.name_edit.text()
        # condition for adding layout image
        if layout_name and self.image_path:
            print(f'Layout Name: {layout_name}, Image Path: {self.image_path}')
            layout_template = {'name': layout_name, 'image_path': self.image_path}
            self.layout_added.emit(layout_template)  # Emit the signal
            self.close()

# Layout template class, to view all layout templates
class ViewLayoutTemplatesWindow(QWidget):
    def __init__(self):
        super(ViewLayoutTemplatesWindow, self).__init__()

        self.layout_templates = []

        self.init_ui()

    def init_ui(self):
        
        self.setWindowTitle('View Layout Templates') #window title
        self.setGeometry(300, 300, 400, 200) # window size

        self.layout = QVBoxLayout()

        self.templates_label = QLabel('Layout templates go here...', self)
        self.templates_label.setStyleSheet('font-size: 18px; color: #333;')

        self.layout.addWidget(self.templates_label, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)

    # add new layout template
    def add_layout_template(self, layout_template):
        self.layout_templates.append(layout_template)
        self.update_templates_label()

    # updates layout template when new layout has been added
    def update_templates_label(self):
        template_text = ""
        for template in self.layout_templates:
            layout_name = template['name']
            image_path = template['image_path']
            template_text += f"Name: {layout_name}\n"
            template_text += f"Image Path: {image_path}\n\n"

            # Load and display the layout image
            pixmap = QPixmap(image_path)
            image_label = QLabel(self)
            image_label.setPixmap(pixmap.scaledToHeight(100))
            self.layout.addWidget(image_label, alignment=Qt.AlignCenter)

        self.templates_label.setText(template_text)
