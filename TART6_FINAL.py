# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TA6_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
try:
    # new location for sip
    # https://www.riverbankcomputing.com/static/Docs/PyQt5/incompatibilities.html#pyqt-v5-11
    from PyQt5 import sip
except ImportError:
    print(ImportError)
    import "C:\\Users\\tedst\Documents\\Unreal Projects\\TART5\\Intermediate\\PipInstall\\Lib\\site-packages\\PyQt5\sip.pyi"
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QFileDialog, QListWidget, QLineEdit, QGraphicsView, QMenuBar, QMenu, QStatusBar
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 573)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.asset_browse = QtWidgets.QPushButton(self.centralwidget)
        self.asset_browse.setGeometry(QtCore.QRect(690, 10, 91, 21))
        self.asset_browse.setObjectName("asset_browse")
        self.asset_line = QtWidgets.QLineEdit(self.centralwidget)
        self.asset_line.setGeometry(QtCore.QRect(90, 10, 591, 20))
        self.asset_line.setObjectName("asset_line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(6, 10, 61, 20))
        self.label.setObjectName("label")
        self.asset_preview = QtWidgets.QLabel(self.centralwidget)
        self.asset_preview.setGeometry(QtCore.QRect(340, 150, 351, 331))
        self.asset_preview.setObjectName("asset_preview")
        self.prefix_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.prefix_edit.setGeometry(QtCore.QRect(100, 110, 113, 20))
        self.prefix_edit.setObjectName("prefix_edit")
        self.suffix_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.suffix_edit.setGeometry(QtCore.QRect(100, 150, 113, 20))
        self.suffix_edit.setObjectName("suffix_edit")
        self.create_instances_button = QtWidgets.QPushButton(self.centralwidget)
        self.create_instances_button.setGeometry(QtCore.QRect(420, 500, 211, 23))
        self.create_instances_button.setObjectName("create_instances_button")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 190, 181, 16))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 160, 47, 13))
        self.label_5.setObjectName("label_5")
        self.material_folder = QtWidgets.QLineEdit(self.centralwidget)
        self.material_folder.setGeometry(QtCore.QRect(90, 40, 591, 20))
        self.material_folder.setObjectName("material_folder")
        self.material_browse = QtWidgets.QPushButton(self.centralwidget)
        self.material_browse.setGeometry(QtCore.QRect(690, 40, 91, 21))
        self.material_browse.setObjectName("material_browse")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(6, 40, 71, 20))
        self.label_3.setObjectName("label_3")
        self.export_folder = QtWidgets.QLineEdit(self.centralwidget)
        self.export_folder.setGeometry(QtCore.QRect(90, 70, 591, 20))
        self.export_folder.setObjectName("export_folder")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 70, 71, 20))
        self.label_9.setObjectName("label_9")
        self.export_browse = QtWidgets.QPushButton(self.centralwidget)
        self.export_browse.setGeometry(QtCore.QRect(690, 70, 91, 21))
        self.export_browse.setObjectName("export_browse")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(340, 120, 181, 16))
        self.label_6.setObjectName("label_6")
        self.folder_items_list = QtWidgets.QListWidget(self.centralwidget)
        self.folder_items_list.setGeometry(QtCore.QRect(10, 210, 221, 251))
        self.folder_items_list.setObjectName("folder_items_list")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 21))
        self.menubar.setObjectName("menubar")
        self.menuMaterail_Instance_Generator = QtWidgets.QMenu(self.menubar)
        self.menuMaterail_Instance_Generator.setObjectName("menuMaterail_Instance_Generator")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMaterail_Instance_Generator.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect the asset browse button to the image picker
        self.asset_browse.clicked.connect(self.browse_asset_folder)
        # Connect the material browse button to the folder picker
        self.material_browse.clicked.connect(self.browse_material_folder)
        #Connect the Export Browse Button to the folder picker
        self.export_browse.clicked.connect(self.browse_export_folder)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.asset_browse.setText(_translate("MainWindow", "Browse"))
        self.label.setText(_translate("MainWindow", "Asset File Path"))
        self.prefix_edit.setText(_translate("MainWindow", "Prefix"))
        self.suffix_edit.setText(_translate("MainWindow", "Suffix"))
        self.create_instances_button.setText(_translate("MainWindow", "Create Instances with All Materials"))
        self.label_2.setText(_translate("MainWindow", "Materials In Folder Path (Total: 0)"))
        self.label_4.setText(_translate("MainWindow", "Prefix"))
        self.label_5.setText(_translate("MainWindow", "Suffix"))
        self.material_browse.setText(_translate("MainWindow", "Browse"))
        self.label_3.setText(_translate("MainWindow", "Material Folder"))
        self.label_9.setText(_translate("MainWindow", "Export Folder:"))
        self.export_browse.setText(_translate("MainWindow", "Browse"))
        self.label_6.setText(_translate("MainWindow", "Asset Preview"))
        self.menuMaterail_Instance_Generator.setTitle(_translate("MainWindow", "Material Instance Generator"))

    def browse_asset_folder(self):
        filename, _ = QFileDialog.getOpenFileName(None, "Select Image", "", )#"Image Files (*.png *.jpg *.bmp)")
        if filename:
            self.asset_line.setText(filename)
            pixmap = QPixmap(filename)
            # Resize the image to fit within the asset_preview box
            scaled_pixmap = pixmap.scaled(self.asset_preview.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
            self.asset_preview.setPixmap(scaled_pixmap)

    def browse_material_folder(self):
        folder = QFileDialog.getExistingDirectory(None, "Select Folder")
        if folder:
            self.material_folder.setText(folder)
            self.folder_items_list.clear()
            for item in os.listdir(folder):
                self.folder_items_list.addItem(item)

    def browse_export_folder(self):
        folder = QFileDialog.getExistingDirectory(None, "Select Folder")
        if folder:
            self.export_folder.setText(folder)
          
            


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
