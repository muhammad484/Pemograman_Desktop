import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *

class MainWindow(QWidget):

    def __init__(self):
        # super(MainWindow,self).__init__() #jika menggunakan PySide 2/6 tidak menggunakan ini 
        QWidget.__init__(self)
        self.setWindowTitle("Horizontal Layout")
        self.setGeometry(350,250,900,200)
        self.SetLayoutH()
        # self.setLayoutV()
        # self.setLayoutG()
        # self.setLayoutF()
        # self.show()

    def SetLayoutH(self):
        horizontalLayout = QHBoxLayout(self)
        hButton1 = QPushButton("Button 1",self)
        hButton2 = QPushButton("Button 2",self)
        hButton3 = QPushButton("Button 3",self)
        hButton4 = QPushButton("Button 4",self)

        horizontalLayout.addWidget(hButton1)
        horizontalLayout.addWidget(hButton2)
        horizontalLayout.addWidget(hButton3)
        horizontalLayout.addWidget(hButton4)

        # self.SetLayoutH(horizontalLayout)

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainwindow = MainWindow()
        mainwindow.show()
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error : ",sys.exc_info()[1])
    except SystemExit:
        print("closing window...")
    except Exception:
        print(sys.exc_info()[1])