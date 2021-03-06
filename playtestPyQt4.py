import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(300, 300, 1000, 600)
        self.setWindowTitle("PyQt4 practice")
        self.setWindowIcon(QtGui.QIcon('python_image.png'))

        extractAction = QtGui.QAction("&Exit", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave The App')
        extractAction.triggered.connect(self.close_application)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)
        

        self.home()

    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(10,110)

        extractAction = QtGui.QAction(QtGui.QIcon('grass.png'), 'Exit', self)
        extractAction.triggered.connect(self.close_application)
        
        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)

        checkBox = QtGui.QCheckBox('Shrink Window', self)
        checkBox.move(150, 50)
        checkBox.stateChanged.connect(self.enlarge_window)

        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(200, 180, 300, 30)

        self.btn = QtGui.QPushButton("Download",self)
        self.btn.move(200,230)
        self.btn.clicked.connect(self.download)

        self.styleChoice = QtGui.QLabel('Style', self)

        comboBox = QtGui.QComboBox(self)
        comboBox.addItem("motif")
        comboBox.addItem("Windows")
        comboBox.addItem("cde")
        comboBox.addItem("Plastique")
        comboBox.addItem("Cleanlooks")
        comboBox.addItem("windowsvista")

        comboBox.move(10,230)
        self.styleChoice.move(10,180)
        comboBox.activated[str].connect(self.style_choice)

        self.show()


    def style_choice(self, text):
        self.styleChoice.setText(text)
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))
        

    def download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)
            

    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(300,300,2000,1200)
        else:
            self.setGeometry(300,300,1000,600)
        

    def close_application(self):
        choice = QtGui.QMessageBox.question(self, 'Extract!',
                                            "Get into the chopper?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            print("Extracting Naaaaaaoooww!!!!")
            sys.exit()
        else:
            pass
        
        
def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()
