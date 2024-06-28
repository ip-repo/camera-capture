# camera-capture
This app allow user to choose the camera to use from the device and capture images with it and also to save them.
This app can be usefull when turning it to an exe file and that will allow users to use it on limited devices or systems (that can use exe files) as a camera capture application it can also be used on a micro pc, scb or even a microcontroller (with python).

![camera-capture](https://github.com/ip-repo/camera-capture/assets/123945379/a9088141-eee9-4c27-88af-ba16437db8f3)

### How to use
```console
python -m venv camera venv 
camera-venv\Scripts\activate
pip install PySide6 #6.6.2

git clone https://github.com/ip-repo/camera-capture.git
cd camera-capture
python main.py
```

If you wish to turn this python project into an exectuable you can use `pyinstaller` with the following commands
```console
pip install pyinstaller

pyinstaller --onefile -w --clean --add-data "style.qss:." --add-data "components:components" --add-data "icons:icons" --icon=capture.ico main.py
```
