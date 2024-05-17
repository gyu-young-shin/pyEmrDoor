# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EMRDoor.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QDockWidget, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)
import emrdoor_imag_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1195, 900)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/image/image/link.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.actionConnect = QAction(MainWindow)
        self.actionConnect.setObjectName(u"actionConnect")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 981, 61))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.pushButton_3 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        font = QFont()
        font.setBold(True)
        self.pushButton_3.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/image/image/free-icon-gears-416153.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/image/image/stop-button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u":/image/image/free-icon-right-arrows-6776011.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_5 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font)
        icon4 = QIcon()
        icon4.addFile(u":/image/image/free-icon-location-pin-8259448.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.pushButton_5)

        self.eventBt = QPushButton(self.horizontalLayoutWidget)
        self.eventBt.setObjectName(u"eventBt")
        self.eventBt.setFont(font)
        icon5 = QIcon()
        icon5.addFile(u":/image/image/free-icon-log-file-format-8760478.png", QSize(), QIcon.Normal, QIcon.Off)
        self.eventBt.setIcon(icon5)
        self.eventBt.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.eventBt)

        self.OpenAllBt = QPushButton(self.horizontalLayoutWidget)
        self.OpenAllBt.setObjectName(u"OpenAllBt")
        self.OpenAllBt.setFont(font)
        icon6 = QIcon()
        icon6.addFile(u":/image/image/free-icon-door-9050998.png", QSize(), QIcon.Normal, QIcon.Off)
        self.OpenAllBt.setIcon(icon6)
        self.OpenAllBt.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.OpenAllBt)

        self.ByeBt = QPushButton(self.horizontalLayoutWidget)
        self.ByeBt.setObjectName(u"ByeBt")
        self.ByeBt.setFont(font)
        icon7 = QIcon()
        icon7.addFile(u":/image/image/free-icon-end-5129674.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ByeBt.setIcon(icon7)
        self.ByeBt.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.ByeBt)

        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(150, 130, 711, 251))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(20, 10, 20, 10)
        self.label_9 = QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setPixmap(QPixmap(u":/image/image/RedOff.png"))
        self.label_9.setScaledContents(True)

        self.gridLayout.addWidget(self.label_9, 0, 4, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setPixmap(QPixmap(u":/image/image/RedOff.png"))
        self.label_7.setScaledContents(True)

        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setPixmap(QPixmap(u":/image/image/RedOff.png"))
        self.label_6.setScaledContents(True)

        self.gridLayout.addWidget(self.label_6, 1, 1, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setPixmap(QPixmap(u":/image/image/RedOff.png"))
        self.label_5.setScaledContents(True)

        self.gridLayout.addWidget(self.label_5, 1, 6, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setPixmap(QPixmap(u":/image/image/RedOff.png"))
        self.label_4.setScaledContents(True)

        self.gridLayout.addWidget(self.label_4, 1, 4, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u":/image/image/GreenOn.png"))
        self.label_3.setScaledContents(True)

        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setPixmap(QPixmap(u":/image/image/RedOff.png"))
        self.label_8.setScaledContents(True)

        self.gridLayout.addWidget(self.label_8, 1, 5, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/image/image/RedOff.png"))
        self.label.setScaledContents(True)

        self.gridLayout.addWidget(self.label, 1, 3, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setPixmap(QPixmap(u":/image/image/RedOff.png"))
        self.label_10.setScaledContents(True)

        self.gridLayout.addWidget(self.label_10, 1, 0, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setPixmap(QPixmap(u":/image/image/RedOff.png"))
        self.label_11.setScaledContents(True)

        self.gridLayout.addWidget(self.label_11, 0, 1, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setPixmap(QPixmap(u":/image/image/RedOff.png"))
        self.label_12.setScaledContents(True)

        self.gridLayout.addWidget(self.label_12, 0, 2, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setPixmap(QPixmap(u":/image/image/RedOff.png"))
        self.label_13.setScaledContents(True)

        self.gridLayout.addWidget(self.label_13, 0, 3, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setPixmap(QPixmap(u":/image/image/RedOff.png"))
        self.label_14.setScaledContents(True)

        self.gridLayout.addWidget(self.label_14, 2, 0, 1, 1)

        self.label_15 = QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setPixmap(QPixmap(u":/image/image/RedOff.png"))
        self.label_15.setScaledContents(True)

        self.gridLayout.addWidget(self.label_15, 3, 0, 1, 1)

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 9):
            self.tableWidget.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
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
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(30, 90, 941, 631))
        self.tableWidget.setFont(font)
        self.tableWidget.setFrameShape(QFrame.Shape.Box)
        self.tableWidget.setFrameShadow(QFrame.Shadow.Plain)
        self.tableWidget.setLineWidth(3)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.tableWidget.setAutoScrollMargin(26)
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setIconSize(QSize(4, 4))
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.PenStyle.DotLine)
        self.tableWidget.setSortingEnabled(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.tableWidget.raise_()
        self.horizontalLayoutWidget.raise_()
        self.gridLayoutWidget.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget_2 = QDockWidget(MainWindow)
        self.dockWidget_2.setObjectName(u"dockWidget_2")
        self.dockWidget_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.dockWidget_2.sizePolicy().hasHeightForWidth())
        self.dockWidget_2.setSizePolicy(sizePolicy)
        self.dockWidget_2.setMinimumSize(QSize(200, 150))
        self.dockWidget_2.setMaximumSize(QSize(200, 150))
        palette = QPalette()
        self.dockWidget_2.setPalette(palette)
        self.dockWidget_2.setAutoFillBackground(False)
        self.dockWidget_2.setStyleSheet(u"\n"
"dockWidget_2{background-color:green;}\n"
"")
        self.dockWidget_2.setFloating(True)
        self.dockWidget_2.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)
        self.dockWidget_2.setAllowedAreas(Qt.DockWidgetArea.NoDockWidgetArea)
        self.dockWidgetContents_2 = QWidget()
        self.dockWidgetContents_2.setObjectName(u"dockWidgetContents_2")
        self.comboBox = QComboBox(self.dockWidgetContents_2)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(100, 40, 91, 21))
        self.label_2 = QLabel(self.dockWidgetContents_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 40, 61, 21))
        self.label_2.setFont(font)
        self.pushButton_4 = QPushButton(self.dockWidgetContents_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(60, 90, 75, 24))
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.dockWidget_2)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\ube44\uc0c1\ubb38 \ubaa8\ub2c8\ud130\ub9c1 \uc2dc\uc2a4\ud15c", None))
        self.actionConnect.setText(QCoreApplication.translate("MainWindow", u"\uc5f0\uacb0", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\ud1b5\uc2e0 \uc124\uc815", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u" \uc815 \uc9c0", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u" \uc2dc \uc791", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\uc704\uce58 \uc124\uc815", None))
        self.eventBt.setText(QCoreApplication.translate("MainWindow", u" \uc774 \ubca4 \ud2b8", None))
        self.OpenAllBt.setText(QCoreApplication.translate("MainWindow", u"\uc804\uccb4 \uac1c\ubc29", None))
        self.ByeBt.setText(QCoreApplication.translate("MainWindow", u" \uc885 \ub8cc", None))
        self.label_9.setText("")
        self.label_7.setText("")
        self.label_6.setText("")
        self.label_5.setText("")
        self.label_4.setText("")
        self.label_3.setText("")
        self.label_8.setText("")
        self.label.setText("")
        self.label_10.setText("")
        self.label_11.setText("")
        self.label_12.setText("")
        self.label_13.setText("")
        self.label_14.setText("")
        self.label_15.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\uc704 \uce58 ", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\ub3c4\uc5b4", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\ub2e8\uc120", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\uc815\uc804", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\ubc29\uc804", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\ucee4\ubc84", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\ud654\uc7ac", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\ube44\uc0c1", None));
#if QT_CONFIG(whatsthis)
        self.dockWidget_2.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.dockWidget_2.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.dockWidget_2.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.dockWidget_2.setWindowTitle(QCoreApplication.translate("MainWindow", u"\uc124\uc815 ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\ud3ec\ud2b8 \uc120\ud0dd :", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\ud655\uc778", None))
    # retranslateUi

