from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QFileDialog
from PyQt5.QtGui import QPixmap

class ImagePicker(QWidget):
    def __init__(self):
        super().__init__()

        self.button = QPushButton("Select Image")
        self.label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.button.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Image Files (*.png *.jpg *.bmp)")
        if filename:
            self.label.setPixmap(QPixmap(filename))

if __name__ == "__main__":
    app = QApplication([])
    window = ImagePicker()
    window.show()
    app.exec_()