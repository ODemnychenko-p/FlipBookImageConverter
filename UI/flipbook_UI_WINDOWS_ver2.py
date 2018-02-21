# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Demnichenko\Programming\FlipBookImageConverter\UI\flipbook_UI_WINDOWS_ver2.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(913, 630)
        MainWindow.setMinimumSize(QtCore.QSize(913, 630))
        MainWindow.setMaximumSize(QtCore.QSize(913, 630))
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background-color: rgb(81, 81, 81);\n"
"}\n"
"QStatusBar {\n"
"color: rgb(203, 203, 203);\n"
"background-color: rgb(89, 90, 90);\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(320, 121))
        self.frame_2.setMaximumSize(QtCore.QSize(320, 121))
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_25 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_25.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_25.setSpacing(0)
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.l_logo = QtWidgets.QLabel(self.frame_2)
        self.l_logo.setMinimumSize(QtCore.QSize(320, 121))
        self.l_logo.setMaximumSize(QtCore.QSize(320, 110))
        self.l_logo.setText("")
        self.l_logo.setPixmap(QtGui.QPixmap("./logo/logo2.png"))
        self.l_logo.setScaledContents(True)
        self.l_logo.setObjectName("l_logo")
        self.gridLayout_25.addWidget(self.l_logo, 0, 0, 1, 1)
        self.gridLayout_18.addWidget(self.frame_2, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(338, 450))
        self.tabWidget.setMaximumSize(QtCore.QSize(338, 450))
        self.tabWidget.setStyleSheet("QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 1px solid rgb(140, 140, 140);\n"
"    position: absolute;\n"
"    top: -0.1em;\n"
"}\n"
"/* Style the tab using the tab sub-control. Note that\n"
"    it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"    color: rgb(80, 80, 80);\n"
"    background-color: qlineargradient(spread:pad, x1:0.489045, y1:1, x2:0.472, y2:0, stop:0 rgba(111, 111, 111, 255), stop:1 rgba(155, 155, 155, 255));\n"
"    border-top-left-radius:2px;\n"
"    border-top-right-radius: 2px;\n"
"    border: 1px solid rgb(140, 140, 140);\n"
"    margin-left: 1px;\n"
"    min-width: 20ex;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0.489045, y1:1, x2:0.472, y2:0, stop:0 rgba(158, 158, 158, 255), stop:1 rgba(203, 203, 203, 255));\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-color: #9B9B9B;\n"
"}\n"
"")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setMinimumSize(QtCore.QSize(320, 61))
        self.groupBox.setMaximumSize(QtCore.QSize(320, 61))
        self.groupBox.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"}\n"
"QGroupBox::title {\n"
"    color: rgb(203, 203, 203);\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"}\n"
"")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_36 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_36.setObjectName("gridLayout_36")
        self.fr_select_field = QtWidgets.QFrame(self.groupBox)
        self.fr_select_field.setMinimumSize(QtCore.QSize(280, 25))
        self.fr_select_field.setMaximumSize(QtCore.QSize(280, 25))
        self.fr_select_field.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_select_field.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_select_field.setObjectName("fr_select_field")
        self.gridLayout = QtWidgets.QGridLayout(self.fr_select_field)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.fld_image_path = QtWidgets.QLineEdit(self.fr_select_field)
        self.fld_image_path.setMinimumSize(QtCore.QSize(253, 23))
        self.fld_image_path.setMaximumSize(QtCore.QSize(253, 23))
        self.fld_image_path.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.fld_image_path.setStyleSheet("QLineEdit{\n"
"color: rgb(203, 203, 203);\n"
"background-color: rgb(117, 117, 117);\n"
"border-top-left-radius: 8px;\n"
"border-bottom-left-radius: 8px;\n"
"padding: 5px;\n"
"}")
        self.fld_image_path.setAlignment(QtCore.Qt.AlignCenter)
        self.fld_image_path.setObjectName("fld_image_path")
        self.gridLayout.addWidget(self.fld_image_path, 0, 0, 1, 1)
        self.btn_image_path = QtWidgets.QToolButton(self.fr_select_field)
        self.btn_image_path.setMinimumSize(QtCore.QSize(28, 23))
        self.btn_image_path.setMaximumSize(QtCore.QSize(28, 23))
        self.btn_image_path.setStyleSheet("QToolButton { /* all types of tool button */\n"
"     border-left:1px solid rgb(75, 75, 75);\n"
"    border-top-right-radius: 8px;\n"
"    border-bottom-right-radius: 8px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.489045, y1:1, x2:0.472, y2:0, stop:0 rgba(111, 111, 111, 255), stop:1 rgba(155, 155, 155, 255));\n"
"}\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0.489045, y1:1, x2:0.472, y2:0, stop:0 rgba(158, 158, 158, 255), stop:1 rgba(203, 203, 203, 255));\n"
"}\n"
"QToolButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0.489045, y1:1, x2:0.472, y2:0, stop:0 rgba(158, 158, 158, 255), stop:1 rgba(203, 203, 203, 255));\n"
"}")
        self.btn_image_path.setObjectName("btn_image_path")
        self.gridLayout.addWidget(self.btn_image_path, 0, 2, 1, 1)
        self.gridLayout_36.addWidget(self.fr_select_field, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 1)
        self.grb_image_info = QtWidgets.QGroupBox(self.tab)
        self.grb_image_info.setMinimumSize(QtCore.QSize(320, 220))
        self.grb_image_info.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.grb_image_info.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"}\n"
"QGroupBox::title {\n"
"    color: rgb(203, 203, 203);\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"}\n"
"")
        self.grb_image_info.setAlignment(QtCore.Qt.AlignCenter)
        self.grb_image_info.setObjectName("grb_image_info")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.grb_image_info)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.fr_image_info = QtWidgets.QFrame(self.grb_image_info)
        self.fr_image_info.setMinimumSize(QtCore.QSize(150, 150))
        self.fr_image_info.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.fr_image_info.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_image_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_image_info.setObjectName("fr_image_info")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.fr_image_info)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.fr_size_px = QtWidgets.QFrame(self.fr_image_info)
        self.fr_size_px.setMinimumSize(QtCore.QSize(150, 25))
        self.fr_size_px.setMaximumSize(QtCore.QSize(16777215, 25))
        self.fr_size_px.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_size_px.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_size_px.setObjectName("fr_size_px")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.fr_size_px)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.l_size_px = QtWidgets.QLabel(self.fr_size_px)
        self.l_size_px.setMinimumSize(QtCore.QSize(60, 25))
        self.l_size_px.setMaximumSize(QtCore.QSize(60, 25))
        self.l_size_px.setStyleSheet("QLabel{    color: rgb(203, 203, 203);}")
        self.l_size_px.setObjectName("l_size_px")
        self.gridLayout_7.addWidget(self.l_size_px, 0, 0, 1, 1)
        self.l_t_size_px = QtWidgets.QLabel(self.fr_size_px)
        self.l_t_size_px.setMinimumSize(QtCore.QSize(80, 25))
        self.l_t_size_px.setMaximumSize(QtCore.QSize(16777215, 25))
        self.l_t_size_px.setStyleSheet("QLabel{    color: rgb(203, 203, 203);}")
        self.l_t_size_px.setText("")
        self.l_t_size_px.setObjectName("l_t_size_px")
        self.gridLayout_7.addWidget(self.l_t_size_px, 0, 1, 1, 1)
        self.gridLayout_11.addWidget(self.fr_size_px, 4, 0, 1, 1)
        self.fr_mode = QtWidgets.QFrame(self.fr_image_info)
        self.fr_mode.setMinimumSize(QtCore.QSize(150, 25))
        self.fr_mode.setMaximumSize(QtCore.QSize(16777215, 25))
        self.fr_mode.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_mode.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_mode.setObjectName("fr_mode")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.fr_mode)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.l_mode = QtWidgets.QLabel(self.fr_mode)
        self.l_mode.setMinimumSize(QtCore.QSize(60, 25))
        self.l_mode.setMaximumSize(QtCore.QSize(60, 25))
        self.l_mode.setStyleSheet("QLabel{    color: rgb(203, 203, 203);}")
        self.l_mode.setObjectName("l_mode")
        self.gridLayout_10.addWidget(self.l_mode, 0, 0, 1, 1)
        self.l_t_mode = QtWidgets.QLabel(self.fr_mode)
        self.l_t_mode.setMinimumSize(QtCore.QSize(80, 25))
        self.l_t_mode.setMaximumSize(QtCore.QSize(16777215, 25))
        self.l_t_mode.setStyleSheet("QLabel{    color: rgb(203, 203, 203);}")
        self.l_t_mode.setText("")
        self.l_t_mode.setObjectName("l_t_mode")
        self.gridLayout_10.addWidget(self.l_t_mode, 0, 1, 1, 1)
        self.gridLayout_11.addWidget(self.fr_mode, 3, 0, 1, 1)
        self.fr_name = QtWidgets.QFrame(self.fr_image_info)
        self.fr_name.setMinimumSize(QtCore.QSize(150, 25))
        self.fr_name.setMaximumSize(QtCore.QSize(16777215, 25))
        self.fr_name.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_name.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_name.setObjectName("fr_name")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.fr_name)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.l_t_name = QtWidgets.QLabel(self.fr_name)
        self.l_t_name.setMinimumSize(QtCore.QSize(80, 25))
        self.l_t_name.setMaximumSize(QtCore.QSize(16777215, 25))
        self.l_t_name.setStyleSheet("QLabel{    color: rgb(203, 203, 203);}")
        self.l_t_name.setText("")
        self.l_t_name.setObjectName("l_t_name")
        self.gridLayout_8.addWidget(self.l_t_name, 1, 1, 1, 1)
        self.l_name = QtWidgets.QLabel(self.fr_name)
        self.l_name.setMinimumSize(QtCore.QSize(60, 25))
        self.l_name.setMaximumSize(QtCore.QSize(60, 25))
        self.l_name.setStyleSheet("QLabel{    color: rgb(203, 203, 203);}")
        self.l_name.setObjectName("l_name")
        self.gridLayout_8.addWidget(self.l_name, 1, 0, 1, 1)
        self.gridLayout_11.addWidget(self.fr_name, 1, 0, 1, 1)
        self.fr_format = QtWidgets.QFrame(self.fr_image_info)
        self.fr_format.setMinimumSize(QtCore.QSize(150, 25))
        self.fr_format.setMaximumSize(QtCore.QSize(16777215, 25))
        self.fr_format.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_format.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_format.setObjectName("fr_format")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.fr_format)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.l_format = QtWidgets.QLabel(self.fr_format)
        self.l_format.setMinimumSize(QtCore.QSize(60, 25))
        self.l_format.setMaximumSize(QtCore.QSize(60, 25))
        self.l_format.setStyleSheet("QLabel{    color: rgb(203, 203, 203);}")
        self.l_format.setObjectName("l_format")
        self.gridLayout_9.addWidget(self.l_format, 0, 0, 1, 1)
        self.l_t_format = QtWidgets.QLabel(self.fr_format)
        self.l_t_format.setMinimumSize(QtCore.QSize(80, 25))
        self.l_t_format.setMaximumSize(QtCore.QSize(16777215, 25))
        self.l_t_format.setStyleSheet("QLabel{    color: rgb(203, 203, 203);}")
        self.l_t_format.setText("")
        self.l_t_format.setObjectName("l_t_format")
        self.gridLayout_9.addWidget(self.l_t_format, 0, 1, 1, 1)
        self.gridLayout_11.addWidget(self.fr_format, 2, 0, 1, 1)
        self.fr_size_mb = QtWidgets.QFrame(self.fr_image_info)
        self.fr_size_mb.setMinimumSize(QtCore.QSize(150, 25))
        self.fr_size_mb.setMaximumSize(QtCore.QSize(16777215, 25))
        self.fr_size_mb.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_size_mb.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_size_mb.setObjectName("fr_size_mb")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.fr_size_mb)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.l_size_mb = QtWidgets.QLabel(self.fr_size_mb)
        self.l_size_mb.setMinimumSize(QtCore.QSize(60, 25))
        self.l_size_mb.setMaximumSize(QtCore.QSize(60, 25))
        self.l_size_mb.setStyleSheet("QLabel{    color: rgb(203, 203, 203);}")
        self.l_size_mb.setObjectName("l_size_mb")
        self.gridLayout_6.addWidget(self.l_size_mb, 0, 0, 1, 1)
        self.l_t_size_mb = QtWidgets.QLabel(self.fr_size_mb)
        self.l_t_size_mb.setMinimumSize(QtCore.QSize(80, 25))
        self.l_t_size_mb.setMaximumSize(QtCore.QSize(16777215, 25))
        self.l_t_size_mb.setStyleSheet("QLabel{    color: rgb(203, 203, 203);}")
        self.l_t_size_mb.setText("")
        self.l_t_size_mb.setObjectName("l_t_size_mb")
        self.gridLayout_6.addWidget(self.l_t_size_mb, 0, 1, 1, 1)
        self.gridLayout_11.addWidget(self.fr_size_mb, 5, 0, 1, 1)
        self.fr_path = QtWidgets.QFrame(self.fr_image_info)
        self.fr_path.setMinimumSize(QtCore.QSize(150, 25))
        self.fr_path.setMaximumSize(QtCore.QSize(16777215, 25))
        self.fr_path.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_path.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_path.setObjectName("fr_path")
        self.gridLayout_30 = QtWidgets.QGridLayout(self.fr_path)
        self.gridLayout_30.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_30.setObjectName("gridLayout_30")
        self.l_path = QtWidgets.QLabel(self.fr_path)
        self.l_path.setMinimumSize(QtCore.QSize(60, 25))
        self.l_path.setMaximumSize(QtCore.QSize(60, 25))
        self.l_path.setStyleSheet("QLabel{    color: rgb(203, 203, 203);}")
        self.l_path.setObjectName("l_path")
        self.gridLayout_30.addWidget(self.l_path, 0, 0, 1, 1)
        self.l_t_path = QtWidgets.QLabel(self.fr_path)
        self.l_t_path.setMinimumSize(QtCore.QSize(80, 25))
        self.l_t_path.setMaximumSize(QtCore.QSize(16777215, 25))
        self.l_t_path.setToolTip("")
        self.l_t_path.setStatusTip("")
        self.l_t_path.setWhatsThis("")
        self.l_t_path.setAccessibleName("")
        self.l_t_path.setAccessibleDescription("")
        self.l_t_path.setStyleSheet("QLabel{    color: rgb(203, 203, 203);}")
        self.l_t_path.setText("")
        self.l_t_path.setTextFormat(QtCore.Qt.AutoText)
        self.l_t_path.setScaledContents(False)
        self.l_t_path.setWordWrap(False)
        self.l_t_path.setOpenExternalLinks(False)
        self.l_t_path.setObjectName("l_t_path")
        self.gridLayout_30.addWidget(self.l_t_path, 0, 1, 1, 1)
        self.gridLayout_11.addWidget(self.fr_path, 0, 0, 1, 1)
        self.gridLayout_12.addWidget(self.fr_image_info, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.grb_image_info, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 3, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_frames = QtWidgets.QWidget()
        self.tab_frames.setObjectName("tab_frames")
        self.gridLayout_26 = QtWidgets.QGridLayout(self.tab_frames)
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.grb_frames_count = QtWidgets.QGroupBox(self.tab_frames)
        self.grb_frames_count.setMinimumSize(QtCore.QSize(145, 80))
        self.grb_frames_count.setMaximumSize(QtCore.QSize(16777215, 80))
        self.grb_frames_count.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.grb_frames_count.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"}\n"
"QGroupBox::title {\n"
"    color: rgb(203, 203, 203);\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"}\n"
"")
        self.grb_frames_count.setAlignment(QtCore.Qt.AlignCenter)
        self.grb_frames_count.setObjectName("grb_frames_count")
        self.gridLayout_27 = QtWidgets.QGridLayout(self.grb_frames_count)
        self.gridLayout_27.setContentsMargins(0, 10, 0, 0)
        self.gridLayout_27.setSpacing(0)
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.fr_horizontal_line = QtWidgets.QFrame(self.grb_frames_count)
        self.fr_horizontal_line.setMinimumSize(QtCore.QSize(120, 25))
        self.fr_horizontal_line.setMaximumSize(QtCore.QSize(16777215, 25))
        self.fr_horizontal_line.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_horizontal_line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_horizontal_line.setObjectName("fr_horizontal_line")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.fr_horizontal_line)
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_15.setSpacing(0)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.l_vertical_count = QtWidgets.QLabel(self.fr_horizontal_line)
        self.l_vertical_count.setMinimumSize(QtCore.QSize(95, 25))
        self.l_vertical_count.setMaximumSize(QtCore.QSize(95, 25))
        self.l_vertical_count.setStyleSheet("QLabel{    color: rgb(203, 203, 203);}")
        self.l_vertical_count.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.l_vertical_count.setObjectName("l_vertical_count")
        self.gridLayout_15.addWidget(self.l_vertical_count, 0, 0, 1, 1)
        self.sb_horizontal_line = QtWidgets.QSpinBox(self.fr_horizontal_line)
        self.sb_horizontal_line.setMinimumSize(QtCore.QSize(200, 24))
        self.sb_horizontal_line.setMaximumSize(QtCore.QSize(220, 24))
        self.sb_horizontal_line.setStyleSheet("QSpinBox{\n"
"color: rgb(203, 203, 203);\n"
"background-color: rgb(117, 117, 117);\n"
"border-radius: 8px;\n"
"padding: 5px;\n"
"}")
        self.sb_horizontal_line.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.sb_horizontal_line.setAccelerated(False)
        self.sb_horizontal_line.setMinimum(1)
        self.sb_horizontal_line.setMaximum(100)
        self.sb_horizontal_line.setObjectName("sb_horizontal_line")
        self.gridLayout_15.addWidget(self.sb_horizontal_line, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_15.addItem(spacerItem2, 0, 2, 1, 1)
        self.gridLayout_27.addWidget(self.fr_horizontal_line, 1, 0, 1, 1)
        self.fr_vertical_line = QtWidgets.QFrame(self.grb_frames_count)
        self.fr_vertical_line.setMinimumSize(QtCore.QSize(120, 25))
        self.fr_vertical_line.setMaximumSize(QtCore.QSize(16777215, 25))
        self.fr_vertical_line.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_vertical_line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_vertical_line.setObjectName("fr_vertical_line")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.fr_vertical_line)
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.l_vertical_line = QtWidgets.QLabel(self.fr_vertical_line)
        self.l_vertical_line.setMinimumSize(QtCore.QSize(95, 25))
        self.l_vertical_line.setMaximumSize(QtCore.QSize(95, 25))
        self.l_vertical_line.setStyleSheet("QLabel{    color: rgb(203, 203, 203);}")
        self.l_vertical_line.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.l_vertical_line.setObjectName("l_vertical_line")
        self.gridLayout_16.addWidget(self.l_vertical_line, 0, 0, 1, 1)
        self.sb_vertical_line = QtWidgets.QSpinBox(self.fr_vertical_line)
        self.sb_vertical_line.setMinimumSize(QtCore.QSize(200, 24))
        self.sb_vertical_line.setMaximumSize(QtCore.QSize(220, 24))
        self.sb_vertical_line.setStyleSheet("QSpinBox{\n"
"color: rgb(203, 203, 203);\n"
"background-color: rgb(117, 117, 117);\n"
"border-radius: 8px;\n"
"padding: 5px;\n"
"}")
        self.sb_vertical_line.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.sb_vertical_line.setMinimum(1)
        self.sb_vertical_line.setMaximum(100)
        self.sb_vertical_line.setObjectName("sb_vertical_line")
        self.gridLayout_16.addWidget(self.sb_vertical_line, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_16.addItem(spacerItem3, 0, 2, 1, 1)
        self.gridLayout_27.addWidget(self.fr_vertical_line, 0, 0, 1, 1)
        self.gridLayout_26.addWidget(self.grb_frames_count, 2, 0, 1, 1)
        self.l_frames_tab_warning = QtWidgets.QLabel(self.tab_frames)
        self.l_frames_tab_warning.setMinimumSize(QtCore.QSize(0, 80))
        self.l_frames_tab_warning.setMaximumSize(QtCore.QSize(16777215, 80))
        self.l_frames_tab_warning.setStyleSheet("QLabel{\n"
"color: rgb(226, 113, 113);\n"
"background-color: rgb(89, 90, 90);\n"
"border-radius: 8px;\n"
"padding: 5px;\n"
"border: 1px solid gray;\n"
"}")
        self.l_frames_tab_warning.setTextFormat(QtCore.Qt.AutoText)
        self.l_frames_tab_warning.setScaledContents(False)
        self.l_frames_tab_warning.setAlignment(QtCore.Qt.AlignCenter)
        self.l_frames_tab_warning.setWordWrap(True)
        self.l_frames_tab_warning.setObjectName("l_frames_tab_warning")
        self.gridLayout_26.addWidget(self.l_frames_tab_warning, 4, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_26.addItem(spacerItem4, 5, 0, 1, 1)
        self.gb_frames_statistic = QtWidgets.QGroupBox(self.tab_frames)
        self.gb_frames_statistic.setMinimumSize(QtCore.QSize(145, 110))
        self.gb_frames_statistic.setMaximumSize(QtCore.QSize(16777215, 110))
        self.gb_frames_statistic.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"}\n"
"QGroupBox::title {\n"
"    color: rgb(203, 203, 203);\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"}\n"
"")
        self.gb_frames_statistic.setAlignment(QtCore.Qt.AlignCenter)
        self.gb_frames_statistic.setObjectName("gb_frames_statistic")
        self.gridLayout_28 = QtWidgets.QGridLayout(self.gb_frames_statistic)
        self.gridLayout_28.setObjectName("gridLayout_28")
        self.fr_total_frames_count = QtWidgets.QFrame(self.gb_frames_statistic)
        self.fr_total_frames_count.setMinimumSize(QtCore.QSize(140, 25))
        self.fr_total_frames_count.setMaximumSize(QtCore.QSize(16777215, 25))
        self.fr_total_frames_count.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_total_frames_count.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_total_frames_count.setObjectName("fr_total_frames_count")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.fr_total_frames_count)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.l_total_frames_count = QtWidgets.QLabel(self.fr_total_frames_count)
        self.l_total_frames_count.setMinimumSize(QtCore.QSize(95, 25))
        self.l_total_frames_count.setMaximumSize(QtCore.QSize(95, 25))
        self.l_total_frames_count.setStyleSheet("QLabel{    color: rgb(203, 203, 203);}")
        self.l_total_frames_count.setObjectName("l_total_frames_count")
        self.gridLayout_13.addWidget(self.l_total_frames_count, 0, 0, 1, 1)
        self.l_t_total_frames_count = QtWidgets.QLabel(self.fr_total_frames_count)
        self.l_t_total_frames_count.setMinimumSize(QtCore.QSize(80, 25))
        self.l_t_total_frames_count.setMaximumSize(QtCore.QSize(16777215, 25))
        self.l_t_total_frames_count.setStyleSheet("QLabel{    color: rgb(203, 203, 203);}")
        self.l_t_total_frames_count.setText("")
        self.l_t_total_frames_count.setObjectName("l_t_total_frames_count")
        self.gridLayout_13.addWidget(self.l_t_total_frames_count, 0, 1, 1, 1)
        self.gridLayout_28.addWidget(self.fr_total_frames_count, 0, 0, 1, 1)
        self.fr_current_frame_id = QtWidgets.QFrame(self.gb_frames_statistic)
        self.fr_current_frame_id.setMinimumSize(QtCore.QSize(140, 25))
        self.fr_current_frame_id.setMaximumSize(QtCore.QSize(16777215, 25))
        self.fr_current_frame_id.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_current_frame_id.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_current_frame_id.setObjectName("fr_current_frame_id")
        self.gridLayout_29 = QtWidgets.QGridLayout(self.fr_current_frame_id)
        self.gridLayout_29.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_29.setSpacing(0)
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.l_current_frame_id = QtWidgets.QLabel(self.fr_current_frame_id)
        self.l_current_frame_id.setMinimumSize(QtCore.QSize(90, 25))
        self.l_current_frame_id.setMaximumSize(QtCore.QSize(90, 25))
        self.l_current_frame_id.setStyleSheet("QLabel{    color: rgb(203, 203, 203);}")
        self.l_current_frame_id.setObjectName("l_current_frame_id")
        self.gridLayout_29.addWidget(self.l_current_frame_id, 0, 0, 1, 1)
        self.l_t_current_frame_id = QtWidgets.QLabel(self.fr_current_frame_id)
        self.l_t_current_frame_id.setMinimumSize(QtCore.QSize(80, 25))
        self.l_t_current_frame_id.setMaximumSize(QtCore.QSize(16777215, 25))
        self.l_t_current_frame_id.setStyleSheet("QLabel{    color: rgb(203, 203, 203);}")
        self.l_t_current_frame_id.setText("")
        self.l_t_current_frame_id.setObjectName("l_t_current_frame_id")
        self.gridLayout_29.addWidget(self.l_t_current_frame_id, 0, 1, 1, 1)
        self.gridLayout_28.addWidget(self.fr_current_frame_id, 1, 0, 1, 1)
        self.fr_frame_size_px = QtWidgets.QFrame(self.gb_frames_statistic)
        self.fr_frame_size_px.setMinimumSize(QtCore.QSize(140, 25))
        self.fr_frame_size_px.setMaximumSize(QtCore.QSize(16777215, 25))
        self.fr_frame_size_px.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_frame_size_px.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_frame_size_px.setObjectName("fr_frame_size_px")
        self.gridLayout_31 = QtWidgets.QGridLayout(self.fr_frame_size_px)
        self.gridLayout_31.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_31.setSpacing(0)
        self.gridLayout_31.setObjectName("gridLayout_31")
        self.l_frame_size_px = QtWidgets.QLabel(self.fr_frame_size_px)
        self.l_frame_size_px.setMinimumSize(QtCore.QSize(80, 25))
        self.l_frame_size_px.setMaximumSize(QtCore.QSize(80, 25))
        self.l_frame_size_px.setStyleSheet("QLabel{    color: rgb(203, 203, 203);}")
        self.l_frame_size_px.setObjectName("l_frame_size_px")
        self.gridLayout_31.addWidget(self.l_frame_size_px, 0, 0, 1, 1)
        self.l_t_frame_size_px = QtWidgets.QLabel(self.fr_frame_size_px)
        self.l_t_frame_size_px.setMinimumSize(QtCore.QSize(80, 25))
        self.l_t_frame_size_px.setMaximumSize(QtCore.QSize(16777215, 25))
        self.l_t_frame_size_px.setStyleSheet("QLabel{    color: rgb(203, 203, 203);}")
        self.l_t_frame_size_px.setText("")
        self.l_t_frame_size_px.setObjectName("l_t_frame_size_px")
        self.gridLayout_31.addWidget(self.l_t_frame_size_px, 0, 1, 1, 1)
        self.gridLayout_28.addWidget(self.fr_frame_size_px, 2, 0, 1, 1)
        self.gridLayout_26.addWidget(self.gb_frames_statistic, 1, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_26.addItem(spacerItem5, 0, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_26.addItem(spacerItem6, 3, 0, 1, 1)
        self.tabWidget.addTab(self.tab_frames, "")
        self.tab_mosaic = QtWidgets.QWidget()
        self.tab_mosaic.setObjectName("tab_mosaic")
        self.gridLayout_40 = QtWidgets.QGridLayout(self.tab_mosaic)
        self.gridLayout_40.setObjectName("gridLayout_40")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_mosaic)
        self.groupBox_2.setMinimumSize(QtCore.QSize(320, 61))
        self.groupBox_2.setMaximumSize(QtCore.QSize(320, 61))
        self.groupBox_2.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"}\n"
"QGroupBox::title {\n"
"    color: rgb(203, 203, 203);\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"}\n"
"")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_34 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_34.setObjectName("gridLayout_34")
        self.fr_frames_path = QtWidgets.QFrame(self.groupBox_2)
        self.fr_frames_path.setMinimumSize(QtCore.QSize(280, 30))
        self.fr_frames_path.setMaximumSize(QtCore.QSize(280, 30))
        self.fr_frames_path.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_frames_path.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_frames_path.setObjectName("fr_frames_path")
        self.gridLayout_24 = QtWidgets.QGridLayout(self.fr_frames_path)
        self.gridLayout_24.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_24.setSpacing(0)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.btn_frames_path = QtWidgets.QToolButton(self.fr_frames_path)
        self.btn_frames_path.setEnabled(True)
        self.btn_frames_path.setMinimumSize(QtCore.QSize(28, 23))
        self.btn_frames_path.setMaximumSize(QtCore.QSize(28, 23))
        self.btn_frames_path.setStyleSheet("QToolButton { /* all types of tool button */\n"
"     border-left:1px solid rgb(75, 75, 75);\n"
"    border-top-right-radius: 8px;\n"
"    border-bottom-right-radius: 8px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.489045, y1:1, x2:0.472, y2:0, stop:0 rgba(111, 111, 111, 255), stop:1 rgba(155, 155, 155, 255));\n"
"}\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0.489045, y1:1, x2:0.472, y2:0, stop:0 rgba(158, 158, 158, 255), stop:1 rgba(203, 203, 203, 255));\n"
"}\n"
"QToolButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0.489045, y1:1, x2:0.472, y2:0, stop:0 rgba(158, 158, 158, 255), stop:1 rgba(203, 203, 203, 255));\n"
"}\n"
"QToolButton:!enabled{\n"
"background-color: qlineargradient(spread:pad, x1:0.489045, y1:1, x2:0.472, y2:0, stop:0 rgba(90, 90, 90, 255), stop:1 rgba(140, 140, 140, 255));\n"
"}")
        self.btn_frames_path.setObjectName("btn_frames_path")
        self.gridLayout_24.addWidget(self.btn_frames_path, 0, 2, 1, 1)
        self.fld_frames_path = QtWidgets.QLineEdit(self.fr_frames_path)
        self.fld_frames_path.setEnabled(True)
        self.fld_frames_path.setMinimumSize(QtCore.QSize(253, 23))
        self.fld_frames_path.setMaximumSize(QtCore.QSize(253, 23))
        self.fld_frames_path.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.fld_frames_path.setStyleSheet("QLineEdit{\n"
"color: rgb(203, 203, 203);\n"
"background-color: rgb(117, 117, 117);\n"
"border-top-left-radius: 8px;\n"
"border-bottom-left-radius: 8px;\n"
"padding: 5px;\n"
"}\n"
"QLineEdit:!enabled{\n"
"background-color: rgb(100, 100, 100);\n"
"}")
        self.fld_frames_path.setAlignment(QtCore.Qt.AlignCenter)
        self.fld_frames_path.setObjectName("fld_frames_path")
        self.gridLayout_24.addWidget(self.fld_frames_path, 0, 1, 1, 1)
        self.gridLayout_34.addWidget(self.fr_frames_path, 0, 0, 1, 1)
        self.gridLayout_40.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_mosaic)
        self.groupBox_5.setMinimumSize(QtCore.QSize(320, 61))
        self.groupBox_5.setMaximumSize(QtCore.QSize(320, 61))
        self.groupBox_5.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"}\n"
"QGroupBox::title {\n"
"    color: rgb(203, 203, 203);\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"}\n"
"")
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_39 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_39.setObjectName("gridLayout_39")
        self.fr_background_color = QtWidgets.QFrame(self.groupBox_5)
        self.fr_background_color.setMinimumSize(QtCore.QSize(300, 20))
        self.fr_background_color.setMaximumSize(QtCore.QSize(300, 40))
        self.fr_background_color.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_background_color.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_background_color.setObjectName("fr_background_color")
        self.gridLayout_35 = QtWidgets.QGridLayout(self.fr_background_color)
        self.gridLayout_35.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_35.setSpacing(0)
        self.gridLayout_35.setObjectName("gridLayout_35")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_35.addItem(spacerItem7, 1, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(35, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_35.addItem(spacerItem8, 1, 7, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(35, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_35.addItem(spacerItem9, 1, 4, 1, 1)
        self.sb_background_color_a = QtWidgets.QSpinBox(self.fr_background_color)
        self.sb_background_color_a.setMinimumSize(QtCore.QSize(65, 24))
        self.sb_background_color_a.setMaximumSize(QtCore.QSize(60, 24))
        self.sb_background_color_a.setStyleSheet("QSpinBox{\n"
"color: rgb(203, 203, 203);\n"
"background-color: rgb(117, 117, 117);\n"
"border-radius: 8px;\n"
"padding: 5px;\n"
"}")
        self.sb_background_color_a.setWrapping(False)
        self.sb_background_color_a.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.sb_background_color_a.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.sb_background_color_a.setMinimum(0)
        self.sb_background_color_a.setMaximum(255)
        self.sb_background_color_a.setProperty("value", 0)
        self.sb_background_color_a.setObjectName("sb_background_color_a")
        self.gridLayout_35.addWidget(self.sb_background_color_a, 1, 8, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(35, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_35.addItem(spacerItem10, 1, 2, 1, 1)
        self.sb_background_color_g = QtWidgets.QSpinBox(self.fr_background_color)
        self.sb_background_color_g.setMinimumSize(QtCore.QSize(65, 24))
        self.sb_background_color_g.setMaximumSize(QtCore.QSize(60, 24))
        self.sb_background_color_g.setStyleSheet("QSpinBox{\n"
"color: rgb(203, 203, 203);\n"
"background-color: rgb(117, 117, 117);\n"
"border-radius: 8px;\n"
"padding: 5px;\n"
"}")
        self.sb_background_color_g.setWrapping(False)
        self.sb_background_color_g.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.sb_background_color_g.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.sb_background_color_g.setMinimum(0)
        self.sb_background_color_g.setMaximum(255)
        self.sb_background_color_g.setProperty("value", 0)
        self.sb_background_color_g.setObjectName("sb_background_color_g")
        self.gridLayout_35.addWidget(self.sb_background_color_g, 1, 3, 1, 1)
        self.sb_background_color_b = QtWidgets.QSpinBox(self.fr_background_color)
        self.sb_background_color_b.setMinimumSize(QtCore.QSize(65, 24))
        self.sb_background_color_b.setMaximumSize(QtCore.QSize(60, 24))
        self.sb_background_color_b.setStyleSheet("QSpinBox{\n"
"color: rgb(203, 203, 203);\n"
"background-color: rgb(117, 117, 117);\n"
"border-radius: 8px;\n"
"padding: 5px;\n"
"}")
        self.sb_background_color_b.setWrapping(False)
        self.sb_background_color_b.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.sb_background_color_b.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.sb_background_color_b.setMinimum(0)
        self.sb_background_color_b.setMaximum(255)
        self.sb_background_color_b.setProperty("value", 0)
        self.sb_background_color_b.setObjectName("sb_background_color_b")
        self.gridLayout_35.addWidget(self.sb_background_color_b, 1, 5, 1, 1)
        self.sb_background_color_r = QtWidgets.QSpinBox(self.fr_background_color)
        self.sb_background_color_r.setMinimumSize(QtCore.QSize(65, 24))
        self.sb_background_color_r.setMaximumSize(QtCore.QSize(60, 24))
        self.sb_background_color_r.setStyleSheet("QSpinBox{\n"
"color: rgb(203, 203, 203);\n"
"background-color: rgb(117, 117, 117);\n"
"border-radius: 8px;\n"
"padding: 5px;\n"
"}")
        self.sb_background_color_r.setWrapping(False)
        self.sb_background_color_r.setFrame(True)
        self.sb_background_color_r.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.sb_background_color_r.setSpecialValueText("")
        self.sb_background_color_r.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.sb_background_color_r.setSuffix("")
        self.sb_background_color_r.setMinimum(0)
        self.sb_background_color_r.setMaximum(255)
        self.sb_background_color_r.setProperty("value", 0)
        self.sb_background_color_r.setObjectName("sb_background_color_r")
        self.gridLayout_35.addWidget(self.sb_background_color_r, 1, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_35.addItem(spacerItem11, 1, 9, 1, 1)
        self.gridLayout_39.addWidget(self.fr_background_color, 0, 0, 1, 1)
        self.gridLayout_40.addWidget(self.groupBox_5, 5, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_mosaic)
        self.groupBox_3.setMinimumSize(QtCore.QSize(320, 61))
        self.groupBox_3.setMaximumSize(QtCore.QSize(320, 61))
        self.groupBox_3.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"}\n"
"QGroupBox::title {\n"
"    color: rgb(203, 203, 203);\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"}\n"
"")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_37 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_37.setObjectName("gridLayout_37")
        self.fr_images_per_line = QtWidgets.QFrame(self.groupBox_3)
        self.fr_images_per_line.setMinimumSize(QtCore.QSize(300, 30))
        self.fr_images_per_line.setMaximumSize(QtCore.QSize(300, 30))
        self.fr_images_per_line.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_images_per_line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_images_per_line.setObjectName("fr_images_per_line")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.fr_images_per_line)
        self.gridLayout_22.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_22.setSpacing(0)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.sb_images_per_line = QtWidgets.QSpinBox(self.fr_images_per_line)
        self.sb_images_per_line.setMinimumSize(QtCore.QSize(281, 24))
        self.sb_images_per_line.setMaximumSize(QtCore.QSize(281, 24))
        self.sb_images_per_line.setStyleSheet("QSpinBox{\n"
"color: rgb(203, 203, 203);\n"
"background-color: rgb(117, 117, 117);\n"
"border-radius: 8px;\n"
"padding: 5px;\n"
"}")
        self.sb_images_per_line.setWrapping(False)
        self.sb_images_per_line.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.sb_images_per_line.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.sb_images_per_line.setMinimum(1)
        self.sb_images_per_line.setMaximum(100)
        self.sb_images_per_line.setProperty("value", 1)
        self.sb_images_per_line.setObjectName("sb_images_per_line")
        self.gridLayout_22.addWidget(self.sb_images_per_line, 0, 0, 1, 1)
        self.gridLayout_37.addWidget(self.fr_images_per_line, 0, 0, 1, 1)
        self.gridLayout_40.addWidget(self.groupBox_3, 3, 0, 1, 1)
        self.l_mosaic_tab_warning = QtWidgets.QLabel(self.tab_mosaic)
        self.l_mosaic_tab_warning.setMinimumSize(QtCore.QSize(0, 80))
        self.l_mosaic_tab_warning.setMaximumSize(QtCore.QSize(16777215, 80))
        self.l_mosaic_tab_warning.setStyleSheet("QLabel{\n"
"color: rgb(226, 113, 113);\n"
"background-color: rgb(89, 90, 90);\n"
"border-radius: 8px;\n"
"padding: 5px;\n"
"border: 1px solid gray;\n"
"}")
        self.l_mosaic_tab_warning.setTextFormat(QtCore.Qt.AutoText)
        self.l_mosaic_tab_warning.setScaledContents(False)
        self.l_mosaic_tab_warning.setAlignment(QtCore.Qt.AlignCenter)
        self.l_mosaic_tab_warning.setWordWrap(True)
        self.l_mosaic_tab_warning.setObjectName("l_mosaic_tab_warning")
        self.gridLayout_40.addWidget(self.l_mosaic_tab_warning, 7, 0, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_40.addItem(spacerItem12, 0, 0, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_40.addItem(spacerItem13, 6, 0, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_40.addItem(spacerItem14, 8, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_mosaic)
        self.groupBox_4.setMinimumSize(QtCore.QSize(320, 61))
        self.groupBox_4.setMaximumSize(QtCore.QSize(320, 61))
        self.groupBox_4.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"}\n"
"QGroupBox::title {\n"
"    color: rgb(203, 203, 203);\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"}\n"
"")
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_38 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_38.setObjectName("gridLayout_38")
        self.fr_max_images = QtWidgets.QFrame(self.groupBox_4)
        self.fr_max_images.setMinimumSize(QtCore.QSize(300, 30))
        self.fr_max_images.setMaximumSize(QtCore.QSize(300, 30))
        self.fr_max_images.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_max_images.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_max_images.setObjectName("fr_max_images")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.fr_max_images)
        self.gridLayout_23.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_23.setSpacing(0)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.sb_max_images = QtWidgets.QSpinBox(self.fr_max_images)
        self.sb_max_images.setEnabled(True)
        self.sb_max_images.setMinimumSize(QtCore.QSize(281, 24))
        self.sb_max_images.setMaximumSize(QtCore.QSize(281, 24))
        self.sb_max_images.setStyleSheet("QSpinBox{\n"
"color: rgb(203, 203, 203);\n"
"background-color: rgb(117, 117, 117);\n"
"border-radius: 8px;\n"
"padding: 5px;\n"
"}\n"
"QSpinBox:!enabled{\n"
"background-color: rgb(100, 100, 100);\n"
"}")
        self.sb_max_images.setWrapping(False)
        self.sb_max_images.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.sb_max_images.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.sb_max_images.setMinimum(1)
        self.sb_max_images.setMaximum(1000)
        self.sb_max_images.setProperty("value", 1)
        self.sb_max_images.setObjectName("sb_max_images")
        self.gridLayout_23.addWidget(self.sb_max_images, 0, 1, 1, 1)
        self.gridLayout_38.addWidget(self.fr_max_images, 0, 0, 1, 1)
        self.gridLayout_40.addWidget(self.groupBox_4, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab_mosaic, "")
        self.tab_output = QtWidgets.QWidget()
        self.tab_output.setObjectName("tab_output")
        self.gridLayout_43 = QtWidgets.QGridLayout(self.tab_output)
        self.gridLayout_43.setObjectName("gridLayout_43")
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_output)
        self.groupBox_8.setMinimumSize(QtCore.QSize(320, 61))
        self.groupBox_8.setMaximumSize(QtCore.QSize(320, 61))
        self.groupBox_8.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"}\n"
"QGroupBox::title {\n"
"    color: rgb(203, 203, 203);\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"}\n"
"")
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_42 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_42.setObjectName("gridLayout_42")
        self.fr_image_format = QtWidgets.QFrame(self.groupBox_8)
        self.fr_image_format.setMinimumSize(QtCore.QSize(300, 30))
        self.fr_image_format.setMaximumSize(QtCore.QSize(300, 30))
        self.fr_image_format.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_image_format.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_image_format.setObjectName("fr_image_format")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.fr_image_format)
        self.gridLayout_19.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_19.setSpacing(0)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.fld_filename = QtWidgets.QLineEdit(self.fr_image_format)
        self.fld_filename.setMinimumSize(QtCore.QSize(200, 23))
        self.fld_filename.setMaximumSize(QtCore.QSize(200, 23))
        self.fld_filename.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.fld_filename.setStyleSheet("QLineEdit{\n"
"color: rgb(203, 203, 203);\n"
"background-color: rgb(117, 117, 117);\n"
"border-radius: 8px;\n"
"padding: 5px;\n"
"}")
        self.fld_filename.setAlignment(QtCore.Qt.AlignCenter)
        self.fld_filename.setObjectName("fld_filename")
        self.gridLayout_19.addWidget(self.fld_filename, 0, 1, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_19.addItem(spacerItem15, 0, 2, 1, 1)
        self.cb_image_format = QtWidgets.QComboBox(self.fr_image_format)
        self.cb_image_format.setMinimumSize(QtCore.QSize(70, 22))
        self.cb_image_format.setMaximumSize(QtCore.QSize(70, 22))
        self.cb_image_format.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cb_image_format.setStyleSheet("QComboBox{\n"
"color: rgb(203, 203, 203);\n"
"background-color: rgb(117, 117, 117);\n"
"padding: 5px;\n"
"padding-left: 10px;\n"
"border-radius: 8px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    color: rgb(203, 203, 203);\n"
"    background-color: rgb(117, 117, 117);\n"
"    border: 1px solid darkgray;\n"
"    selection-background-color:  rgb(150, 150, 150);;\n"
"}\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"     color: white;\n"
"     border-left-width: 1px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     padding-left: 10px;\n"
" }\n"
"QComboBox::down-arrow {\n"
"    image: url(\'D:/Demnichenko/Programming/FlipBookImageConverter/logo/arrow_drop_down_grey_192x192.png\');\n"
"}")
        self.cb_image_format.setFrame(False)
        self.cb_image_format.setObjectName("cb_image_format")
        self.cb_image_format.addItem("")
        self.cb_image_format.addItem("")
        self.cb_image_format.addItem("")
        self.gridLayout_19.addWidget(self.cb_image_format, 0, 3, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_19.addItem(spacerItem16, 0, 0, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_19.addItem(spacerItem17, 0, 4, 1, 1)
        self.gridLayout_42.addWidget(self.fr_image_format, 0, 0, 1, 1)
        self.gridLayout_43.addWidget(self.groupBox_8, 3, 0, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_output)
        self.groupBox_6.setMinimumSize(QtCore.QSize(320, 61))
        self.groupBox_6.setMaximumSize(QtCore.QSize(320, 61))
        self.groupBox_6.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"}\n"
"QGroupBox::title {\n"
"    color: rgb(203, 203, 203);\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"}\n"
"")
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_41 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_41.setObjectName("gridLayout_41")
        self.fr_outpath = QtWidgets.QFrame(self.groupBox_6)
        self.fr_outpath.setMinimumSize(QtCore.QSize(280, 30))
        self.fr_outpath.setMaximumSize(QtCore.QSize(280, 30))
        self.fr_outpath.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_outpath.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_outpath.setObjectName("fr_outpath")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.fr_outpath)
        self.gridLayout_20.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_20.setSpacing(0)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.btn_out_path = QtWidgets.QToolButton(self.fr_outpath)
        self.btn_out_path.setMinimumSize(QtCore.QSize(28, 23))
        self.btn_out_path.setMaximumSize(QtCore.QSize(28, 23))
        self.btn_out_path.setStyleSheet("QToolButton { /* all types of tool button */\n"
"     border-left:1px solid rgb(75, 75, 75);\n"
"    border-top-right-radius: 8px;\n"
"    border-bottom-right-radius: 8px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.489045, y1:1, x2:0.472, y2:0, stop:0 rgba(111, 111, 111, 255), stop:1 rgba(155, 155, 155, 255));\n"
"}\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0.489045, y1:1, x2:0.472, y2:0, stop:0 rgba(158, 158, 158, 255), stop:1 rgba(203, 203, 203, 255));\n"
"}\n"
"QToolButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0.489045, y1:1, x2:0.472, y2:0, stop:0 rgba(158, 158, 158, 255), stop:1 rgba(203, 203, 203, 255));\n"
"}")
        self.btn_out_path.setObjectName("btn_out_path")
        self.gridLayout_20.addWidget(self.btn_out_path, 0, 1, 1, 1)
        self.fld_out_path = QtWidgets.QLineEdit(self.fr_outpath)
        self.fld_out_path.setMinimumSize(QtCore.QSize(253, 23))
        self.fld_out_path.setMaximumSize(QtCore.QSize(253, 23))
        self.fld_out_path.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.fld_out_path.setStyleSheet("QLineEdit{\n"
"color: rgb(203, 203, 203);\n"
"background-color: rgb(117, 117, 117);\n"
"border-top-left-radius: 8px;\n"
"border-bottom-left-radius: 8px;\n"
"padding: 5px;\n"
"}")
        self.fld_out_path.setAlignment(QtCore.Qt.AlignCenter)
        self.fld_out_path.setObjectName("fld_out_path")
        self.gridLayout_20.addWidget(self.fld_out_path, 0, 0, 1, 1)
        self.gridLayout_41.addWidget(self.fr_outpath, 0, 0, 1, 1)
        self.gridLayout_43.addWidget(self.groupBox_6, 1, 0, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_output)
        self.groupBox_7.setMinimumSize(QtCore.QSize(320, 100))
        self.groupBox_7.setMaximumSize(QtCore.QSize(320, 100))
        self.groupBox_7.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"}\n"
"QGroupBox::title {\n"
"    color: rgb(203, 203, 203);\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"}\n"
"")
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_32 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_32.setContentsMargins(-1, 15, -1, -1)
        self.gridLayout_32.setObjectName("gridLayout_32")
        self.fr_valid_frame_range = QtWidgets.QFrame(self.groupBox_7)
        self.fr_valid_frame_range.setMinimumSize(QtCore.QSize(300, 30))
        self.fr_valid_frame_range.setMaximumSize(QtCore.QSize(300, 30))
        self.fr_valid_frame_range.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_valid_frame_range.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_valid_frame_range.setObjectName("fr_valid_frame_range")
        self.gridLayout_33 = QtWidgets.QGridLayout(self.fr_valid_frame_range)
        self.gridLayout_33.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_33.setSpacing(0)
        self.gridLayout_33.setObjectName("gridLayout_33")
        self.cb_valid_frame_range = QtWidgets.QComboBox(self.fr_valid_frame_range)
        self.cb_valid_frame_range.setMinimumSize(QtCore.QSize(160, 22))
        self.cb_valid_frame_range.setMaximumSize(QtCore.QSize(160, 22))
        self.cb_valid_frame_range.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cb_valid_frame_range.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cb_valid_frame_range.setStyleSheet("QComboBox{\n"
"color: rgb(203, 203, 203);\n"
"background-color: rgb(117, 117, 117);\n"
"padding: 5px;\n"
"border-radius: 8px;\n"
"padding-left:10px\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    color: rgb(203, 203, 203);\n"
"    background-color: rgb(117, 117, 117);\n"
"    border: 1px solid darkgray;\n"
"    selection-background-color:  rgb(150, 150, 150);;\n"
"}\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"     color: white;\n"
"     border-left-width: 1px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     padding-left: 10px;\n"
" }")
        self.cb_valid_frame_range.setEditable(False)
        self.cb_valid_frame_range.setMinimumContentsLength(0)
        self.cb_valid_frame_range.setFrame(False)
        self.cb_valid_frame_range.setObjectName("cb_valid_frame_range")
        self.cb_valid_frame_range.addItem("")
        self.cb_valid_frame_range.addItem("")
        self.gridLayout_33.addWidget(self.cb_valid_frame_range, 0, 0, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(107, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_33.addItem(spacerItem18, 0, 1, 1, 1)
        self.gridLayout_32.addWidget(self.fr_valid_frame_range, 0, 0, 1, 1)
        self.fr_start_end_inc = QtWidgets.QFrame(self.groupBox_7)
        self.fr_start_end_inc.setMinimumSize(QtCore.QSize(305, 20))
        self.fr_start_end_inc.setMaximumSize(QtCore.QSize(305, 40))
        self.fr_start_end_inc.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_start_end_inc.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_start_end_inc.setObjectName("fr_start_end_inc")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.fr_start_end_inc)
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_21.setSpacing(0)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.sb_start_value = QtWidgets.QSpinBox(self.fr_start_end_inc)
        self.sb_start_value.setEnabled(False)
        self.sb_start_value.setMinimumSize(QtCore.QSize(60, 24))
        self.sb_start_value.setMaximumSize(QtCore.QSize(60, 24))
        self.sb_start_value.setStyleSheet("QSpinBox{\n"
"color: rgb(203, 203, 203);\n"
"background-color: rgb(117, 117, 117);\n"
"border-radius: 8px;\n"
"padding: 5px;\n"
"}\n"
"QSpinBox:!enabled{\n"
"background-color: rgb(100, 100, 100);\n"
"}\n"
"")
        self.sb_start_value.setWrapping(False)
        self.sb_start_value.setFrame(True)
        self.sb_start_value.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.sb_start_value.setSpecialValueText("")
        self.sb_start_value.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.sb_start_value.setSuffix("")
        self.sb_start_value.setPrefix("")
        self.sb_start_value.setMinimum(0)
        self.sb_start_value.setMaximum(255)
        self.sb_start_value.setProperty("value", 0)
        self.sb_start_value.setObjectName("sb_start_value")
        self.gridLayout_21.addWidget(self.sb_start_value, 2, 2, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_21.addItem(spacerItem19, 2, 3, 1, 1)
        self.l_start_end_inc = QtWidgets.QLabel(self.fr_start_end_inc)
        self.l_start_end_inc.setMinimumSize(QtCore.QSize(80, 25))
        self.l_start_end_inc.setMaximumSize(QtCore.QSize(80, 25))
        self.l_start_end_inc.setStyleSheet("QLabel{    color: rgb(203, 203, 203);}")
        self.l_start_end_inc.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.l_start_end_inc.setObjectName("l_start_end_inc")
        self.gridLayout_21.addWidget(self.l_start_end_inc, 2, 1, 1, 1)
        self.sb_inc_value = QtWidgets.QSpinBox(self.fr_start_end_inc)
        self.sb_inc_value.setEnabled(False)
        self.sb_inc_value.setMinimumSize(QtCore.QSize(60, 24))
        self.sb_inc_value.setMaximumSize(QtCore.QSize(60, 24))
        self.sb_inc_value.setStyleSheet("QSpinBox{\n"
"color: rgb(203, 203, 203);\n"
"background-color: rgb(117, 117, 117);\n"
"border-radius: 8px;\n"
"padding: 5px;\n"
"}\n"
"QSpinBox:!enabled{\n"
"background-color: rgb(100, 100, 100);\n"
"}")
        self.sb_inc_value.setWrapping(False)
        self.sb_inc_value.setFrame(True)
        self.sb_inc_value.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.sb_inc_value.setSpecialValueText("")
        self.sb_inc_value.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.sb_inc_value.setSuffix("")
        self.sb_inc_value.setPrefix("")
        self.sb_inc_value.setMinimum(0)
        self.sb_inc_value.setMaximum(255)
        self.sb_inc_value.setProperty("value", 0)
        self.sb_inc_value.setObjectName("sb_inc_value")
        self.gridLayout_21.addWidget(self.sb_inc_value, 2, 6, 1, 1)
        self.sb_end_value = QtWidgets.QSpinBox(self.fr_start_end_inc)
        self.sb_end_value.setEnabled(False)
        self.sb_end_value.setMinimumSize(QtCore.QSize(60, 24))
        self.sb_end_value.setMaximumSize(QtCore.QSize(60, 24))
        self.sb_end_value.setStyleSheet("QSpinBox{\n"
"color: rgb(203, 203, 203);\n"
"background-color: rgb(117, 117, 117);\n"
"border-radius: 8px;\n"
"padding: 5px;\n"
"}\n"
"QSpinBox:!enabled{\n"
"background-color: rgb(100, 100, 100);\n"
"}")
        self.sb_end_value.setWrapping(False)
        self.sb_end_value.setFrame(True)
        self.sb_end_value.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.sb_end_value.setSpecialValueText("")
        self.sb_end_value.setSuffix("")
        self.sb_end_value.setPrefix("")
        self.sb_end_value.setMinimum(0)
        self.sb_end_value.setMaximum(255)
        self.sb_end_value.setProperty("value", 0)
        self.sb_end_value.setObjectName("sb_end_value")
        self.gridLayout_21.addWidget(self.sb_end_value, 2, 4, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_21.addItem(spacerItem20, 2, 5, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_21.addItem(spacerItem21, 2, 7, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_21.addItem(spacerItem22, 2, 0, 1, 1)
        self.gridLayout_32.addWidget(self.fr_start_end_inc, 1, 0, 1, 1)
        self.gridLayout_43.addWidget(self.groupBox_7, 2, 0, 1, 1)
        self.fr_save_butons = QtWidgets.QFrame(self.tab_output)
        self.fr_save_butons.setMinimumSize(QtCore.QSize(320, 22))
        self.fr_save_butons.setMaximumSize(QtCore.QSize(320, 23))
        self.fr_save_butons.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_save_butons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_save_butons.setObjectName("fr_save_butons")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.fr_save_butons)
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_17.setSpacing(0)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.btn_save = QtWidgets.QPushButton(self.fr_save_butons)
        self.btn_save.setMinimumSize(QtCore.QSize(100, 21))
        self.btn_save.setMaximumSize(QtCore.QSize(100, 21))
        self.btn_save.setStyleSheet("QPushButton { /* all types of tool button */\n"
"    color: rgb(80, 80, 80);\n"
"     border-left:1px solid rgb(75, 75, 75);\n"
"    border-radius: 5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.489045, y1:1, x2:0.472, y2:0, stop:0 rgba(111, 111, 111, 255), stop:1 rgba(155, 155, 155, 255));\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0.489045, y1:1, x2:0.472, y2:0, stop:0 rgba(158, 158, 158, 255), stop:1 rgba(203, 203, 203, 255));\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0.489045, y1:1, x2:0.472, y2:0, stop:0 rgba(158, 158, 158, 255), stop:1 rgba(203, 203, 203, 255));\n"
"}")
        self.btn_save.setObjectName("btn_save")
        self.gridLayout_17.addWidget(self.btn_save, 0, 2, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_17.addItem(spacerItem23, 0, 1, 1, 1)
        self.gridLayout_43.addWidget(self.fr_save_butons, 5, 0, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_43.addItem(spacerItem24, 6, 0, 1, 1)
        spacerItem25 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_43.addItem(spacerItem25, 0, 0, 1, 1)
        spacerItem26 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_43.addItem(spacerItem26, 4, 0, 1, 1)
        self.tabWidget.addTab(self.tab_output, "")
        self.gridLayout_18.addWidget(self.tabWidget, 2, 0, 1, 1)
        self.fr_preview = QtWidgets.QFrame(self.centralwidget)
        self.fr_preview.setMinimumSize(QtCore.QSize(542, 593))
        self.fr_preview.setMaximumSize(QtCore.QSize(542, 593))
        self.fr_preview.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_preview.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_preview.setObjectName("fr_preview")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.fr_preview)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.grb_preview = QtWidgets.QGroupBox(self.fr_preview)
        self.grb_preview.setMinimumSize(QtCore.QSize(542, 590))
        self.grb_preview.setMaximumSize(QtCore.QSize(542, 590))
        self.grb_preview.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"}\n"
"QGroupBox::title {\n"
"    color: rgb(203, 203, 203);\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"}\n"
"")
        self.grb_preview.setObjectName("grb_preview")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.grb_preview)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.fr_preview_image = QtWidgets.QFrame(self.grb_preview)
        self.fr_preview_image.setMinimumSize(QtCore.QSize(512, 512))
        self.fr_preview_image.setMaximumSize(QtCore.QSize(512, 512))
        self.fr_preview_image.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_preview_image.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_preview_image.setObjectName("fr_preview_image")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.fr_preview_image)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.l_preview_image = QtWidgets.QLabel(self.fr_preview_image)
        self.l_preview_image.setMaximumSize(QtCore.QSize(512, 512))
        self.l_preview_image.setStyleSheet("background-color: rgb(89, 90, 90);")
        self.l_preview_image.setText("")
        self.l_preview_image.setAlignment(QtCore.Qt.AlignCenter)
        self.l_preview_image.setObjectName("l_preview_image")
        self.gridLayout_3.addWidget(self.l_preview_image, 0, 3, 1, 1)
        self.gridLayout_4.addWidget(self.fr_preview_image, 0, 0, 1, 1)
        self.fr_frame_slider = QtWidgets.QFrame(self.grb_preview)
        self.fr_frame_slider.setMinimumSize(QtCore.QSize(512, 30))
        self.fr_frame_slider.setMaximumSize(QtCore.QSize(512, 30))
        self.fr_frame_slider.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fr_frame_slider.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_frame_slider.setObjectName("fr_frame_slider")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.fr_frame_slider)
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_14.setSpacing(0)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.sl_frame = QtWidgets.QSlider(self.fr_frame_slider)
        self.sl_frame.setMinimumSize(QtCore.QSize(512, 30))
        self.sl_frame.setMaximumSize(QtCore.QSize(512, 30))
        self.sl_frame.setStyleSheet("QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"    height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 18px;\n"
"    margin: -8px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 3px;\n"
"}")
        self.sl_frame.setMaximum(0)
        self.sl_frame.setOrientation(QtCore.Qt.Horizontal)
        self.sl_frame.setInvertedAppearance(False)
        self.sl_frame.setInvertedControls(False)
        self.sl_frame.setObjectName("sl_frame")
        self.gridLayout_14.addWidget(self.sl_frame, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.fr_frame_slider, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.grb_preview, 0, 0, 1, 1)
        self.gridLayout_18.addWidget(self.fr_preview, 0, 1, 3, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.cb_valid_frame_range.setCurrentIndex(0)
        self.sl_frame.valueChanged['int'].connect(self.l_t_current_frame_id.setNum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FlipBook Converter"))
        self.groupBox.setTitle(_translate("MainWindow", "Image"))
        self.fld_image_path.setPlaceholderText(_translate("MainWindow", "Image Path"))
        self.btn_image_path.setText(_translate("MainWindow", "..."))
        self.grb_image_info.setTitle(_translate("MainWindow", "Info"))
        self.l_size_px.setText(_translate("MainWindow", "Size(px):"))
        self.l_mode.setText(_translate("MainWindow", "Mode:"))
        self.l_name.setText(_translate("MainWindow", "Name:"))
        self.l_format.setText(_translate("MainWindow", "Format:"))
        self.l_size_mb.setText(_translate("MainWindow", "Size(Mb):"))
        self.l_path.setText(_translate("MainWindow", "Path:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Image"))
        self.grb_frames_count.setTitle(_translate("MainWindow", "Frames per line"))
        self.l_vertical_count.setText(_translate("MainWindow", "Horizontal lines:"))
        self.l_vertical_line.setText(_translate("MainWindow", "Vertical lines:"))
        self.l_frames_tab_warning.setText(_translate("MainWindow", "If you want get frames from subUV or Flipbook, use this tab for dividing your image"))
        self.gb_frames_statistic.setTitle(_translate("MainWindow", "Frames statistic"))
        self.l_total_frames_count.setText(_translate("MainWindow", "Total frames count:"))
        self.l_current_frame_id.setText(_translate("MainWindow", "Current frame ID:"))
        self.l_frame_size_px.setText(_translate("MainWindow", "Frame size(px):"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_frames), _translate("MainWindow", "Frames"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Frames directory"))
        self.btn_frames_path.setText(_translate("MainWindow", "..."))
        self.fld_frames_path.setPlaceholderText(_translate("MainWindow", "Frames directory"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Background color"))
        self.sb_background_color_a.setPrefix(_translate("MainWindow", " A:  "))
        self.sb_background_color_g.setPrefix(_translate("MainWindow", " G:  "))
        self.sb_background_color_b.setPrefix(_translate("MainWindow", " B:  "))
        self.sb_background_color_r.setPrefix(_translate("MainWindow", " R:  "))
        self.groupBox_3.setTitle(_translate("MainWindow", "Images per line"))
        self.l_mosaic_tab_warning.setText(_translate("MainWindow", "If you want get SubUV or Flipbook from frames list, use this tab"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Max Images"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_mosaic), _translate("MainWindow", "Mosaic"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Image name and format"))
        self.fld_filename.setPlaceholderText(_translate("MainWindow", "File name"))
        self.cb_image_format.setItemText(0, _translate("MainWindow", "TGA"))
        self.cb_image_format.setItemText(1, _translate("MainWindow", "PNG"))
        self.cb_image_format.setItemText(2, _translate("MainWindow", "JPEG"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Output directory"))
        self.btn_out_path.setText(_translate("MainWindow", "..."))
        self.fld_out_path.setPlaceholderText(_translate("MainWindow", "Output Path"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Valid frame Range"))
        self.cb_valid_frame_range.setCurrentText(_translate("MainWindow", "Render Current Frame"))
        self.cb_valid_frame_range.setItemText(0, _translate("MainWindow", "Render Current Frame"))
        self.cb_valid_frame_range.setItemText(1, _translate("MainWindow", "Render Frame Range"))
        self.l_start_end_inc.setText(_translate("MainWindow", "Start/End/Incr"))
        self.btn_save.setText(_translate("MainWindow", "Render"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_output), _translate("MainWindow", "Output"))
        self.grb_preview.setTitle(_translate("MainWindow", "Preview"))

