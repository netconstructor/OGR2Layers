# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_OGR2Layers.ui'
#
# Created: Sat Mar 27 12:00:21 2010
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_OGR2Layers(object):
    def setupUi(self, OGR2Layers):
        OGR2Layers.setObjectName("OGR2Layers")
        OGR2Layers.resize(535, 411)
        self.verticalLayout_2 = QtGui.QVBoxLayout(OGR2Layers)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtGui.QLabel(OGR2Layers)
        self.label_2.setPixmap(QtGui.QPixmap(":/plugins/OGR2Layers/icongui.png"))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(OGR2Layers)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setFrameShape(QtGui.QFrame.NoFrame)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_5 = QtGui.QLabel(OGR2Layers)
        self.label_5.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtGui.QLabel(OGR2Layers)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.tabWidget = QtGui.QTabWidget(OGR2Layers)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.LayerList = QtGui.QListWidget(self.tab)
        self.LayerList.setObjectName("LayerList")
        self.verticalLayout_3.addWidget(self.LayerList)
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.kmldirpath = QtGui.QLineEdit(self.tab)
        self.kmldirpath.setObjectName("kmldirpath")
        self.horizontalLayout_3.addWidget(self.kmldirpath)
        self.browseButton = QtGui.QPushButton(self.tab)
        self.browseButton.setObjectName("browseButton")
        self.horizontalLayout_3.addWidget(self.browseButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_7 = QtGui.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtGui.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(10, 90, 61, 16))
        self.label_8.setObjectName("label_8")
        self.mapSize = QtGui.QComboBox(self.tab_2)
        self.mapSize.setGeometry(QtCore.QRect(10, 110, 121, 22))
        self.mapSize.setObjectName("mapSize")
        self.mapSize.addItem("")
        self.mapSize.addItem("")
        self.mapSize.addItem("")
        self.mapBaseLayer = QtGui.QComboBox(self.tab_2)
        self.mapBaseLayer.setGeometry(QtCore.QRect(190, 110, 231, 22))
        self.mapBaseLayer.setObjectName("mapBaseLayer")
        self.mapBaseLayer.addItem("")
        self.mapBaseLayer.addItem("")
        self.mapBaseLayer.addItem("")
        self.mapBaseLayer.addItem("")
        self.mapBaseLayer.addItem("")
        self.label_9 = QtGui.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(190, 90, 101, 16))
        self.label_9.setObjectName("label_9")
        self.lineEdit = QtGui.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(10, 180, 100, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 180, 100, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(260, 180, 100, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(390, 180, 100, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_10 = QtGui.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(10, 160, 121, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtGui.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(10, 220, 151, 21))
        self.label_11.setObjectName("label_11")
        self.layerSwitcherActive = QtGui.QComboBox(self.tab_2)
        self.layerSwitcherActive.setGeometry(QtCore.QRect(170, 220, 69, 21))
        self.layerSwitcherActive.setObjectName("layerSwitcherActive")
        self.layerSwitcherActive.addItem("")
        self.layerSwitcherActive.addItem("")
        self.mapTitle = QtGui.QLineEdit(self.tab_2)
        self.mapTitle.setGeometry(QtCore.QRect(10, 40, 481, 20))
        self.mapTitle.setObjectName("mapTitle")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_12 = QtGui.QLabel(self.tab_3)
        self.label_12.setGeometry(QtCore.QRect(10, 20, 171, 16))
        self.label_12.setObjectName("label_12")
        self.mousepos = QtGui.QCheckBox(self.tab_3)
        self.mousepos.setGeometry(QtCore.QRect(20, 40, 120, 21))
        self.mousepos.setObjectName("mousepos")
        self.permalink = QtGui.QCheckBox(self.tab_3)
        self.permalink.setGeometry(QtCore.QRect(310, 60, 120, 21))
        self.permalink.setObjectName("permalink")
        self.copyr = QtGui.QCheckBox(self.tab_3)
        self.copyr.setGeometry(QtCore.QRect(310, 40, 120, 21))
        self.copyr.setObjectName("copyr")
        self.scale = QtGui.QCheckBox(self.tab_3)
        self.scale.setGeometry(QtCore.QRect(180, 40, 120, 21))
        self.scale.setObjectName("scale")
        self.zoomBar = QtGui.QCheckBox(self.tab_3)
        self.zoomBar.setGeometry(QtCore.QRect(20, 60, 120, 21))
        self.zoomBar.setObjectName("zoomBar")
        self.navi = QtGui.QCheckBox(self.tab_3)
        self.navi.setGeometry(QtCore.QRect(180, 60, 120, 21))
        self.navi.setObjectName("navi")
        self.groupBox = QtGui.QGroupBox(self.tab_3)
        self.groupBox.setGeometry(QtCore.QRect(10, 90, 471, 51))
        self.groupBox.setObjectName("groupBox")
        self.defaultRender = QtGui.QRadioButton(self.groupBox)
        self.defaultRender.setGeometry(QtCore.QRect(10, 20, 185, 22))
        self.defaultRender.setObjectName("defaultRender")
        self.qgisRender = QtGui.QRadioButton(self.groupBox)
        self.qgisRender.setEnabled(True)
        self.qgisRender.setGeometry(QtCore.QRect(240, 20, 98, 22))
        self.qgisRender.setObjectName("qgisRender")
        self.groupBox_2 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 150, 471, 51))
        self.groupBox_2.setObjectName("groupBox_2")
        self.query = QtGui.QRadioButton(self.groupBox_2)
        self.query.setGeometry(QtCore.QRect(10, 20, 132, 22))
        self.query.setObjectName("query")
        self.query_2 = QtGui.QRadioButton(self.groupBox_2)
        self.query_2.setEnabled(True)
        self.query_2.setGeometry(QtCore.QRect(170, 20, 151, 22))
        self.query_2.setObjectName("query_2")
        self.query_3 = QtGui.QRadioButton(self.groupBox_2)
        self.query_3.setGeometry(QtCore.QRect(350, 20, 98, 22))
        self.query_3.setObjectName("query_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.textBrowser = QtGui.QTextBrowser(self.tab_4)
        self.textBrowser.setGeometry(QtCore.QRect(10, 30, 481, 201))
        self.textBrowser.setObjectName("textBrowser")
        self.label_13 = QtGui.QLabel(self.tab_4)
        self.label_13.setGeometry(QtCore.QRect(10, 10, 217, 16))
        self.label_13.setObjectName("label_13")
        self.tabWidget.addTab(self.tab_4, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.progressBar = QtGui.QProgressBar(OGR2Layers)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_2.addWidget(self.progressBar)
        self.helpButton = QtGui.QPushButton(OGR2Layers)
        self.helpButton.setObjectName("helpButton")
        self.horizontalLayout_2.addWidget(self.helpButton)
        self.buttonBox = QtGui.QDialogButtonBox(OGR2Layers)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_2.addWidget(self.buttonBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(OGR2Layers)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(OGR2Layers)

    def retranslateUi(self, OGR2Layers):
        OGR2Layers.setWindowTitle(QtGui.QApplication.translate("OGR2Layers", "OGR2Layers Plugin: Export to OpenLayers", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("OGR2Layers", "OGR2Layers Plugin", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("OGR2Layers", "This plugin will export active OGR layers to an OpenLayers HTML Map", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("OGR2Layers", "Be careful, the heavier OGR Layers are, the slower the OL Map will be !", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("OGR2Layers", "OGR Active Layers :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("OGR2Layers", "Output directory :", None, QtGui.QApplication.UnicodeUTF8))
        self.browseButton.setText(QtGui.QApplication.translate("OGR2Layers", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("OGR2Layers", "QGIS", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("OGR2Layers", "Map Title :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("OGR2Layers", "Map Size :", None, QtGui.QApplication.UnicodeUTF8))
        self.mapSize.setItemText(0, QtGui.QApplication.translate("OGR2Layers", "400 x 400", None, QtGui.QApplication.UnicodeUTF8))
        self.mapSize.setItemText(1, QtGui.QApplication.translate("OGR2Layers", "800 x 600", None, QtGui.QApplication.UnicodeUTF8))
        self.mapSize.setItemText(2, QtGui.QApplication.translate("OGR2Layers", "Fullscreen", None, QtGui.QApplication.UnicodeUTF8))
        self.mapBaseLayer.setItemText(0, QtGui.QApplication.translate("OGR2Layers", "OpenStreetMap (Mapnik)", None, QtGui.QApplication.UnicodeUTF8))
        self.mapBaseLayer.setItemText(1, QtGui.QApplication.translate("OGR2Layers", "OpenStreetMap (OSMarender)", None, QtGui.QApplication.UnicodeUTF8))
        self.mapBaseLayer.setItemText(2, QtGui.QApplication.translate("OGR2Layers", "OpenStreetMap (Cycleway)", None, QtGui.QApplication.UnicodeUTF8))
        self.mapBaseLayer.setItemText(3, QtGui.QApplication.translate("OGR2Layers", "OpenLayers WMS", None, QtGui.QApplication.UnicodeUTF8))
        self.mapBaseLayer.setItemText(4, QtGui.QApplication.translate("OGR2Layers", "Demis WMS", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("OGR2Layers", "Map Base Layer :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("OGR2Layers", "Default Map Extent :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("OGR2Layers", "Layer Switcher active ?", None, QtGui.QApplication.UnicodeUTF8))
        self.layerSwitcherActive.setItemText(0, QtGui.QApplication.translate("OGR2Layers", "yes", None, QtGui.QApplication.UnicodeUTF8))
        self.layerSwitcherActive.setItemText(1, QtGui.QApplication.translate("OGR2Layers", "no", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("OGR2Layers", "OpenLayers", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("OGR2Layers", "Choose other map controls", None, QtGui.QApplication.UnicodeUTF8))
        self.mousepos.setText(QtGui.QApplication.translate("OGR2Layers", "mouseposition", None, QtGui.QApplication.UnicodeUTF8))
        self.permalink.setText(QtGui.QApplication.translate("OGR2Layers", "permalink", None, QtGui.QApplication.UnicodeUTF8))
        self.copyr.setText(QtGui.QApplication.translate("OGR2Layers", "attribution", None, QtGui.QApplication.UnicodeUTF8))
        self.scale.setText(QtGui.QApplication.translate("OGR2Layers", "scale bar", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomBar.setText(QtGui.QApplication.translate("OGR2Layers", "panZoomBar", None, QtGui.QApplication.UnicodeUTF8))
        self.navi.setText(QtGui.QApplication.translate("OGR2Layers", "overview map", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("OGR2Layers", "Render option", None, QtGui.QApplication.UnicodeUTF8))
        self.defaultRender.setText(QtGui.QApplication.translate("OGR2Layers", "default OpenLayers render", None, QtGui.QApplication.UnicodeUTF8))
        self.qgisRender.setText(QtGui.QApplication.translate("OGR2Layers", "QGIS render", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("OGR2Layers", "Query option", None, QtGui.QApplication.UnicodeUTF8))
        self.query.setText(QtGui.QApplication.translate("OGR2Layers", "query one feature", None, QtGui.QApplication.UnicodeUTF8))
        self.query_2.setText(QtGui.QApplication.translate("OGR2Layers", "query more features ", None, QtGui.QApplication.UnicodeUTF8))
        self.query_3.setText(QtGui.QApplication.translate("OGR2Layers", "none", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("OGR2Layers", "Optional", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("OGR2Layers", "Proiection trasformation information", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("OGR2Layers", "Output", None, QtGui.QApplication.UnicodeUTF8))
        self.helpButton.setText(QtGui.QApplication.translate("OGR2Layers", "Help", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc