# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWtTLjx.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
# 개인적으로 추가해서 넣은 함수 정리하는 구역
# MainWindow.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
# qss_file = './themes/py_dracula_dark.qss'  # QSS 파일 경로
#
# with open(qss_file, 'r') as f:
#         style_sheet = f.read()
# self.styleSheet.setStyleSheet(style_sheet)
# self.appMargins = QVBoxLayout(self.styleSheet)
#
#
# self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
################################################################################
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QTableWidget
from . resources_rc import *
from rc_resources import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1280, 800))
        MainWindow.setMaximumSize(QSize(2560, 1600))
        MainWindow.setSizeIncrement(QSize(0, 0))
        MainWindow.setBaseSize(QSize(1280, 800))
        font = QFont()
        font.setFamily(u"\ub098\ub214\uace0\ub515")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setTabletTracking(True)
        MainWindow.setContextMenuPolicy(Qt.NoContextMenu)
        icon = QIcon()
        icon.addFile(u":/images/images/images/bread40.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        self.styleSheet.setFont(font1)

        qss_file = './themes/py_dracula_dark.qss'  # QSS 파일 경로

        with open(qss_file, 'r') as f:
                style_sheet = f.read()
        self.styleSheet.setStyleSheet(style_sheet)

        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font2 = QFont()
        font2.setFamily(u"Segoe UI Semibold")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftApp.setFont(font2)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(8)
        font3.setBold(False)
        font3.setItalic(False)
        self.titleLeftDescription.setFont(font3)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy1)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font1)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy1.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy1)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font1)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_calender = QPushButton(self.topMenu)
        self.btn_calender.setObjectName(u"btn_calender")
        sizePolicy1.setHeightForWidth(self.btn_calender.sizePolicy().hasHeightForWidth())
        self.btn_calender.setSizePolicy(sizePolicy1)
        self.btn_calender.setMinimumSize(QSize(0, 45))
        self.btn_calender.setFont(font1)
        self.btn_calender.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_calender.setLayoutDirection(Qt.LeftToRight)
        self.btn_calender.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-calendar-check.png);")

        self.verticalLayout_8.addWidget(self.btn_calender)

        self.btn_chart = QPushButton(self.topMenu)
        self.btn_chart.setObjectName(u"btn_chart")
        sizePolicy1.setHeightForWidth(self.btn_chart.sizePolicy().hasHeightForWidth())
        self.btn_chart.setSizePolicy(sizePolicy1)
        self.btn_chart.setMinimumSize(QSize(0, 45))
        self.btn_chart.setFont(font1)
        self.btn_chart.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_chart.setLayoutDirection(Qt.LeftToRight)
        self.btn_chart.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-chart-line.png);")

        self.verticalLayout_8.addWidget(self.btn_chart)

        self.btn_save = QPushButton(self.topMenu)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy1.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy1)
        self.btn_save.setMinimumSize(QSize(0, 45))
        self.btn_save.setFont(font1)
        self.btn_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save.setLayoutDirection(Qt.LeftToRight)
        self.btn_save.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-save.png)")

        self.verticalLayout_8.addWidget(self.btn_save)

        self.btn_exit = QPushButton(self.topMenu)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy1.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy1)
        self.btn_exit.setMinimumSize(QSize(0, 45))
        self.btn_exit.setFont(font1)
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exit.setLayoutDirection(Qt.LeftToRight)
        self.btn_exit.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-x.png);")

        self.verticalLayout_8.addWidget(self.btn_exit)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy1.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy1)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font1)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy2)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy3)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font1)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font4)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon4)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.gridLayout_4 = QGridLayout(self.home)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label = QLabel(self.home)
        self.label.setObjectName(u"label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy4)
        self.label.setMinimumSize(QSize(350, 40))
        self.label.setMaximumSize(QSize(650, 150))
        self.label.setBaseSize(QSize(750, 40))
        self.label.setFont(font1)

        self.horizontalLayout_7.addWidget(self.label)


        self.gridLayout_4.addLayout(self.horizontalLayout_7, 4, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.btn_hotamericano = QPushButton(self.home)
        self.btn_hotamericano.setObjectName(u"btn_hotamericano")
        sizePolicy4.setHeightForWidth(self.btn_hotamericano.sizePolicy().hasHeightForWidth())
        self.btn_hotamericano.setSizePolicy(sizePolicy4)
        self.btn_hotamericano.setMinimumSize(QSize(50, 50))
        self.btn_hotamericano.setMaximumSize(QSize(150, 150))
        self.btn_hotamericano.setSizeIncrement(QSize(50, 50))
        self.btn_hotamericano.setStyleSheet(u"background-color: #bd93f9;")

        self.gridLayout_3.addWidget(self.btn_hotamericano, 2, 3, 1, 1)

        self.btn_cheeseball = QPushButton(self.home)
        self.btn_cheeseball.setObjectName(u"btn_cheeseball")
        sizePolicy4.setHeightForWidth(self.btn_cheeseball.sizePolicy().hasHeightForWidth())
        self.btn_cheeseball.setSizePolicy(sizePolicy4)
        self.btn_cheeseball.setMinimumSize(QSize(50, 50))
        self.btn_cheeseball.setMaximumSize(QSize(150, 150))
        self.btn_cheeseball.setSizeIncrement(QSize(50, 50))
        self.btn_cheeseball.setStyleSheet(u"background-color: #bd93f9;")

        self.gridLayout_3.addWidget(self.btn_cheeseball, 2, 1, 1, 1)

        self.btn_peach = QPushButton(self.home)
        self.btn_peach.setObjectName(u"btn_peach")
        sizePolicy4.setHeightForWidth(self.btn_peach.sizePolicy().hasHeightForWidth())
        self.btn_peach.setSizePolicy(sizePolicy4)
        self.btn_peach.setMinimumSize(QSize(50, 50))
        self.btn_peach.setMaximumSize(QSize(150, 150))
        self.btn_peach.setSizeIncrement(QSize(50, 50))
        self.btn_peach.setAutoFillBackground(False)
        self.btn_peach.setStyleSheet(u"background-color: #bd93f9;")

        self.gridLayout_3.addWidget(self.btn_peach, 3, 3, 1, 1)

        self.btn_brezel = QPushButton(self.home)
        self.btn_brezel.setObjectName(u"btn_brezel")
        sizePolicy4.setHeightForWidth(self.btn_brezel.sizePolicy().hasHeightForWidth())
        self.btn_brezel.setSizePolicy(sizePolicy4)
        self.btn_brezel.setMinimumSize(QSize(50, 50))
        self.btn_brezel.setMaximumSize(QSize(150, 150))
        self.btn_brezel.setSizeIncrement(QSize(50, 50))
        self.btn_brezel.setStyleSheet(u"background-color: #bd93f9;")

        self.gridLayout_3.addWidget(self.btn_brezel, 0, 0, 1, 1)

        self.btn_donuts = QPushButton(self.home)
        self.btn_donuts.setObjectName(u"btn_donuts")
        sizePolicy4.setHeightForWidth(self.btn_donuts.sizePolicy().hasHeightForWidth())
        self.btn_donuts.setSizePolicy(sizePolicy4)
        self.btn_donuts.setMinimumSize(QSize(50, 50))
        self.btn_donuts.setMaximumSize(QSize(150, 150))
        self.btn_donuts.setSizeIncrement(QSize(50, 50))
        self.btn_donuts.setStyleSheet(u"background-color: #bd93f9;")

        self.gridLayout_3.addWidget(self.btn_donuts, 0, 3, 1, 1)

        self.btn_dinoagg = QPushButton(self.home)
        self.btn_dinoagg.setObjectName(u"btn_dinoagg")
        sizePolicy4.setHeightForWidth(self.btn_dinoagg.sizePolicy().hasHeightForWidth())
        self.btn_dinoagg.setSizePolicy(sizePolicy4)
        self.btn_dinoagg.setMinimumSize(QSize(50, 50))
        self.btn_dinoagg.setMaximumSize(QSize(150, 150))
        self.btn_dinoagg.setSizeIncrement(QSize(50, 50))
        self.btn_dinoagg.setStyleSheet(u"background-color: #bd93f9;")

        self.gridLayout_3.addWidget(self.btn_dinoagg, 0, 2, 1, 1)

        self.btn_hotdog = QPushButton(self.home)
        self.btn_hotdog.setObjectName(u"btn_hotdog")
        sizePolicy4.setHeightForWidth(self.btn_hotdog.sizePolicy().hasHeightForWidth())
        self.btn_hotdog.setSizePolicy(sizePolicy4)
        self.btn_hotdog.setMinimumSize(QSize(50, 50))
        self.btn_hotdog.setMaximumSize(QSize(150, 150))
        self.btn_hotdog.setSizeIncrement(QSize(50, 50))
        self.btn_hotdog.setStyleSheet(u"background-color: #bd93f9;")

        self.gridLayout_3.addWidget(self.btn_hotdog, 2, 0, 1, 1)

        self.btn_plum = QPushButton(self.home)
        self.btn_plum.setObjectName(u"btn_plum")
        sizePolicy4.setHeightForWidth(self.btn_plum.sizePolicy().hasHeightForWidth())
        self.btn_plum.setSizePolicy(sizePolicy4)
        self.btn_plum.setMinimumSize(QSize(50, 50))
        self.btn_plum.setMaximumSize(QSize(150, 150))
        self.btn_plum.setSizeIncrement(QSize(50, 50))
        self.btn_plum.setStyleSheet(u"background-color: #bd93f9;")

        self.gridLayout_3.addWidget(self.btn_plum, 3, 1, 1, 1)

        self.btn_americano = QPushButton(self.home)
        self.btn_americano.setObjectName(u"btn_americano")
        sizePolicy4.setHeightForWidth(self.btn_americano.sizePolicy().hasHeightForWidth())
        self.btn_americano.setSizePolicy(sizePolicy4)
        self.btn_americano.setMinimumSize(QSize(50, 50))
        self.btn_americano.setMaximumSize(QSize(150, 150))
        self.btn_americano.setSizeIncrement(QSize(50, 50))
        self.btn_americano.setStyleSheet(u"background-color: #bd93f9;")

        self.gridLayout_3.addWidget(self.btn_americano, 2, 2, 1, 1)

        self.btn_pomegranate = QPushButton(self.home)
        self.btn_pomegranate.setObjectName(u"btn_pomegranate")
        sizePolicy4.setHeightForWidth(self.btn_pomegranate.sizePolicy().hasHeightForWidth())
        self.btn_pomegranate.setSizePolicy(sizePolicy4)
        self.btn_pomegranate.setMinimumSize(QSize(50, 50))
        self.btn_pomegranate.setMaximumSize(QSize(150, 150))
        self.btn_pomegranate.setSizeIncrement(QSize(50, 50))
        self.btn_pomegranate.setStyleSheet(u"background-color: #bd93f9;")

        self.gridLayout_3.addWidget(self.btn_pomegranate, 3, 0, 1, 1)

        self.btn_brezel_set = QPushButton(self.home)
        self.btn_brezel_set.setObjectName(u"btn_brezel_set")
        sizePolicy4.setHeightForWidth(self.btn_brezel_set.sizePolicy().hasHeightForWidth())
        self.btn_brezel_set.setSizePolicy(sizePolicy4)
        self.btn_brezel_set.setMinimumSize(QSize(50, 50))
        self.btn_brezel_set.setMaximumSize(QSize(150, 150))
        self.btn_brezel_set.setSizeIncrement(QSize(50, 50))
        self.btn_brezel_set.setStyleSheet(u"background-color: #bd93f9;")

        self.gridLayout_3.addWidget(self.btn_brezel_set, 0, 1, 1, 1)

        self.btn_blueberries = QPushButton(self.home)
        self.btn_blueberries.setObjectName(u"btn_blueberries")
        sizePolicy4.setHeightForWidth(self.btn_blueberries.sizePolicy().hasHeightForWidth())
        self.btn_blueberries.setSizePolicy(sizePolicy4)
        self.btn_blueberries.setMinimumSize(QSize(50, 50))
        self.btn_blueberries.setMaximumSize(QSize(150, 150))
        self.btn_blueberries.setSizeIncrement(QSize(50, 50))
        self.btn_blueberries.setStyleSheet(u"background-color: #bd93f9;")

        self.gridLayout_3.addWidget(self.btn_blueberries, 3, 2, 1, 1)

        self.btn_coke = QPushButton(self.home)
        self.btn_coke.setObjectName(u"btn_coke")
        sizePolicy4.setHeightForWidth(self.btn_coke.sizePolicy().hasHeightForWidth())
        self.btn_coke.setSizePolicy(sizePolicy4)
        self.btn_coke.setMinimumSize(QSize(50, 50))
        self.btn_coke.setMaximumSize(QSize(150, 150))
        self.btn_coke.setSizeIncrement(QSize(50, 50))
        self.btn_coke.setStyleSheet(u"background-color: #bd93f9;")

        self.gridLayout_3.addWidget(self.btn_coke, 4, 0, 1, 1)

        self.btn_cider = QPushButton(self.home)
        self.btn_cider.setObjectName(u"btn_cider")
        sizePolicy4.setHeightForWidth(self.btn_cider.sizePolicy().hasHeightForWidth())
        self.btn_cider.setSizePolicy(sizePolicy4)
        self.btn_cider.setMinimumSize(QSize(50, 50))
        self.btn_cider.setMaximumSize(QSize(150, 150))
        self.btn_cider.setSizeIncrement(QSize(50, 50))
        self.btn_cider.setStyleSheet(u"background-color: #bd93f9;")

        self.gridLayout_3.addWidget(self.btn_cider, 4, 1, 1, 1)

        self.btn_Fanta = QPushButton(self.home)
        self.btn_Fanta.setObjectName(u"btn_Fanta")
        sizePolicy4.setHeightForWidth(self.btn_Fanta.sizePolicy().hasHeightForWidth())
        self.btn_Fanta.setSizePolicy(sizePolicy4)
        self.btn_Fanta.setMinimumSize(QSize(50, 50))
        self.btn_Fanta.setMaximumSize(QSize(150, 150))
        self.btn_Fanta.setSizeIncrement(QSize(50, 50))
        self.btn_Fanta.setStyleSheet(u"background-color: #bd93f9;")

        self.gridLayout_3.addWidget(self.btn_Fanta, 4, 2, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 2, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.pushButton_3 = QPushButton(self.home)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy4.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy4)
        self.pushButton_3.setMinimumSize(QSize(110, 40))
        self.pushButton_3.setMaximumSize(QSize(500, 150))
        self.pushButton_3.setBaseSize(QSize(110, 40))
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.horizontalLayout_6.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.home)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy4.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy4)
        self.pushButton_2.setMinimumSize(QSize(110, 40))
        self.pushButton_2.setMaximumSize(QSize(500, 150))
        self.pushButton_2.setBaseSize(QSize(110, 40))
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.horizontalLayout_6.addWidget(self.pushButton_2)


        self.gridLayout_4.addLayout(self.horizontalLayout_6, 4, 1, 1, 3)

        self.tableWidget = QTableWidget(self.home)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        font5 = QFont()
        font5.setStyleStrategy(QFont.PreferDefault)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font5);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QSize(220, 580))
        self.tableWidget.setMaximumSize(QSize(900, 1220))
        self.tableWidget.setBaseSize(QSize(220, 580))
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)

        self.gridLayout_4.addWidget(self.tableWidget, 2, 2, 1, 1)

        self.stackedWidget.addWidget(self.home)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget.addWidget(self.widgets)
        self.new_page = QWidget()
        self.new_page.setObjectName(u"new_page")
        self.verticalLayout_20 = QVBoxLayout(self.new_page)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.tableView = QTableView(self.new_page)
        self.tableView.setObjectName(u"tableView")


        # # 추가/삭제 레이아웃 
        # # horizental box를 담을 위젯 생성
        # self.btn_0_4_cellWidget = QWidget()
        # # 버튼을 담을 horizental box 생성
        # self.btn_0_4_layout = QGridLayout(self.btn_0_4_cellWidget)
        # self.btn_0_4_cellWidget.setLayout(self.btn_0_4_layout)
        # self.btn_0_4_Add = QPushButton(self.home).setObjectName("추가")
        # self.btn_0_4_Sub = QPushButton(self.home).setObjectName("제거")
        # self.btn_0_4_layout.setContentsMargins(0, 0, 0, 0)
        # # 버튼 가운데로 세팅 하기 위해 마진 설정
        # # 레이아웃에 버튼 삽입
        # self.btn_0_4_layout.addWidget(self.btn_0_4_Add, 0, 4)
        # self.btn_0_4_layout.addWidget(self.btn_0_4_Sub, 0, 4)
        # # 위젯에 레이아웃 담기
        # self.btn_0_4_cellWidget.setLayout(self.btn_0_4_layout)

        # # horizental box를 담을 위젯 생성
        # btn_0_5_cellWidget = QWidget()
        # # 버튼을 담을 horizental box 생성
        # btn_0_5_layout = QGridLayout(btn_0_5_cellWidget)
        # self.btn_0_5_Del = QPushButton().setObjectName("X")
        # # 레이아웃에 버튼 삽입
        # btn_0_5_layout.addWidget(self.btn_0_5_Del)
        # # 버튼 가운데로 세팅 하기 위해 마진 설정
        # btn_0_5_layout.setContentsMargins(0, 0, 0, 0)
        # # 위젯에 레이아웃 담기
        # btn_0_5_cellWidget.setLayout(btn_0_5_layout)

        # # horizental box를 담을 위젯 생성
        # btn_1_4_cellWidget = QWidget()
        # # 버튼을 담을 horizental box 생성
        # btn_1_4_layout = QGridLayout(btn_1_4_cellWidget)
        # self.btn_1_4_Add = QPushButton().setObjectName("추가")
        # # 레이아웃에 버튼 삽입
        # btn_1_4_layout.addWidget(self.btn_1_4_Add)
        # # 버튼 가운데로 세팅 하기 위해 마진 설정
        # btn_1_4_layout.setContentsMargins(0, 0, 0, 0)
        # # 위젯에 레이아웃 담기
        # btn_1_4_cellWidget.setLayout(btn_1_4_layout)

        # # horizental box를 담을 위젯 생성
        # btn_2_4_cellWidget = QWidget()
        # # 버튼을 담을 horizental box 생성
        # btn_2_4_layout = QGridLayout(btn_2_4_cellWidget)
        # self.btn_2_4_Add = QPushButton().setObjectName("추가")
        # # 레이아웃에 버튼 삽입
        # btn_2_4_layout.addWidget(self.btn_2_4_Add)
        # # 버튼 가운데로 세팅 하기 위해 마진 설정
        # btn_2_4_layout.setContentsMargins(0, 0, 0, 0)
        # # 위젯에 레이아웃 담기
        # btn_2_4_cellWidget.setLayout(btn_2_4_layout)

        # # horizental box를 담을 위젯 생성
        # btn_3_4_cellWidget = QWidget()
        # # 버튼을 담을 horizental box 생성
        # btn_3_4_layout = QGridLayout(btn_3_4_cellWidget)
        # self.btn_3_4_Add = QPushButton().setObjectName("추가")
        # # 레이아웃에 버튼 삽입
        # btn_3_4_layout.addWidget(self.btn_3_4_Add)
        # # 버튼 가운데로 세팅 하기 위해 마진 설정
        # btn_3_4_layout.setContentsMargins(0, 0, 0, 0)
        # # 위젯에 레이아웃 담기
        # btn_3_4_cellWidget.setLayout(btn_3_4_layout)

        # # horizental box를 담을 위젯 생성
        # btn_4_4_cellWidget = QWidget()
        # # 버튼을 담을 horizental box 생성
        # btn_4_4_layout = QGridLayout(btn_4_4_cellWidget)
        # self.btn_4_4_Add = QPushButton().setObjectName("추가")
        # # 레이아웃에 버튼 삽입
        # btn_4_4_layout.addWidget(self.btn_4_4_Add)
        # # 버튼 가운데로 세팅 하기 위해 마진 설정
        # btn_4_4_layout.setContentsMargins(0, 0, 0, 0)
        # # 위젯에 레이아웃 담기
        # btn_4_4_cellWidget.setLayout(btn_4_4_layout)

        # # horizental box를 담을 위젯 생성
        # btn_5_4_cellWidget = QWidget()
        # # 버튼을 담을 horizental box 생성
        # btn_5_4_layout = QGridLayout(btn_5_4_cellWidget)
        # self.btn_5_4_Add = QPushButton().setObjectName("추가")
        # # 레이아웃에 버튼 삽입
        # btn_5_4_layout.addWidget(self.btn_5_4_Add)
        # # 버튼 가운데로 세팅 하기 위해 마진 설정
        # btn_5_4_layout.setContentsMargins(0, 0, 0, 0)
        # # 위젯에 레이아웃 담기
        # btn_5_4_cellWidget.setLayout(btn_5_4_layout)

        # # horizental box를 담을 위젯 생성
        # btn_6_4_cellWidget = QWidget()
        # # 버튼을 담을 horizental box 생성
        # btn_6_4_layout = QGridLayout(btn_6_4_cellWidget)
        # self.btn_6_4_Add = QPushButton().setObjectName("추가")
        # # 레이아웃에 버튼 삽입
        # btn_6_4_layout.addWidget(self.btn_6_4_Add)
        # # 버튼 가운데로 세팅 하기 위해 마진 설정
        # btn_6_4_layout.setContentsMargins(0, 0, 0, 0)
        # # 위젯에 레이아웃 담기
        # btn_6_4_cellWidget.setLayout(btn_6_4_layout)

        # # horizental box를 담을 위젯 생성
        # btn_7_4_cellWidget = QWidget()
        # # 버튼을 담을 horizental box 생성
        # btn_7_4_layout = QGridLayout(btn_7_4_cellWidget)
        # self.btn_7_4_Add = QPushButton().setObjectName("추가")
        # # 레이아웃에 버튼 삽입
        # btn_7_4_layout.addWidget(self.btn_7_4_Add)
        # # 버튼 가운데로 세팅 하기 위해 마진 설정
        # btn_7_4_layout.setContentsMargins(0, 0, 0, 0)
        # # 위젯에 레이아웃 담기
        # btn_7_4_cellWidget.setLayout(btn_7_4_layout)

        # # horizental box를 담을 위젯 생성
        # btn_8_4_cellWidget = QWidget()
        # # 버튼을 담을 horizental box 생성
        # btn_8_4_layout = QGridLayout(btn_8_4_cellWidget)
        # self.btn_8_4_Add = QPushButton().setObjectName("추가")
        # # 레이아웃에 버튼 삽입
        # btn_8_4_layout.addWidget(self.btn_8_4_Add)
        # # 버튼 가운데로 세팅 하기 위해 마진 설정
        # btn_8_4_layout.setContentsMargins(0, 0, 0, 0)
        # # 위젯에 레이아웃 담기
        # btn_8_4_cellWidget.setLayout(btn_8_4_layout)

        # # horizental box를 담을 위젯 생성
        # btn_9_4_cellWidget = QWidget()
        # # 버튼을 담을 horizental box 생성
        # btn_9_4_layout = QGridLayout(btn_9_4_cellWidget)
        # self.btn_9_4_Add = QPushButton().setObjectName("추가")
        # # 레이아웃에 버튼 삽입
        # btn_9_4_layout.addWidget(self.btn_9_4_Add)
        # # 버튼 가운데로 세팅 하기 위해 마진 설정
        # btn_9_4_layout.setContentsMargins(0, 0, 0, 0)
        # # 위젯에 레이아웃 담기
        # btn_9_4_cellWidget.setLayout(btn_9_4_layout)

        # # horizental box를 담을 위젯 생성
        # btn_10_4_cellWidget = QWidget()
        # # 버튼을 담을 horizental box 생성
        # btn_10_4_layout = QGridLayout(btn_10_4_cellWidget)
        # self.btn_10_4_Add = QPushButton().setObjectName("추가")
        # # 레이아웃에 버튼 삽입
        # btn_10_4_layout.addWidget(self.btn_10_4_Add)
        # # 버튼 가운데로 세팅 하기 위해 마진 설정
        # btn_10_4_layout.setContentsMargins(0, 0, 0, 0)
        # # 위젯에 레이아웃 담기
        # btn_10_4_cellWidget.setLayout(btn_10_4_layout)

        # # horizental box를 담을 위젯 생성
        # btn_11_4_cellWidget = QWidget()
        # # 버튼을 담을 horizental box 생성
        # btn_11_4_layout = QGridLayout(btn_11_4_cellWidget)
        # self.btn_11_4_Add = QPushButton().setObjectName("추가")
        # # 레이아웃에 버튼 삽입
        # btn_11_4_layout.addWidget(self.btn_11_4_Add)
        # # 버튼 가운데로 세팅 하기 위해 마진 설정
        # btn_11_4_layout.setContentsMargins(0, 0, 0, 0)
        # # 위젯에 레이아웃 담기
        # btn_11_4_cellWidget.setLayout(btn_11_4_layout)
        
        # # horizental box를 담을 위젯 생성
        # btn_12_4_cellWidget = QWidget()
        # # 버튼을 담을 horizental box 생성
        # btn_12_4_layout = QGridLayout(btn_12_4_cellWidget)
        # self.btn_12_4_Add = QPushButton().setObjectName("추가")
        # # 레이아웃에 버튼 삽입
        # btn_12_4_layout.addWidget(self.btn_12_4_Add)
        # # 버튼 가운데로 세팅 하기 위해 마진 설정
        # btn_12_4_layout.setContentsMargins(0, 0, 0, 0)
        # # 위젯에 레이아웃 담기
        # btn_12_4_cellWidget.setLayout(btn_12_4_layout)

        # # horizental box를 담을 위젯 생성
        # btn_13_4_cellWidget = QWidget()
        # # 버튼을 담을 horizental box 생성
        # btn_13_4_layout = QGridLayout(btn_13_4_cellWidget)
        # self.btn_13_4_Add = QPushButton().setObjectName("추가")
        # # 레이아웃에 버튼 삽입
        # btn_13_4_layout.addWidget(self.btn_13_4_Add)
        # # 버튼 가운데로 세팅 하기 위해 마진 설정
        # btn_13_4_layout.setContentsMargins(0, 0, 0, 0)
        # # 위젯에 레이아웃 담기
        # btn_13_4_cellWidget.setLayout(btn_13_4_layout)

        # # horizental box를 담을 위젯 생성
        # btn_14_4_cellWidget = QWidget()
        # # 버튼을 담을 horizental box 생성
        # btn_14_4_layout = QGridLayout(btn_14_4_cellWidget)
        # self.btn_14_4_Add = QPushButton().setObjectName("추가")
        # # 레이아웃에 버튼 삽입
        # btn_14_4_layout.addWidget(self.btn_14_4_Add)
        # # 버튼 가운데로 세팅 하기 위해 마진 설정
        # btn_14_4_layout.setContentsMargins(0, 0, 0, 0)
        # # 위젯에 레이아웃 담기
        # btn_14_4_cellWidget.setLayout(btn_14_4_layout)


        # self.btn_1_4_Sub = QPushButton().setObjectName("제거")
        # # 레이아웃에 버튼 삽입
        # btn_1_4_layout.addWidget(self.btn_1_4_Sub)
        # # 버튼 가운데로 세팅 하기 위해 마진 설정
        # btn_1_4_layout.setContentsMargins(0, 0, 0, 0)
        # # 위젯에 레이아웃 담기
        # btn_1_4_cellWidget.setLayout(btn_1_4_layout)

        # self.btn_2_4_Sub = QPushButton().setObjectName("제거")
        # # 레이아웃에 버튼 삽입
        # btn_2_4_layout.addWidget(self.btn_1_4_Sub)
        # # 버튼 가운데로 세팅 하기 위해 마진 설정
        # btn_2_4_layout.setContentsMargins(0, 0, 0, 0)
        # # 위젯에 레이아웃 담기
        # btn_2_4_cellWidget.setLayout(btn_2_4_layout)

        # self.btn_3_4_Sub = QPushButton().setObjectName("제거")
        # # 레이아웃에 버튼 삽입
        # btn_3_4_layout.addWidget(self.btn_1_4_Sub)
        # # 버튼 가운데로 세팅 하기 위해 마진 설정
        # btn_3_4_layout.setContentsMargins(0, 0, 0, 0)
        # # 위젯에 레이아웃 담기
        # btn_3_4_cellWidget.setLayout(btn_3_4_layout)

        # self.btn_4_4_Sub = QPushButton().setObjectName("제거")
        # # 레이아웃에 버튼 삽입
        # btn_4_4_layout.addWidget(self.btn_1_4_Sub)
        # # 버튼 가운데로 세팅 하기 위해 마진 설정
        # btn_4_4_layout.setContentsMargins(0, 0, 0, 0)
        # # 위젯에 레이아웃 담기
        # btn_4_4_cellWidget.setLayout(btn_4_4_layout)

        # self.btn_5_4_Sub = QPushButton().setObjectName("제거")
        # # 레이아웃에 버튼 삽입
        # btn_5_4_layout.addWidget(self.btn_1_4_Sub)
        # # 버튼 가운데로 세팅 하기 위해 마진 설정
        # btn_5_4_layout.setContentsMargins(0, 0, 0, 0)
        # # 위젯에 레이아웃 담기
        # btn_5_4_cellWidget.setLayout(btn_5_4_layout)

        # self.btn_6_4_Sub = QPushButton().setObjectName("제거")
        # # 레이아웃에 버튼 삽입
        # btn_6_4_layout.addWidget(self.btn_1_4_Sub)
        # # 버튼 가운데로 세팅 하기 위해 마진 설정
        # btn_6_4_layout.setContentsMargins(0, 0, 0, 0)
        # # 위젯에 레이아웃 담기
        # btn_6_4_cellWidget.setLayout(btn_6_4_layout)

        # self.btn_7_4_Sub = QPushButton().setObjectName("제거")
        # # 레이아웃에 버튼 삽입
        # btn_7_4_layout.addWidget(self.btn_1_4_Sub)
        # # 버튼 가운데로 세팅 하기 위해 마진 설정
        # btn_7_4_layout.setContentsMargins(0, 0, 0, 0)
        # # 위젯에 레이아웃 담기
        # btn_7_4_cellWidget.setLayout(btn_7_4_layout)

        # self.btn_8_4_Sub = QPushButton().setObjectName("제거")
        # # 레이아웃에 버튼 삽입
        # btn_8_4_layout.addWidget(self.btn_1_4_Sub)
        # # 버튼 가운데로 세팅 하기 위해 마진 설정
        # btn_8_4_layout.setContentsMargins(0, 0, 0, 0)
        # # 위젯에 레이아웃 담기
        # btn_8_4_cellWidget.setLayout(btn_8_4_layout)

        # self.btn_9_4_Sub = QPushButton().setObjectName("제거")
        # # 레이아웃에 버튼 삽입
        # btn_9_4_layout.addWidget(self.btn_1_4_Sub)
        # # 버튼 가운데로 세팅 하기 위해 마진 설정
        # btn_9_4_layout.setContentsMargins(0, 0, 0, 0)
        # # 위젯에 레이아웃 담기
        # btn_9_4_cellWidget.setLayout(btn_9_4_layout)

        # self.btn_10_4_Sub = QPushButton().setObjectName("제거")
        # # 레이아웃에 버튼 삽입
        # btn_10_4_layout.addWidget(self.btn_1_4_Sub)
        # # 버튼 가운데로 세팅 하기 위해 마진 설정
        # btn_10_4_layout.setContentsMargins(0, 0, 0, 0)
        # # 위젯에 레이아웃 담기
        # btn_10_4_cellWidget.setLayout(btn_10_4_layout)

        # self.btn_11_4_Sub = QPushButton().setObjectName("제거")
        # # 레이아웃에 버튼 삽입
        # btn_11_4_layout.addWidget(self.btn_1_4_Sub)
        # # 버튼 가운데로 세팅 하기 위해 마진 설정
        # btn_11_4_layout.setContentsMargins(0, 0, 0, 0)
        # # 위젯에 레이아웃 담기
        # btn_11_4_cellWidget.setLayout(btn_11_4_layout)

        # self.btn_12_4_Sub = QPushButton().setObjectName("제거")
        # # 레이아웃에 버튼 삽입
        # btn_12_4_layout.addWidget(self.btn_1_4_Sub)
        # # 버튼 가운데로 세팅 하기 위해 마진 설정
        # btn_12_4_layout.setContentsMargins(0, 0, 0, 0)
        # # 위젯에 레이아웃 담기
        # btn_12_4_cellWidget.setLayout(btn_12_4_layout)

        # self.btn_13_4_Sub = QPushButton().setObjectName("제거")
        # # 레이아웃에 버튼 삽입
        # btn_13_4_layout.addWidget(self.btn_1_4_Sub)
        # # 버튼 가운데로 세팅 하기 위해 마진 설정
        # btn_13_4_layout.setContentsMargins(0, 0, 0, 0)
        # # 위젯에 레이아웃 담기
        # btn_13_4_cellWidget.setLayout(btn_13_4_layout)

        # self.btn_14_4_Sub = QPushButton().setObjectName("제거")
        # # 레이아웃에 버튼 삽입
        # btn_14_4_layout.addWidget(self.btn_1_4_Sub)
        # # 버튼 가운데로 세팅 하기 위해 마진 설정
        # btn_14_4_layout.setContentsMargins(0, 0, 0, 0)
        # # 위젯에 레이아웃 담기
        # btn_14_4_cellWidget.setLayout(btn_14_4_layout)


        # # horizental box를 담을 위젯 생성
        # btn_1_5_cellWidget = QWidget()
        # # 버튼을 담을 horizental box 생성
        # btn_1_5_layout = QGridLayout(btn_1_5_cellWidget)
        # self.btn_1_5_Del = QPushButton().setObjectName("X")
        # # 레이아웃에 버튼 삽입
        # btn_1_5_layout.addWidget(self.btn_1_5_Del)
        # # 버튼 가운데로 세팅 하기 위해 마진 설정
        # btn_1_5_layout.setContentsMargins(0, 0, 0, 0)
        # # 위젯에 레이아웃 담기
        # btn_1_5_cellWidget.setLayout(btn_1_5_layout)

        # # horizental box를 담을 위젯 생성
        # btn_2_5_cellWidget = QWidget()
        # # 버튼을 담을 horizental box 생성
        # btn_2_5_layout = QGridLayout(btn_2_5_cellWidget)
        # self.btn_2_5_Del = QPushButton().setObjectName("X")
        # # 레이아웃에 버튼 삽입
        # btn_2_5_layout.addWidget(self.btn_2_5_Del)
        # # 버튼 가운데로 세팅 하기 위해 마진 설정
        # btn_2_5_layout.setContentsMargins(0, 0, 0, 0)
        # # 위젯에 레이아웃 담기
        # btn_2_5_cellWidget.setLayout(btn_2_5_layout)

        # # horizental box를 담을 위젯 생성
        # btn_3_5_cellWidget = QWidget()
        # # 버튼을 담을 horizental box 생성
        # btn_3_5_layout = QGridLayout(btn_3_5_cellWidget)
        # self.btn_3_5_Del = QPushButton().setObjectName("X")
        # # 레이아웃에 버튼 삽입
        # btn_3_5_layout.addWidget(self.btn_3_5_Del)
        # # 버튼 가운데로 세팅 하기 위해 마진 설정
        # btn_3_5_layout.setContentsMargins(0, 0, 0, 0)
        # # 위젯에 레이아웃 담기
        # btn_3_5_cellWidget.setLayout(btn_3_5_layout)

        # # horizental box를 담을 위젯 생성
        # btn_4_5_cellWidget = QWidget()
        # # 버튼을 담을 horizental box 생성
        # btn_4_5_layout = QGridLayout(btn_4_5_cellWidget)
        # self.btn_4_5_Del = QPushButton().setObjectName("X")
        # # 레이아웃에 버튼 삽입
        # btn_4_5_layout.addWidget(self.btn_4_5_Del)
        # # 버튼 가운데로 세팅 하기 위해 마진 설정
        # btn_4_5_layout.setContentsMargins(0, 0, 0, 0)
        # # 위젯에 레이아웃 담기
        # btn_4_5_cellWidget.setLayout(btn_4_5_layout)

        # # horizental box를 담을 위젯 생성
        # btn_5_5_cellWidget = QWidget()
        # # 버튼을 담을 horizental box 생성
        # btn_5_5_layout = QGridLayout(btn_5_5_cellWidget)
        # self.btn_5_5_Del = QPushButton().setObjectName("X")
        # # 레이아웃에 버튼 삽입
        # btn_5_5_layout.addWidget(self.btn_5_5_Del)
        # # 버튼 가운데로 세팅 하기 위해 마진 설정
        # btn_5_5_layout.setContentsMargins(0, 0, 0, 0)
        # # 위젯에 레이아웃 담기
        # btn_5_5_cellWidget.setLayout(btn_5_5_layout)

        # # horizental box를 담을 위젯 생성
        # btn_6_5_cellWidget = QWidget()
        # # 버튼을 담을 horizental box 생성
        # btn_6_5_layout = QGridLayout(btn_6_5_cellWidget)
        # self.btn_6_5_Del = QPushButton().setObjectName("X")
        # # 레이아웃에 버튼 삽입
        # btn_6_5_layout.addWidget(self.btn_6_5_Del)
        # # 버튼 가운데로 세팅 하기 위해 마진 설정
        # btn_6_5_layout.setContentsMargins(0, 0, 0, 0)
        # # 위젯에 레이아웃 담기
        # btn_6_5_cellWidget.setLayout(btn_6_5_layout)

        # # horizental box를 담을 위젯 생성
        # btn_7_5_cellWidget = QWidget()
        # # 버튼을 담을 horizental box 생성
        # btn_7_5_layout = QGridLayout(btn_7_5_cellWidget)
        # self.btn_7_5_Del = QPushButton().setObjectName("X")
        # # 레이아웃에 버튼 삽입
        # btn_7_5_layout.addWidget(self.btn_7_5_Del)
        # # 버튼 가운데로 세팅 하기 위해 마진 설정
        # btn_7_5_layout.setContentsMargins(0, 0, 0, 0)
        # # 위젯에 레이아웃 담기
        # btn_7_5_cellWidget.setLayout(btn_7_5_layout)

        # # horizental box를 담을 위젯 생성
        # btn_8_5_cellWidget = QWidget()
        # # 버튼을 담을 horizental box 생성
        # btn_8_5_layout = QGridLayout(btn_8_5_cellWidget)
        # self.btn_8_5_Del = QPushButton().setObjectName("X")
        # # 레이아웃에 버튼 삽입
        # btn_8_5_layout.addWidget(self.btn_8_5_Del)
        # # 버튼 가운데로 세팅 하기 위해 마진 설정
        # btn_8_5_layout.setContentsMargins(0, 0, 0, 0)
        # # 위젯에 레이아웃 담기
        # btn_8_5_cellWidget.setLayout(btn_8_5_layout)

        # # horizental box를 담을 위젯 생성
        # btn_9_5_cellWidget = QWidget()
        # # 버튼을 담을 horizental box 생성
        # btn_9_5_layout = QGridLayout(btn_9_5_cellWidget)
        # self.btn_9_5_Del = QPushButton().setObjectName("X")
        # # 레이아웃에 버튼 삽입
        # btn_9_5_layout.addWidget(self.btn_9_5_Del)
        # # 버튼 가운데로 세팅 하기 위해 마진 설정
        # btn_9_5_layout.setContentsMargins(0, 0, 0, 0)
        # # 위젯에 레이아웃 담기
        # btn_9_5_cellWidget.setLayout(btn_9_5_layout)

        # # horizental box를 담을 위젯 생성
        # btn_10_5_cellWidget = QWidget()
        # # 버튼을 담을 horizental box 생성
        # btn_10_5_layout = QGridLayout(btn_10_5_cellWidget)
        # self.btn_10_5_Del = QPushButton().setObjectName("X")
        # # 레이아웃에 버튼 삽입
        # btn_10_5_layout.addWidget(self.btn_10_5_Del)
        # # 버튼 가운데로 세팅 하기 위해 마진 설정
        # btn_10_5_layout.setContentsMargins(0, 0, 0, 0)
        # # 위젯에 레이아웃 담기
        # btn_10_5_cellWidget.setLayout(btn_10_5_layout)

        # # horizental box를 담을 위젯 생성
        # btn_11_5_cellWidget = QWidget()
        # # 버튼을 담을 horizental box 생성
        # btn_11_5_layout = QGridLayout(btn_11_5_cellWidget)
        # self.btn_11_5_Del = QPushButton().setObjectName("X")
        # # 레이아웃에 버튼 삽입
        # btn_11_5_layout.addWidget(self.btn_11_5_Del)
        # # 버튼 가운데로 세팅 하기 위해 마진 설정
        # btn_11_5_layout.setContentsMargins(0, 0, 0, 0)
        # # 위젯에 레이아웃 담기
        # btn_11_5_cellWidget.setLayout(btn_11_5_layout)

        # # horizental box를 담을 위젯 생성
        # btn_12_5_cellWidget = QWidget()
        # # 버튼을 담을 horizental box 생성
        # btn_12_5_layout = QGridLayout(btn_12_5_cellWidget)
        # self.btn_12_5_Del = QPushButton().setObjectName("X")
        # # 레이아웃에 버튼 삽입
        # btn_12_5_layout.addWidget(self.btn_12_5_Del)
        # # 버튼 가운데로 세팅 하기 위해 마진 설정
        # btn_12_5_layout.setContentsMargins(0, 0, 0, 0)
        # # 위젯에 레이아웃 담기
        # btn_12_5_cellWidget.setLayout(btn_12_5_layout)

        # # horizental box를 담을 위젯 생성
        # btn_13_5_cellWidget = QWidget()
        # # 버튼을 담을 horizental box 생성
        # btn_13_5_layout = QGridLayout(btn_13_5_cellWidget)
        # self.btn_13_5_Del = QPushButton().setObjectName("X")
        # # 레이아웃에 버튼 삽입
        # btn_13_5_layout.addWidget(self.btn_13_5_Del)
        # # 버튼 가운데로 세팅 하기 위해 마진 설정
        # btn_13_5_layout.setContentsMargins(0, 0, 0, 0)
        # # 위젯에 레이아웃 담기
        # btn_13_5_cellWidget.setLayout(btn_13_5_layout)

        # # horizental box를 담을 위젯 생성
        # btn_14_5_cellWidget = QWidget()
        # # 버튼을 담을 horizental box 생성
        # btn_14_5_layout = QGridLayout(btn_14_5_cellWidget)
        # self.btn_14_5_Del = QPushButton().setObjectName("X")
        # # 레이아웃에 버튼 삽입
        # btn_14_5_layout.addWidget(self.btn_14_5_Del)
        # # 버튼 가운데로 세팅 하기 위해 마진 설정
        # btn_14_5_layout.setContentsMargins(0, 0, 0, 0)
        # # 위젯에 레이아웃 담기
        # btn_14_5_cellWidget.setLayout(btn_14_5_layout)


        # self.tableWidget.cellWidget(0, 4).layout().addChildWidget = QPushButton("Btn_0_4_Add")
        # self.tableWidget.cellWidget(0, 4).layout().QPushButton("Btn_0_4_Del")

        self.verticalLayout_20.addWidget(self.tableView)

        self.stackedWidget.addWidget(self.new_page)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setBold(False)
        font6.setItalic(False)
        self.creditsLabel.setFont(font6)
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\uc800\uad6c\uba85\ud488\uaf48\ubc30\uae30 \uacc4\uc0b0 \ud0a4\uc624\uc2a4\ud06c", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"PyDracula", None))
        self.titleLeftDescription.setText("")
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_calender.setText(QCoreApplication.translate("MainWindow", u"Widgets", None))
        self.btn_chart.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"\uc800\uad6c\uba85\ud488\uaf48\ubc30\uae30 \uacc4\uc0b0 \ud0a4\uc624\uc2a4\ud06c", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\ud569\uacc4 : ", None))
        self.btn_hotamericano.setText(QCoreApplication.translate("MainWindow", u"\ub530\ub73b\ud55c \uc544\uba54\ub9ac\uce74\ub178", None))
        self.btn_cheeseball.setText(QCoreApplication.translate("MainWindow", u"\uce58\uc988\ubcfc", None))
        self.btn_peach.setText(QCoreApplication.translate("MainWindow", u"\ubcf5\uc22d\uc544 \uc544\uc774\uc2a4\ud2f0", None))
        self.btn_brezel.setText(QCoreApplication.translate("MainWindow", u"\uaf48\ubc30\uae30", None))
        self.btn_donuts.setText(QCoreApplication.translate("MainWindow", u"\ub3c4\ub108\uce20", None))
        self.btn_dinoagg.setText(QCoreApplication.translate("MainWindow", u"\uacf5\ub8e1\uc54c(4\uac1c)", None))
        self.btn_hotdog.setText(QCoreApplication.translate("MainWindow", u"\ud56b\ub3c4\uadf8", None))
        self.btn_plum.setText(QCoreApplication.translate("MainWindow", u"\ub9e4\uc2e4 \uc544\uc774\uc2a4\ud2f0", None))
        self.btn_americano.setText(QCoreApplication.translate("MainWindow", u"\uc544\uc774\uc2a4 \uc544\uba54\ub9ac\uce74\ub178", None))
        self.btn_pomegranate.setText(QCoreApplication.translate("MainWindow", u"\uc11d\ub958 \uc544\uc774\uc2a4\ud2f0", None))
        self.btn_brezel_set.setText(QCoreApplication.translate("MainWindow", u"\uaf48\ubc30\uae30(3\uac1c)", None))
        self.btn_blueberries.setText(QCoreApplication.translate("MainWindow", u"\ube14\ub8e8\ubca0\ub9ac \uc544\uc774\uc2a4\ud2f0", None))
        self.btn_coke.setText(QCoreApplication.translate("MainWindow", u"\ucf5c\ub77c", None))
        self.btn_cider.setText(QCoreApplication.translate("MainWindow", u"\uc0ac\uc774\ub2e4", None))
        self.btn_Fanta.setText(QCoreApplication.translate("MainWindow", u"\ud658\ud0c0", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\uc81c\ud488\uba85", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\uac00\uaca9", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\uac1c\uc218", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\ucd1d \uac00\uaca9", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\ucd94\uac00/\uc81c\uac70", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\uc0ad\uc81c", None));
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: ParkSeongHyeon", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v0.0.1", None))
    # retranslateUi