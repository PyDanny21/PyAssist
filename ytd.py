
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(484, 640)
        MainWindow.setFocusPolicy(Qt.WheelFocus)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 70, 371, 91))
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgb(193, 0, 0);\n"
"border:4px solid rgb(0, 85, 0);")
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setFrameShadow(QFrame.Raised)
        self.label.setLineWidth(13)
        self.label.setMidLineWidth(11)
        self.label.setTextFormat(Qt.AutoText)
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setMargin(1)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 270, 81, 51))
        font1 = QFont()
        font1.setFamily(u"Gloucester MT Extra Condensed")
        font1.setPointSize(16)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"border:2px solid rgb(255, 255, 255);")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(160, 270, 251, 41))
        font2 = QFont()
        font2.setPointSize(12)
        self.lineEdit.setFont(font2)
        self.lineEdit.setStyleSheet(u"border:2px solid rgb(255, 255, 255);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 350, 81, 51))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"border:2px solid rgb(255, 255, 255);")
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(160, 350, 251, 41))
        self.lineEdit_2.setFont(font2)
        self.lineEdit_2.setStyleSheet(u"border:2px solid rgb(255, 255, 255);")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(300, 480, 111, 41))
        font3 = QFont()
        font3.setFamily(u"Tahoma")
        font3.setPointSize(14)
        self.pushButton.setFont(font3)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(0, 85, 0);")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(70, 480, 111, 41))
        self.pushButton_2.setFont(font3)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(170, 410, 241, 21))
        self.label_4.setStyleSheet(u"border:none;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QApplication.translate("MainWindow", u"YTDownloader", None))
        self.label.setText(QApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:600; color:#ffffff; vertical-align:sub;\">YOUTUBE VIDEO DOWNLOADER</span></p></body></html>", None))
        self.label_2.setText(QApplication.translate("MainWindow", u"PASTE LINK :", None))
        self.label_3.setText(QApplication.translate("MainWindow", u"FILE LOC:", None))
        self.pushButton.setText(QApplication.translate("MainWindow", u"DOWNLOAD", None))
        self.pushButton_2.setText(QApplication.translate("MainWindow", u"CANCEL", None))
        self.label_4.setText(QApplication.translate("MainWindow", u"Downloading.....", None))
    # retranslateUi

        def ytd():
            try:
                from pytube import YouTube
                link=self.lineEdit.text()
                yt=YouTube(link)
                print('Title: ',yt.title)
                print('View: ',yt.views)
                Loc=self.lineEdit_2.text()
                yd=yt.streams.get_highest_resolution()
                self.label_4.setText('Downloading!!!')
                yd.download(Loc,filename='downloads by Pi',filename_prefix='.mp4')
                self.label_4.setText('Download Successful')
            except:
                print('No internet connection')
                self.label_4.setText('No internet connection!')
            
        self.pushButton_2.clicked.connect(ytd)
        



if __name__ == "__main__":
    app=QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())