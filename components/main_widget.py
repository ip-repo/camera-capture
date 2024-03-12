from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton,QLabel, QListWidget,QFileDialog, QStackedWidget, QListWidgetItem
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtMultimedia import QMediaCaptureSession, QImageCapture, QCamera
from PySide6.QtCore import  Qt, QDateTime
from PySide6.QtGui import QPixmap, QResizeEvent
from components.item_widget import ItemWidget
from components.funcs import resource_path

class MainWidget(QWidget):
    def __init__(self, camera_device=None) -> None:
        super().__init__()
        self.camera_device = camera_device
        self.images = {}
        self.init_ui()
        self.init_camera()

    def init_ui(self)  -> None:
        """ widget ui"""
        self.list_widget = QListWidget()
        self.list_widget.itemDoubleClicked.connect(self.item_double_clicked)
        self.video_widget = QVideoWidget()
        self.stack_widget = QStackedWidget()
        self.list_widget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.preview_label = QLabel()

        self.capture_btn = QPushButton()
        self.save_image_btn = QPushButton()
        self.save_image_btn.setIcon(QPixmap(resource_path("icons\\save.png")))
        self.capture_btn.setIcon(QPixmap(resource_path("icons\\capture_l.png")))
        self.capture_btn.setObjectName("capture")
        
        self.stack_widget.addWidget(self.video_widget)
        self.stack_widget.addWidget(self.preview_label)

        button_layout = QHBoxLayout()
        right_layout = QVBoxLayout()
        button_layout.addWidget(self.capture_btn, 1)
        button_layout.addWidget(self.save_image_btn, 1)
        right_layout.addLayout(button_layout)
        right_layout.addWidget(self.list_widget, 9)

        center_layout = QHBoxLayout()
        center_layout.addWidget(self.stack_widget, 8)
        center_layout.addLayout(right_layout, 3)

        self.setLayout(center_layout)
        self.capture_btn.clicked.connect(self.capture_image)
        self.save_image_btn.clicked.connect(self.save_image)
        

    def init_camera(self) -> None:
        """start camera, if there is no camera program will close """       
        self.capture_session = QMediaCaptureSession()
       
        self.camera = QCamera()
       
        self.camera.setCameraDevice(self.camera_device)
        self.capture_session.setCamera(self.camera)

        self.image_capture = QImageCapture()
        self.image_capture.imageCaptured.connect(self.new_image_captured)
        self.capture_session.setImageCapture(self.image_capture)
        self.capture_session.setVideoOutput(self.video_widget)
        self.camera.start()
    

    def capture_image(self) -> None:
        """ called when capture image is clicked"""
        if self.capture_btn.objectName() == "capture":
            self.image_capture.capture()
        else:
            self.stack_widget.setCurrentIndex(0) 
            self.capture_btn.setIcon(QPixmap(resource_path("icons\\capture_l.png")))
            self.capture_btn.setObjectName("capture")
    
    def new_image_captured(self, *captured) -> None:
        """ called when a new image is captured and then process the data"""
        date_time = QDateTime.currentDateTime().toString().split(' ')
        blank = ''
        for i in range(len(date_time)):
            if i == 3:
                temp = "_".join(date_time[i].split(':'))
                blank += temp + '_'
            else:
                blank += date_time[i] + '_'
        self.images[captured[0] - 1] = [captured[1] ,  str(QDateTime.currentDateTime().toPython()), blank+str(0)]
        print(self.images)
        self.init_list()

    def init_list(self):
        """ load images as items to list widget"""
        self.list_widget.clear()
        keys = sorted(self.images.keys())
        for key in  keys:
            print(key, self.images[key])
            item = QListWidgetItem()
            item_widget = ItemWidget()
           
            item_widget.init_ui(self.images[key][0],key - 1,self.images[key][-1])
            item.setSizeHint(self.list_widget.size() * 0.30)
            self.list_widget.addItem(item)
            self.list_widget.setItemWidget(item, item_widget)
    
    def resizeEvent(self, event: QResizeEvent) -> None:
        """on resize event make sure image preview will fit the window size"""
        if self.list_widget.count():
            if isinstance(self.stack_widget.currentWidget(), QLabel):
                if self.list_widget.selectedIndexes():
                    self.item_double_clicked(self.list_widget.currentItem())
        self.init_list()
                
    
    def item_double_clicked(self, *item_clicked) -> None:
        """ called when an item in list widget is double clicked and load the selected image"""
        self.capture_btn.setObjectName("camera")
        self.capture_btn.setIcon(QPixmap(resource_path("icons\\camera.png")))
        self.preview_label.clear()
        self.preview_label.setMaximumSize(self.stack_widget.size())
        item , = item_clicked
        index_for_images = self.list_widget.indexFromItem(item).row()
        
        pix = QPixmap(self.video_widget.width(),self.video_widget.height())
        pix = pix.fromImage(self.images[index_for_images][0])
        pix = pix.scaled(self.stack_widget.size(), Qt.AspectRatioMode.KeepAspectRatio)
        self.preview_label.setScaledContents(True)
        self.preview_label.setPixmap(pix)
        self.stack_widget.setCurrentWidget(self.preview_label)


    def save_image(self) -> None:
        """ called when save image clicked"""
        if self.list_widget.selectedIndexes():
            file_name, format = QFileDialog.getSaveFileName(caption="Save image",
                                dir= self.list_widget.itemWidget(self.list_widget.currentItem()).toolTip().rstrip()+".jpg", filter="Images (*.jpg *.png)")
            if file_name:
               for key in self.images.keys():
                   #print(self.images[key])
                   if self.images[key][-1] == self.list_widget.itemWidget(self.list_widget.currentItem()).toolTip():
                       self.images[key][0].save(self.list_widget.itemWidget(self.list_widget.currentItem()).toolTip().rstrip() + format.split("*")[-1][:-1])
        

     
    
    
