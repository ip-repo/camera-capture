from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QPixmap
from components.main_window import MainWindow
from components.funcs import resource_path
from components.device_dialog import SettingsDialog

if __name__ == '__main__':
	app = QApplication([])
	with open(resource_path("style.qss"), "r") as style_file:
		app.setStyleSheet(style_file.read())
	dialog = SettingsDialog()
	result  = SettingsDialog.exec(dialog)
	if result == 25:
		window = MainWindow(dialog.camera_device)
		available_geometry = window.screen().availableGeometry()
		window.setGeometry(0,0,available_geometry.width() *0.75 , available_geometry.height())
		window.setWindowIcon(QPixmap(resource_path("icons\\capture_l.png")))
		window.setWindowTitle("Capture Camera")
		
		window.show()
		app.exec()
