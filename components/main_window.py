from PySide6.QtWidgets import QMainWindow
from components.main_widget import MainWidget
from PySide6.QtMultimedia import QCameraDevice

class MainWindow(QMainWindow):
    def __init__(self, camera_device: QCameraDevice) -> None:
        super().__init__()
        self.camera_device = camera_device
        self.main_widget = MainWidget(camera_device=camera_device)
        self.setCentralWidget(self.main_widget)
        
