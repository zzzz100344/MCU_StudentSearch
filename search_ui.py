# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1140, 899)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.studentIdInput = QtWidgets.QLineEdit(self.centralwidget)
        self.studentIdInput.setGeometry(QtCore.QRect(0, 40, 251, 31))
        self.studentIdInput.setObjectName("studentIdInput")
        self.textLabel = QtWidgets.QLabel(self.centralwidget)
        self.textLabel.setGeometry(QtCore.QRect(40, 210, 170, 232))
        self.textLabel.setStyleSheet("")
        self.textLabel.setObjectName("textLabel")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 80, 171, 51))
        self.pushButton.setStyleSheet("font: 75 12pt \"微软雅黑\";")
        self.pushButton.setObjectName("pushButton")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(268, 0, 851, 879))
        self.frame.setMaximumSize(QtCore.QSize(1000, 1000))
        self.frame.setObjectName("frame")
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 861, 881))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.widget = QtWebEngineWidgets.QWebEngineView(self.tab)
        self.widget.setGeometry(QtCore.QRect(0, 0, 841, 851))
        self.widget.setObjectName("widget")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab_3)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 861, 881))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_22 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 3, 3, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 2, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 4, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 2, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 3, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 2, 1, 1)
        self.label_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 1, 4, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 2, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 5, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 3, 2, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 3, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 3, 5, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 2, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 2, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 1, 5, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 2, 5, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 3, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 3, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab_4)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 861, 881))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_27 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_27.setObjectName("label_27")
        self.gridLayout_2.addWidget(self.label_27, 0, 2, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_26.setObjectName("label_26")
        self.gridLayout_2.addWidget(self.label_26, 0, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_25.setObjectName("label_25")
        self.gridLayout_2.addWidget(self.label_25, 0, 0, 1, 1)
        self.label_48 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_48.setObjectName("label_48")
        self.gridLayout_2.addWidget(self.label_48, 3, 5, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_28.setObjectName("label_28")
        self.gridLayout_2.addWidget(self.label_28, 0, 3, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_29.setObjectName("label_29")
        self.gridLayout_2.addWidget(self.label_29, 0, 4, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_30.setObjectName("label_30")
        self.gridLayout_2.addWidget(self.label_30, 0, 5, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_31.setObjectName("label_31")
        self.gridLayout_2.addWidget(self.label_31, 1, 0, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_32.setObjectName("label_32")
        self.gridLayout_2.addWidget(self.label_32, 1, 1, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_33.setObjectName("label_33")
        self.gridLayout_2.addWidget(self.label_33, 1, 2, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_34.setObjectName("label_34")
        self.gridLayout_2.addWidget(self.label_34, 1, 3, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_35.setObjectName("label_35")
        self.gridLayout_2.addWidget(self.label_35, 1, 4, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_36.setObjectName("label_36")
        self.gridLayout_2.addWidget(self.label_36, 1, 5, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_37.setObjectName("label_37")
        self.gridLayout_2.addWidget(self.label_37, 2, 0, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_38.setObjectName("label_38")
        self.gridLayout_2.addWidget(self.label_38, 2, 1, 1, 1)
        self.label_39 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_39.setObjectName("label_39")
        self.gridLayout_2.addWidget(self.label_39, 2, 2, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_40.setObjectName("label_40")
        self.gridLayout_2.addWidget(self.label_40, 2, 3, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_41.setObjectName("label_41")
        self.gridLayout_2.addWidget(self.label_41, 2, 4, 1, 1)
        self.label_42 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_42.setObjectName("label_42")
        self.gridLayout_2.addWidget(self.label_42, 2, 5, 1, 1)
        self.label_43 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_43.setObjectName("label_43")
        self.gridLayout_2.addWidget(self.label_43, 3, 0, 1, 1)
        self.label_44 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_44.setObjectName("label_44")
        self.gridLayout_2.addWidget(self.label_44, 3, 1, 1, 1)
        self.label_45 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_45.setObjectName("label_45")
        self.gridLayout_2.addWidget(self.label_45, 3, 2, 1, 1)
        self.label_46 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_46.setObjectName("label_46")
        self.gridLayout_2.addWidget(self.label_46, 3, 3, 1, 1)
        self.label_47 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_47.setObjectName("label_47")
        self.gridLayout_2.addWidget(self.label_47, 3, 4, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.tab_5)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 861, 881))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_50 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_50.setObjectName("label_50")
        self.gridLayout_3.addWidget(self.label_50, 0, 1, 1, 1)
        self.label_72 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_72.setObjectName("label_72")
        self.gridLayout_3.addWidget(self.label_72, 3, 5, 1, 1)
        self.label_71 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_71.setObjectName("label_71")
        self.gridLayout_3.addWidget(self.label_71, 3, 4, 1, 1)
        self.label_70 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_70.setObjectName("label_70")
        self.gridLayout_3.addWidget(self.label_70, 3, 3, 1, 1)
        self.label_69 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_69.setObjectName("label_69")
        self.gridLayout_3.addWidget(self.label_69, 3, 2, 1, 1)
        self.label_68 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_68.setObjectName("label_68")
        self.gridLayout_3.addWidget(self.label_68, 3, 1, 1, 1)
        self.label_67 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_67.setObjectName("label_67")
        self.gridLayout_3.addWidget(self.label_67, 3, 0, 1, 1)
        self.label_66 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_66.setObjectName("label_66")
        self.gridLayout_3.addWidget(self.label_66, 2, 5, 1, 1)
        self.label_65 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_65.setObjectName("label_65")
        self.gridLayout_3.addWidget(self.label_65, 2, 4, 1, 1)
        self.label_64 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_64.setObjectName("label_64")
        self.gridLayout_3.addWidget(self.label_64, 2, 3, 1, 1)
        self.label_63 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_63.setObjectName("label_63")
        self.gridLayout_3.addWidget(self.label_63, 2, 2, 1, 1)
        self.label_62 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_62.setObjectName("label_62")
        self.gridLayout_3.addWidget(self.label_62, 2, 1, 1, 1)
        self.label_61 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_61.setObjectName("label_61")
        self.gridLayout_3.addWidget(self.label_61, 2, 0, 1, 1)
        self.label_60 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_60.setObjectName("label_60")
        self.gridLayout_3.addWidget(self.label_60, 1, 5, 1, 1)
        self.label_59 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_59.setObjectName("label_59")
        self.gridLayout_3.addWidget(self.label_59, 1, 4, 1, 1)
        self.label_58 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_58.setObjectName("label_58")
        self.gridLayout_3.addWidget(self.label_58, 1, 3, 1, 1)
        self.label_57 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_57.setObjectName("label_57")
        self.gridLayout_3.addWidget(self.label_57, 1, 2, 1, 1)
        self.label_56 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_56.setObjectName("label_56")
        self.gridLayout_3.addWidget(self.label_56, 1, 1, 1, 1)
        self.label_55 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_55.setObjectName("label_55")
        self.gridLayout_3.addWidget(self.label_55, 1, 0, 1, 1)
        self.label_54 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_54.setObjectName("label_54")
        self.gridLayout_3.addWidget(self.label_54, 0, 5, 1, 1)
        self.label_53 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_53.setObjectName("label_53")
        self.gridLayout_3.addWidget(self.label_53, 0, 4, 1, 1)
        self.label_52 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_52.setObjectName("label_52")
        self.gridLayout_3.addWidget(self.label_52, 0, 3, 1, 1)
        self.label_51 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_51.setObjectName("label_51")
        self.gridLayout_3.addWidget(self.label_51, 0, 2, 1, 1)
        self.label_49 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_49.setObjectName("label_49")
        self.gridLayout_3.addWidget(self.label_49, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayoutWidget_7 = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget_7.setGeometry(QtCore.QRect(0, 0, 861, 881))
        self.gridLayoutWidget_7.setObjectName("gridLayoutWidget_7")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_75 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.label_75.setObjectName("label_75")
        self.gridLayout_7.addWidget(self.label_75, 0, 2, 1, 1)
        self.label_74 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.label_74.setObjectName("label_74")
        self.gridLayout_7.addWidget(self.label_74, 0, 1, 1, 1)
        self.label_73 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.label_73.setObjectName("label_73")
        self.gridLayout_7.addWidget(self.label_73, 0, 0, 1, 1)
        self.label_96 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.label_96.setObjectName("label_96")
        self.gridLayout_7.addWidget(self.label_96, 3, 5, 1, 1)
        self.label_76 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.label_76.setObjectName("label_76")
        self.gridLayout_7.addWidget(self.label_76, 0, 3, 1, 1)
        self.label_77 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.label_77.setObjectName("label_77")
        self.gridLayout_7.addWidget(self.label_77, 0, 4, 1, 1)
        self.label_78 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.label_78.setObjectName("label_78")
        self.gridLayout_7.addWidget(self.label_78, 0, 5, 1, 1)
        self.label_79 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.label_79.setObjectName("label_79")
        self.gridLayout_7.addWidget(self.label_79, 1, 0, 1, 1)
        self.label_80 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.label_80.setObjectName("label_80")
        self.gridLayout_7.addWidget(self.label_80, 1, 1, 1, 1)
        self.label_81 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.label_81.setObjectName("label_81")
        self.gridLayout_7.addWidget(self.label_81, 1, 2, 1, 1)
        self.label_82 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.label_82.setObjectName("label_82")
        self.gridLayout_7.addWidget(self.label_82, 1, 3, 1, 1)
        self.label_83 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.label_83.setObjectName("label_83")
        self.gridLayout_7.addWidget(self.label_83, 1, 4, 1, 1)
        self.label_84 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.label_84.setObjectName("label_84")
        self.gridLayout_7.addWidget(self.label_84, 1, 5, 1, 1)
        self.label_85 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.label_85.setObjectName("label_85")
        self.gridLayout_7.addWidget(self.label_85, 2, 0, 1, 1)
        self.label_86 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.label_86.setObjectName("label_86")
        self.gridLayout_7.addWidget(self.label_86, 2, 1, 1, 1)
        self.label_87 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.label_87.setObjectName("label_87")
        self.gridLayout_7.addWidget(self.label_87, 2, 2, 1, 1)
        self.label_88 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.label_88.setObjectName("label_88")
        self.gridLayout_7.addWidget(self.label_88, 2, 3, 1, 1)
        self.label_89 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.label_89.setObjectName("label_89")
        self.gridLayout_7.addWidget(self.label_89, 2, 4, 1, 1)
        self.label_90 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.label_90.setObjectName("label_90")
        self.gridLayout_7.addWidget(self.label_90, 2, 5, 1, 1)
        self.label_91 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.label_91.setObjectName("label_91")
        self.gridLayout_7.addWidget(self.label_91, 3, 0, 1, 1)
        self.label_92 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.label_92.setObjectName("label_92")
        self.gridLayout_7.addWidget(self.label_92, 3, 1, 1, 1)
        self.label_93 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.label_93.setObjectName("label_93")
        self.gridLayout_7.addWidget(self.label_93, 3, 2, 1, 1)
        self.label_94 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.label_94.setObjectName("label_94")
        self.gridLayout_7.addWidget(self.label_94, 3, 3, 1, 1)
        self.label_95 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.label_95.setObjectName("label_95")
        self.gridLayout_7.addWidget(self.label_95, 3, 4, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayoutWidget_8 = QtWidgets.QWidget(self.tab_6)
        self.gridLayoutWidget_8.setGeometry(QtCore.QRect(0, 0, 861, 881))
        self.gridLayoutWidget_8.setObjectName("gridLayoutWidget_8")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_98 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        self.label_98.setObjectName("label_98")
        self.gridLayout_8.addWidget(self.label_98, 0, 1, 1, 1)
        self.label_99 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        self.label_99.setObjectName("label_99")
        self.gridLayout_8.addWidget(self.label_99, 0, 2, 1, 1)
        self.label_97 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        self.label_97.setObjectName("label_97")
        self.gridLayout_8.addWidget(self.label_97, 0, 0, 1, 1)
        self.label_120 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        self.label_120.setObjectName("label_120")
        self.gridLayout_8.addWidget(self.label_120, 3, 5, 1, 1)
        self.label_119 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        self.label_119.setObjectName("label_119")
        self.gridLayout_8.addWidget(self.label_119, 3, 4, 1, 1)
        self.label_118 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        self.label_118.setObjectName("label_118")
        self.gridLayout_8.addWidget(self.label_118, 3, 3, 1, 1)
        self.label_117 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        self.label_117.setObjectName("label_117")
        self.gridLayout_8.addWidget(self.label_117, 3, 2, 1, 1)
        self.label_116 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        self.label_116.setObjectName("label_116")
        self.gridLayout_8.addWidget(self.label_116, 3, 1, 1, 1)
        self.label_115 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        self.label_115.setObjectName("label_115")
        self.gridLayout_8.addWidget(self.label_115, 3, 0, 1, 1)
        self.label_114 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        self.label_114.setObjectName("label_114")
        self.gridLayout_8.addWidget(self.label_114, 2, 5, 1, 1)
        self.label_113 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        self.label_113.setObjectName("label_113")
        self.gridLayout_8.addWidget(self.label_113, 2, 4, 1, 1)
        self.label_112 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        self.label_112.setObjectName("label_112")
        self.gridLayout_8.addWidget(self.label_112, 2, 3, 1, 1)
        self.label_111 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        self.label_111.setObjectName("label_111")
        self.gridLayout_8.addWidget(self.label_111, 2, 2, 1, 1)
        self.label_110 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        self.label_110.setObjectName("label_110")
        self.gridLayout_8.addWidget(self.label_110, 2, 1, 1, 1)
        self.label_109 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        self.label_109.setObjectName("label_109")
        self.gridLayout_8.addWidget(self.label_109, 2, 0, 1, 1)
        self.label_108 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        self.label_108.setObjectName("label_108")
        self.gridLayout_8.addWidget(self.label_108, 1, 5, 1, 1)
        self.label_107 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        self.label_107.setObjectName("label_107")
        self.gridLayout_8.addWidget(self.label_107, 1, 4, 1, 1)
        self.label_106 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        self.label_106.setObjectName("label_106")
        self.gridLayout_8.addWidget(self.label_106, 1, 3, 1, 1)
        self.label_105 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        self.label_105.setObjectName("label_105")
        self.gridLayout_8.addWidget(self.label_105, 1, 2, 1, 1)
        self.label_104 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        self.label_104.setObjectName("label_104")
        self.gridLayout_8.addWidget(self.label_104, 1, 1, 1, 1)
        self.label_103 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        self.label_103.setObjectName("label_103")
        self.gridLayout_8.addWidget(self.label_103, 1, 0, 1, 1)
        self.label_102 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        self.label_102.setObjectName("label_102")
        self.gridLayout_8.addWidget(self.label_102, 0, 5, 1, 1)
        self.label_101 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        self.label_101.setObjectName("label_101")
        self.gridLayout_8.addWidget(self.label_101, 0, 4, 1, 1)
        self.label_100 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        self.label_100.setObjectName("label_100")
        self.gridLayout_8.addWidget(self.label_100, 0, 3, 1, 1)
        self.tabWidget.addTab(self.tab_6, "")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 560, 161, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 261, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("font: 20pt \"微软雅黑\";")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1140, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.studentIdInput, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.tabWidget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.studentIdInput.setText(_translate("MainWindow", "06360471"))
        self.textLabel.setText(_translate("MainWindow", "                  圖片顯示處"))
        self.pushButton.setText(_translate("MainWindow", "查詢"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "瀏覽"))
        self.label_22.setText(_translate("MainWindow", "TextLabel"))
        self.label_16.setText(_translate("MainWindow", "TextLabel"))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.label_13.setText(_translate("MainWindow", "TextLabel"))
        self.label_19.setText(_translate("MainWindow", "TextLabel"))
        self.label_9.setText(_translate("MainWindow", "TextLabel"))
        self.label_1.setText(_translate("MainWindow", "TextLabel"))
        self.label_11.setText(_translate("MainWindow", "TextLabel"))
        self.label_8.setText(_translate("MainWindow", "TextLabel"))
        self.label_17.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.label_21.setText(_translate("MainWindow", "TextLabel"))
        self.label_20.setText(_translate("MainWindow", "TextLabel"))
        self.label_24.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_15.setText(_translate("MainWindow", "TextLabel"))
        self.label_14.setText(_translate("MainWindow", "TextLabel"))
        self.label_12.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "TextLabel"))
        self.label_18.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.label_23.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.label_10.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "第一頁"))
        self.label_27.setText(_translate("MainWindow", "TextLabel"))
        self.label_26.setText(_translate("MainWindow", "TextLabel"))
        self.label_25.setText(_translate("MainWindow", "TextLabel"))
        self.label_48.setText(_translate("MainWindow", "TextLabel"))
        self.label_28.setText(_translate("MainWindow", "TextLabel"))
        self.label_29.setText(_translate("MainWindow", "TextLabel"))
        self.label_30.setText(_translate("MainWindow", "TextLabel"))
        self.label_31.setText(_translate("MainWindow", "TextLabel"))
        self.label_32.setText(_translate("MainWindow", "TextLabel"))
        self.label_33.setText(_translate("MainWindow", "TextLabel"))
        self.label_34.setText(_translate("MainWindow", "TextLabel"))
        self.label_35.setText(_translate("MainWindow", "TextLabel"))
        self.label_36.setText(_translate("MainWindow", "TextLabel"))
        self.label_37.setText(_translate("MainWindow", "TextLabel"))
        self.label_38.setText(_translate("MainWindow", "TextLabel"))
        self.label_39.setText(_translate("MainWindow", "TextLabel"))
        self.label_40.setText(_translate("MainWindow", "TextLabel"))
        self.label_41.setText(_translate("MainWindow", "TextLabel"))
        self.label_42.setText(_translate("MainWindow", "TextLabel"))
        self.label_43.setText(_translate("MainWindow", "TextLabel"))
        self.label_44.setText(_translate("MainWindow", "TextLabel"))
        self.label_45.setText(_translate("MainWindow", "TextLabel"))
        self.label_46.setText(_translate("MainWindow", "TextLabel"))
        self.label_47.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "第二頁"))
        self.label_50.setText(_translate("MainWindow", "TextLabel"))
        self.label_72.setText(_translate("MainWindow", "TextLabel"))
        self.label_71.setText(_translate("MainWindow", "TextLabel"))
        self.label_70.setText(_translate("MainWindow", "TextLabel"))
        self.label_69.setText(_translate("MainWindow", "TextLabel"))
        self.label_68.setText(_translate("MainWindow", "TextLabel"))
        self.label_67.setText(_translate("MainWindow", "TextLabel"))
        self.label_66.setText(_translate("MainWindow", "TextLabel"))
        self.label_65.setText(_translate("MainWindow", "TextLabel"))
        self.label_64.setText(_translate("MainWindow", "TextLabel"))
        self.label_63.setText(_translate("MainWindow", "TextLabel"))
        self.label_62.setText(_translate("MainWindow", "TextLabel"))
        self.label_61.setText(_translate("MainWindow", "TextLabel"))
        self.label_60.setText(_translate("MainWindow", "TextLabel"))
        self.label_59.setText(_translate("MainWindow", "TextLabel"))
        self.label_58.setText(_translate("MainWindow", "TextLabel"))
        self.label_57.setText(_translate("MainWindow", "TextLabel"))
        self.label_56.setText(_translate("MainWindow", "TextLabel"))
        self.label_55.setText(_translate("MainWindow", "TextLabel"))
        self.label_54.setText(_translate("MainWindow", "TextLabel"))
        self.label_53.setText(_translate("MainWindow", "TextLabel"))
        self.label_52.setText(_translate("MainWindow", "TextLabel"))
        self.label_51.setText(_translate("MainWindow", "TextLabel"))
        self.label_49.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "第三頁"))
        self.label_75.setText(_translate("MainWindow", "TextLabel"))
        self.label_74.setText(_translate("MainWindow", "TextLabel"))
        self.label_73.setText(_translate("MainWindow", "TextLabel"))
        self.label_96.setText(_translate("MainWindow", "TextLabel"))
        self.label_76.setText(_translate("MainWindow", "TextLabel"))
        self.label_77.setText(_translate("MainWindow", "TextLabel"))
        self.label_78.setText(_translate("MainWindow", "TextLabel"))
        self.label_79.setText(_translate("MainWindow", "TextLabel"))
        self.label_80.setText(_translate("MainWindow", "TextLabel"))
        self.label_81.setText(_translate("MainWindow", "TextLabel"))
        self.label_82.setText(_translate("MainWindow", "TextLabel"))
        self.label_83.setText(_translate("MainWindow", "TextLabel"))
        self.label_84.setText(_translate("MainWindow", "TextLabel"))
        self.label_85.setText(_translate("MainWindow", "TextLabel"))
        self.label_86.setText(_translate("MainWindow", "TextLabel"))
        self.label_87.setText(_translate("MainWindow", "TextLabel"))
        self.label_88.setText(_translate("MainWindow", "TextLabel"))
        self.label_89.setText(_translate("MainWindow", "TextLabel"))
        self.label_90.setText(_translate("MainWindow", "TextLabel"))
        self.label_91.setText(_translate("MainWindow", "TextLabel"))
        self.label_92.setText(_translate("MainWindow", "TextLabel"))
        self.label_93.setText(_translate("MainWindow", "TextLabel"))
        self.label_94.setText(_translate("MainWindow", "TextLabel"))
        self.label_95.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "第四頁"))
        self.label_98.setText(_translate("MainWindow", "TextLabel"))
        self.label_99.setText(_translate("MainWindow", "TextLabel"))
        self.label_97.setText(_translate("MainWindow", "TextLabel"))
        self.label_120.setText(_translate("MainWindow", "TextLabel"))
        self.label_119.setText(_translate("MainWindow", "TextLabel"))
        self.label_118.setText(_translate("MainWindow", "TextLabel"))
        self.label_117.setText(_translate("MainWindow", "TextLabel"))
        self.label_116.setText(_translate("MainWindow", "TextLabel"))
        self.label_115.setText(_translate("MainWindow", "TextLabel"))
        self.label_114.setText(_translate("MainWindow", "TextLabel"))
        self.label_113.setText(_translate("MainWindow", "TextLabel"))
        self.label_112.setText(_translate("MainWindow", "TextLabel"))
        self.label_111.setText(_translate("MainWindow", "TextLabel"))
        self.label_110.setText(_translate("MainWindow", "TextLabel"))
        self.label_109.setText(_translate("MainWindow", "TextLabel"))
        self.label_108.setText(_translate("MainWindow", "TextLabel"))
        self.label_107.setText(_translate("MainWindow", "TextLabel"))
        self.label_106.setText(_translate("MainWindow", "TextLabel"))
        self.label_105.setText(_translate("MainWindow", "TextLabel"))
        self.label_104.setText(_translate("MainWindow", "TextLabel"))
        self.label_103.setText(_translate("MainWindow", "TextLabel"))
        self.label_102.setText(_translate("MainWindow", "TextLabel"))
        self.label_101.setText(_translate("MainWindow", "TextLabel"))
        self.label_100.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "第五頁"))
        self.pushButton_2.setText(_translate("MainWindow", "查詢本班選課學生"))
        self.label.setText(_translate("MainWindow", "請輸入欲查詢的學號:"))
from PyQt5 import QtWebEngineWidgets


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())