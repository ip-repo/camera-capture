from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel
from PySide6.QtGui import QPixmap

class ItemWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
    def init_ui(self, image,index, time_stamp=None) -> None:
        """
        Args:
            image : image captured 
            index : image index
            time_stamp : timestap to name image
        """
        self.setToolTip(time_stamp)
        self.index = index
        self.h_layout = QHBoxLayout()
        self.preview_label = QLabel()
        self.preview_label.setScaledContents(True)
        self.preview_label.setPixmap(QPixmap.fromImage(image))
        self.h_layout.addWidget(self.preview_label)
        self.setLayout(self.h_layout)
