from PySide6.QtWidgets import QDialog,QLabel,QHBoxLayout,QComboBox,QPushButton
from PySide6.QtMultimedia import QMediaDevices
from PySide6.QtGui import QPixmap
from components.funcs import resource_path


class SettingsDialog(QDialog):
	"""
	This class is dialog that allow user do pick different values.
	"""
	def __init__(self, parent=None) -> None:
		super(SettingsDialog, self).__init__(parent)
		self.setWindowIcon(QPixmap(resource_path("icons\\capture_l.png")))
		self.setWindowTitle("Choose camera device")
		self.label = QLabel("Choose video input: ")
		self.ok_btn = QPushButton()
		self.ok_btn.clicked.connect(self.accept)
		self.ok_btn.setStyleSheet("QPushButton {qproperty-iconSize: 25px;}")
		self.ok_btn.setIcon(QPixmap(resource_path("icons\\ok.png")))
		self.box = QComboBox()
		
		layout = QHBoxLayout()
		layout.addWidget(self.label)
		layout.addWidget(self.box)
		layout.addWidget(self.ok_btn)
		self.setLayout(layout)
		self.data = {}
		self.check_for_devices()
	

	def check_for_devices(self):
		video_inputs_avilable = QMediaDevices.videoInputs()
		if video_inputs_avilable:
			items = []
			for video_input in video_inputs_avilable:
				print(video_input)
				self.data[video_input.description()] = video_input
				items.append(video_input.description())
			self.box.addItems(items)
			
		else:
			self.ok_btn.hide()
			self.box.hide()
			self.label.setText("Sorry did not found any camera devices.")
		
			
				
		
	def accept(self) -> None:
		self.camera_device = self.data[self.box.currentText()]
		self.done(25)
		
		
