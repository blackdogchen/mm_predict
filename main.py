from PySide2.QtWidgets import QApplication,QFileDialog
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from PySide2.QtGui import QPixmap

from predicter import Predicter

class Predict():
    def __init__(self):
        file = QFile("D:/Shetuan/mmdetection-master/UI/main.ui")
        file.open(QFile.ReadOnly)
        file.close()
        self.ui = QUiLoader().load(file)  

        self.ui.bnt_load_image.clicked.connect(self.Load)
        self.ui.bnt_open_predict.clicked.connect(self.Predict)


    def Load(self):
        self.imgNamepath, self.imgType = QFileDialog.getOpenFileName(self.ui,"选择图片",
                                                       "./demo/" , "*.png;;*.jpg")
        print(self.imgNamepath)
        self.img = QPixmap(self.imgNamepath).scaled(self.ui.lb_Image.width(), self.ui.lb_Image.height())
        self.ui.lb_Image.setPixmap(self.img)

    def Predict(self):
        Predicter.predict(self.imgNamepath)
        self.imgNamepath = 'result.png'
        self.img = QPixmap(self.imgNamepath).scaled(self.ui.lb_Image.width(), self.ui.lb_Image.height())
        self.ui.lb_Image.setPixmap(self.img)

if __name__ == '__main__':
    app = QApplication([])
    Predict = Predict()
    Predict.ui.show()
    app.exec_()