# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(350, 600))
        MainWindow.setMaximumSize(QtCore.QSize(350, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/stop-small.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QScrollBar:vertical {    border: none;    background: white;    width: 8px;    margin: 12px 0 12px 0;    border-radius: 0px; }/*  HANDLE BAR VERTICAL */QScrollBar::handle:vertical {        background-color: rgb(101, 73, 154);    border-radius: 4px;}QScrollBar::handle:vertical:hover{        background-color: rgb(122, 89, 188);}QScrollBar::handle:vertical:pressed {        background-color: rgb(122, 89, 188);}/* BTN TOP - SCROLLBAR */QScrollBar::sub-line:vertical {    border: none;    background-color:rgb(101, 73, 154);    height: 10px;    border-top-left-radius: 4px;    border-top-right-radius: 4px;    subcontrol-position: top;    subcontrol-origin: margin;}QScrollBar::sub-line:vertical:hover {        background-color:rgb(122, 89, 188);}QScrollBar::sub-line:vertical:pressed {        background-color:rgb(122, 89, 188);}/* BTN BOTTOM - SCROLLBAR */QScrollBar::add-line:vertical {    border: none;    background-color:rgb(101, 73, 154);    height: 10px;    border-bottom-left-radius: 4px;    border-bottom-right-radius: 4px;    subcontrol-position: bottom;    subcontrol-origin: margin;}QScrollBar::add-line:vertical:hover {        background-color:rgb(122, 89, 188);}QScrollBar::add-line:vertical:pressed {        background-color:rgb(122, 89, 188);}/* RESET ARROW */QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {    background: none;}QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {    background: none;}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background:rgb(254,254,254)")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.title_wgt = QtWidgets.QWidget(self.centralwidget)
        self.title_wgt.setObjectName("title_wgt")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.title_wgt)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_3.addWidget(self.title_wgt)
        self.time_wgt = QtWidgets.QWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.time_wgt.setFont(font)
        self.time_wgt.setObjectName("time_wgt")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.time_wgt)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.time_lbl = QtWidgets.QLabel(self.time_wgt)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(18)
        self.time_lbl.setFont(font)
        self.time_lbl.setStyleSheet("QLabel { \n"
"    background:rgb(101, 73, 154); \n"
"    color:white;\n"
"    border: 2px solid rgb(101, 73, 154);\n"
"    border-radius: 18px;\n"
"\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
" }\n"
"")
        self.time_lbl.setObjectName("time_lbl")
        self.horizontalLayout.addWidget(self.time_lbl, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addWidget(self.time_wgt)
        self.seleted_project_lbl = QtWidgets.QLabel(self.centralwidget)
        self.seleted_project_lbl.setMinimumSize(QtCore.QSize(0, 0))
        self.seleted_project_lbl.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.seleted_project_lbl.setFont(font)
        self.seleted_project_lbl.setStyleSheet("color:rgb(101, 73, 154);")
        self.seleted_project_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.seleted_project_lbl.setObjectName("seleted_project_lbl")
        self.verticalLayout_3.addWidget(self.seleted_project_lbl)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem)
        self.start_btn_wgt = QtWidgets.QWidget(self.centralwidget)
        self.start_btn_wgt.setObjectName("start_btn_wgt")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.start_btn_wgt)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.start_btn_lbl = QtWidgets.QLabel(self.start_btn_wgt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_btn_lbl.sizePolicy().hasHeightForWidth())
        self.start_btn_lbl.setSizePolicy(sizePolicy)
        self.start_btn_lbl.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_btn_lbl.setText("")
        self.start_btn_lbl.setPixmap(QtGui.QPixmap("images/stop large.png"))
        self.start_btn_lbl.setObjectName("start_btn_lbl")
        self.horizontalLayout_2.addWidget(self.start_btn_lbl)
        self.verticalLayout_3.addWidget(self.start_btn_wgt)
        self.central_info_wgt = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.central_info_wgt.sizePolicy().hasHeightForWidth())
        self.central_info_wgt.setSizePolicy(sizePolicy)
        self.central_info_wgt.setMinimumSize(QtCore.QSize(274, 40))
        self.central_info_wgt.setMaximumSize(QtCore.QSize(274, 40))
        self.central_info_wgt.setStyleSheet("QWidget{\n"
"    border: 1px solid rgb(179, 179, 179);\n"
"    border-radius: 20px;\n"
"}")
        self.central_info_wgt.setObjectName("central_info_wgt")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.central_info_wgt)
        self.horizontalLayout_5.setContentsMargins(20, 5, 10, 5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.nolimits_lbl = QtWidgets.QLabel(self.central_info_wgt)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.nolimits_lbl.setFont(font)
        self.nolimits_lbl.setStyleSheet("border:None;color:rgb(179, 179, 179);")
        self.nolimits_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.nolimits_lbl.setObjectName("nolimits_lbl")
        self.horizontalLayout_5.addWidget(self.nolimits_lbl)
        self.separator_line = QtWidgets.QFrame(self.central_info_wgt)
        self.separator_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.separator_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.separator_line.setObjectName("separator_line")
        self.horizontalLayout_5.addWidget(self.separator_line)
        self.time_today_lbl = QtWidgets.QLabel(self.central_info_wgt)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.time_today_lbl.setFont(font)
        self.time_today_lbl.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.time_today_lbl.setStyleSheet("border:None;color:rgb(179, 179, 179);")
        self.time_today_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.time_today_lbl.setObjectName("time_today_lbl")
        self.horizontalLayout_5.addWidget(self.time_today_lbl)
        self.verticalLayout_3.addWidget(self.central_info_wgt, 0, QtCore.Qt.AlignHCenter)
        self.search_wgt = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_wgt.sizePolicy().hasHeightForWidth())
        self.search_wgt.setSizePolicy(sizePolicy)
        self.search_wgt.setMinimumSize(QtCore.QSize(274, 30))
        self.search_wgt.setMaximumSize(QtCore.QSize(274, 40))
        self.search_wgt.setStyleSheet("QWidget{\n"
"    border: 1px solid rgb(179, 179, 179);\n"
"    border-radius: 14px;\n"
"    background:rgb(179, 179, 179);\n"
"}")
        self.search_wgt.setObjectName("search_wgt")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.search_wgt)
        self.horizontalLayout_6.setContentsMargins(20, 0, 10, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.search_line_edit = QtWidgets.QLineEdit(self.search_wgt)
        self.search_line_edit.setStyleSheet("border: None;\n"
"color:white;")
        self.search_line_edit.setText("")
        self.search_line_edit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.search_line_edit.setObjectName("search_line_edit")
        self.horizontalLayout_6.addWidget(self.search_line_edit)
        self.search_lbl = QtWidgets.QLabel(self.search_wgt)
        self.search_lbl.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.search_lbl.setStyleSheet("border:None")
        self.search_lbl.setText("")
        self.search_lbl.setPixmap(QtGui.QPixmap("images/magnifier.png"))
        self.search_lbl.setObjectName("search_lbl")
        self.horizontalLayout_6.addWidget(self.search_lbl)
        self.verticalLayout_3.addWidget(self.search_wgt, 0, QtCore.Qt.AlignHCenter)
        self.projects_wgt = QtWidgets.QWidget(self.centralwidget)
        self.projects_wgt.setObjectName("projects_wgt")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.projects_wgt)
        self.horizontalLayout_3.setContentsMargins(20, 0, 20, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.projects_wgt_2 = QtWidgets.QWidget(self.projects_wgt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.projects_wgt_2.sizePolicy().hasHeightForWidth())
        self.projects_wgt_2.setSizePolicy(sizePolicy)
        self.projects_wgt_2.setWhatsThis("")
        self.projects_wgt_2.setStyleSheet("border: 1px solid rgb(179, 179, 179);\n"
"border-radius:26px;\n"
"background:None;")
        self.projects_wgt_2.setObjectName("projects_wgt_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.projects_wgt_2)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.add_projects_wgt = QtWidgets.QWidget(self.projects_wgt_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_projects_wgt.sizePolicy().hasHeightForWidth())
        self.add_projects_wgt.setSizePolicy(sizePolicy)
        self.add_projects_wgt.setMinimumSize(QtCore.QSize(274, 40))
        self.add_projects_wgt.setMaximumSize(QtCore.QSize(274, 40))
        self.add_projects_wgt.setStyleSheet("QWidget { \n"
"    background:rgb(101, 73, 154); \n"
"    color:white;\n"
"    border: 1px solid rgb(101, 73, 154);\n"
"    border-radius: 18px;\n"
" }\n"
"")
        self.add_projects_wgt.setObjectName("add_projects_wgt")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.add_projects_wgt)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.projects_lbl = QtWidgets.QLabel(self.add_projects_wgt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.projects_lbl.sizePolicy().hasHeightForWidth())
        self.projects_lbl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.projects_lbl.setFont(font)
        self.projects_lbl.setObjectName("projects_lbl")
        self.horizontalLayout_4.addWidget(self.projects_lbl, 0, QtCore.Qt.AlignTop)
        self.add_projects_btn = QtWidgets.QLabel(self.add_projects_wgt)
        self.add_projects_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_projects_btn.setStyleSheet("background:None")
        self.add_projects_btn.setText("")
        self.add_projects_btn.setPixmap(QtGui.QPixmap("images/plus (1).png"))
        self.add_projects_btn.setObjectName("add_projects_btn")
        self.horizontalLayout_4.addWidget(self.add_projects_btn)
        self.verticalLayout.addWidget(self.add_projects_wgt)
        self.scrollArea = QtWidgets.QScrollArea(self.projects_wgt_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setStyleSheet("\n"
"    background:rgb(254,254,254);\n"
"border:None;\n"
"border-radius:0px;\n"
"padding:0px;\n"
"")
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 274, 178))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollAreaWidgetContents.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.add_projects_wgt_5 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_projects_wgt_5.sizePolicy().hasHeightForWidth())
        self.add_projects_wgt_5.setSizePolicy(sizePolicy)
        self.add_projects_wgt_5.setMinimumSize(QtCore.QSize(274, 40))
        self.add_projects_wgt_5.setMaximumSize(QtCore.QSize(274, 40))
        self.add_projects_wgt_5.setStyleSheet("QWidget { \n"
"    background:rgb(101, 73, 154); \n"
"    color:white;\n"
"    border: 1px solid rgb(101, 73, 154);\n"
"    border-radius: 18px;\n"
" }\n"
"")
        self.add_projects_wgt_5.setObjectName("add_projects_wgt_5")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.add_projects_wgt_5)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.projects_lbl_5 = QtWidgets.QLabel(self.add_projects_wgt_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.projects_lbl_5.sizePolicy().hasHeightForWidth())
        self.projects_lbl_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.projects_lbl_5.setFont(font)
        self.projects_lbl_5.setObjectName("projects_lbl_5")
        self.horizontalLayout_12.addWidget(self.projects_lbl_5, 0, QtCore.Qt.AlignTop)
        self.add_projects_btn_5 = QtWidgets.QLabel(self.add_projects_wgt_5)
        self.add_projects_btn_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_projects_btn_5.setStyleSheet("background:None")
        self.add_projects_btn_5.setText("")
        self.add_projects_btn_5.setPixmap(QtGui.QPixmap("images/plus (1).png"))
        self.add_projects_btn_5.setObjectName("add_projects_btn_5")
        self.horizontalLayout_12.addWidget(self.add_projects_btn_5)
        self.verticalLayout_2.addWidget(self.add_projects_wgt_5)
        self.add_projects_wgt_4 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_projects_wgt_4.sizePolicy().hasHeightForWidth())
        self.add_projects_wgt_4.setSizePolicy(sizePolicy)
        self.add_projects_wgt_4.setMinimumSize(QtCore.QSize(274, 40))
        self.add_projects_wgt_4.setMaximumSize(QtCore.QSize(274, 40))
        self.add_projects_wgt_4.setStyleSheet("QWidget { \n"
"    background:rgb(101, 73, 154); \n"
"    color:white;\n"
"    border: 1px solid rgb(101, 73, 154);\n"
"    border-radius: 18px;\n"
" }\n"
"")
        self.add_projects_wgt_4.setObjectName("add_projects_wgt_4")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.add_projects_wgt_4)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.projects_lbl_4 = QtWidgets.QLabel(self.add_projects_wgt_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.projects_lbl_4.sizePolicy().hasHeightForWidth())
        self.projects_lbl_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.projects_lbl_4.setFont(font)
        self.projects_lbl_4.setObjectName("projects_lbl_4")
        self.horizontalLayout_11.addWidget(self.projects_lbl_4, 0, QtCore.Qt.AlignTop)
        self.add_projects_btn_4 = QtWidgets.QLabel(self.add_projects_wgt_4)
        self.add_projects_btn_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_projects_btn_4.setStyleSheet("background:None")
        self.add_projects_btn_4.setText("")
        self.add_projects_btn_4.setPixmap(QtGui.QPixmap("images/plus (1).png"))
        self.add_projects_btn_4.setObjectName("add_projects_btn_4")
        self.horizontalLayout_11.addWidget(self.add_projects_btn_4)
        self.verticalLayout_2.addWidget(self.add_projects_wgt_4)
        self.add_projects_wgt_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_projects_wgt_2.sizePolicy().hasHeightForWidth())
        self.add_projects_wgt_2.setSizePolicy(sizePolicy)
        self.add_projects_wgt_2.setMinimumSize(QtCore.QSize(274, 40))
        self.add_projects_wgt_2.setMaximumSize(QtCore.QSize(274, 40))
        self.add_projects_wgt_2.setStyleSheet("QWidget { \n"
"    background:rgb(101, 73, 154); \n"
"    color:white;\n"
"    border: 1px solid rgb(101, 73, 154);\n"
"    border-radius: 18px;\n"
" }\n"
"")
        self.add_projects_wgt_2.setObjectName("add_projects_wgt_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.add_projects_wgt_2)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.projects_lbl_2 = QtWidgets.QLabel(self.add_projects_wgt_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.projects_lbl_2.sizePolicy().hasHeightForWidth())
        self.projects_lbl_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.projects_lbl_2.setFont(font)
        self.projects_lbl_2.setObjectName("projects_lbl_2")
        self.horizontalLayout_8.addWidget(self.projects_lbl_2, 0, QtCore.Qt.AlignTop)
        self.add_projects_btn_2 = QtWidgets.QLabel(self.add_projects_wgt_2)
        self.add_projects_btn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_projects_btn_2.setStyleSheet("background:None")
        self.add_projects_btn_2.setText("")
        self.add_projects_btn_2.setPixmap(QtGui.QPixmap("images/plus (1).png"))
        self.add_projects_btn_2.setObjectName("add_projects_btn_2")
        self.horizontalLayout_8.addWidget(self.add_projects_btn_2)
        self.verticalLayout_2.addWidget(self.add_projects_wgt_2)
        self.add_projects_wgt_3 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_projects_wgt_3.sizePolicy().hasHeightForWidth())
        self.add_projects_wgt_3.setSizePolicy(sizePolicy)
        self.add_projects_wgt_3.setMinimumSize(QtCore.QSize(274, 40))
        self.add_projects_wgt_3.setMaximumSize(QtCore.QSize(274, 40))
        self.add_projects_wgt_3.setStyleSheet("QWidget { \n"
"    background:rgb(101, 73, 154); \n"
"    color:white;\n"
"    border: 1px solid rgb(101, 73, 154);\n"
"    border-radius: 18px;\n"
" }\n"
"")
        self.add_projects_wgt_3.setObjectName("add_projects_wgt_3")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.add_projects_wgt_3)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.projects_lbl_3 = QtWidgets.QLabel(self.add_projects_wgt_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.projects_lbl_3.sizePolicy().hasHeightForWidth())
        self.projects_lbl_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.projects_lbl_3.setFont(font)
        self.projects_lbl_3.setObjectName("projects_lbl_3")
        self.horizontalLayout_10.addWidget(self.projects_lbl_3, 0, QtCore.Qt.AlignTop)
        self.add_projects_btn_3 = QtWidgets.QLabel(self.add_projects_wgt_3)
        self.add_projects_btn_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_projects_btn_3.setStyleSheet("background:None")
        self.add_projects_btn_3.setText("")
        self.add_projects_btn_3.setPixmap(QtGui.QPixmap("images/plus (1).png"))
        self.add_projects_btn_3.setObjectName("add_projects_btn_3")
        self.horizontalLayout_10.addWidget(self.add_projects_btn_3)
        self.verticalLayout_2.addWidget(self.add_projects_wgt_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea, 0, QtCore.Qt.AlignTop)
        self.scrollArea.raise_()
        self.add_projects_wgt.raise_()
        self.horizontalLayout_3.addWidget(self.projects_wgt_2)
        self.verticalLayout_3.addWidget(self.projects_wgt)
        self.error_lbl = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.error_lbl.sizePolicy().hasHeightForWidth())
        self.error_lbl.setSizePolicy(sizePolicy)
        self.error_lbl.setMinimumSize(QtCore.QSize(0, 40))
        self.error_lbl.setMaximumSize(QtCore.QSize(16777215, 40))
        self.error_lbl.setStyleSheet("color:red")
        self.error_lbl.setText("")
        self.error_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.error_lbl.setObjectName("error_lbl")
        self.verticalLayout_3.addWidget(self.error_lbl)
        self.bottom_info_wgt = QtWidgets.QWidget(self.centralwidget)
        self.bottom_info_wgt.setObjectName("bottom_info_wgt")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.bottom_info_wgt)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.refresh_lbl = QtWidgets.QLabel(self.bottom_info_wgt)
        self.refresh_lbl.setText("")
        self.refresh_lbl.setPixmap(QtGui.QPixmap("images/refresh-page-option (1).png"))
        self.refresh_lbl.setObjectName("refresh_lbl")
        self.horizontalLayout_7.addWidget(self.refresh_lbl)
        self.lastupdate_lbl = QtWidgets.QLabel(self.bottom_info_wgt)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lastupdate_lbl.sizePolicy().hasHeightForWidth())
        self.lastupdate_lbl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lastupdate_lbl.setFont(font)
        self.lastupdate_lbl.setStyleSheet("color:rgb(101,73,154);")
        self.lastupdate_lbl.setObjectName("lastupdate_lbl")
        self.horizontalLayout_7.addWidget(self.lastupdate_lbl)
        self.resize_lbl = QtWidgets.QLabel(self.bottom_info_wgt)
        self.resize_lbl.setText("")
        self.resize_lbl.setPixmap(QtGui.QPixmap("images/minimize-arrows.png"))
        self.resize_lbl.setObjectName("resize_lbl")
        self.horizontalLayout_7.addWidget(self.resize_lbl)
        self.forward_lbl = QtWidgets.QLabel(self.bottom_info_wgt)
        self.forward_lbl.setText("")
        self.forward_lbl.setPixmap(QtGui.QPixmap("images/fast-forward.png"))
        self.forward_lbl.setObjectName("forward_lbl")
        self.horizontalLayout_7.addWidget(self.forward_lbl)
        self.verticalLayout_3.addWidget(self.bottom_info_wgt)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Trackify"))
        self.time_lbl.setText(_translate("MainWindow", "00:00:00"))
        self.seleted_project_lbl.setText(_translate("MainWindow", "Design"))
        self.nolimits_lbl.setText(_translate("MainWindow", "No Limits"))
        self.time_today_lbl.setText(_translate("MainWindow", "Today: 00:00"))
        self.search_line_edit.setPlaceholderText(_translate("MainWindow", "Search"))
        self.projects_lbl.setText(_translate("MainWindow", "Projects"))
        self.projects_lbl_5.setText(_translate("MainWindow", "Projects"))
        self.projects_lbl_4.setText(_translate("MainWindow", "Projects"))
        self.projects_lbl_2.setText(_translate("MainWindow", "Projects"))
        self.projects_lbl_3.setText(_translate("MainWindow", "Projects"))
        self.lastupdate_lbl.setText(_translate("MainWindow", "Last updated at: 01/01/2000 12:34pm"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())