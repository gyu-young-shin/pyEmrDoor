import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog,QTableWidgetItem, QTableWidget,QVBoxLayout, QLabel, QWidget,QCheckBox
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QThread, Signal,Qt, QSize
from EMRDoor_ui import Ui_MainWindow
from PySide6.QtGui import QPixmap, QIcon

import serial
import serial.tools.list_ports
import emrdoor_imag_rc
from EMRDoor01_ui import Ui_Dialog  # 변환된 EMRDoor01.py 파일을 import

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


class SubDialog(QDialog):

    row_changed = Signal(int)  # Custom signal to notify row change

    def __init__(self,rowcnt):
        super(SubDialog, self).__init__()
        self.rowcnt1 = rowcnt
   
        self.ut = Ui_Dialog()
        self.ut.setupUi(self)

        self.ut.pushButton.clicked.connect(self.change_row_and_close_dialog)
        self.ut.pushButton_2.clicked.connect(self.close)

        self.ut.spinBox.setValue(rowcnt)  # Set the value of the spin box
        self.ut.spinBox.valueChanged.connect(self.update_rowcnt)
     
    def update_rowcnt(self, value):
        # Update the rowcnt with the new value
        self.rowcnt1 = int(value)
        print(self.rowcnt1)
    
   
    def change_row_and_close_dialog(self):
        # Perform the desired action, e.g., changing the row
        self.row_changed.emit(self.rowcnt1)
        print("chageed good")
        # Close the dialog
        # self.close()

class SerialReadThread(QThread):
    data_received = Signal(str)

    def __init__(self, serial_connection):
        super().__init__()
        self.serial_connection = serial_connection
        self._running = True

    def run(self):
        while self._running:
            try:
                if self.serial_connection.in_waiting > 0:
                    data = self.serial_connection.read(self.serial_connection.in_waiting)
                    hex_data = data.hex().upper()  # Convert to hex string and make uppercase
                    self.data_received.emit(hex_data)
            except serial.SerialException:
                self._running = False
                self.data_received.emit("Disconnected")

    def stop(self):
        self._running = False
        self.serial_connection.close()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 상태바 추가
        self.statusBar().showMessage("Ready")
        self.statusBar().setStyleSheet("QStatusBar{background-color: rgb(172, 157, 255) ;}")
        
        
        # 버튼 클릭 시 호출할 슬롯 연결
        self.ui.pushButton.clicked.connect(self.on_button_click)
        self.ui.pushButton_2.clicked.connect(self.close_serial)
        self.ui.pushButton_3.clicked.connect(self.setting_serial)
        self.ui.pushButton_4.clicked.connect(self. setting_serial)
        self.ui.pushButton_5.clicked.connect(self. uiopen)
        self.ui.OpenAllBt.clicked.connect(self. sendAllDoorOpen)
        self.ui.ByeBt.clicked.connect(self. close)
        
        # self.ui.tableWidget
        

                # self.ui.tableWidget.setColumnWidth(j, desired_size.width())

        # checkBox = QCheckBox()
        # widget = QWidget()


        # layout = QVBoxLayout(widget)
        # layout.addWidget(checkBox)
        # layout.setAlignment(Qt.alignCenter)
        # layout.setContentsMargins(0,0,0,0)

        # self.ui.tableWidget.setCellWidget(0, 1, label)

        # self.ui.tableWidget.setLayout(layout)
        # layout.setAlignment(Qt.AlignCenter)  # Center the label within the widget

        
        # Adjust the row and column sizes to fit the label
   
<<<<<<< HEAD

        # Insert the QLabel into the QTableWidget at position (0, 0)
        # self.ui.tableWidget.setCellWidget(0, 0, label)
        

        # update_label_size(self.ui.tableWidget, 0, 0, label, pixmap)
        # icon = QIcon(scaled_pixmap)
        # # Set the icon in the table widget item
        # self.item.setIcon(icon)
        # self.ui.tableWidget.setItem(0, 0, self.item)
        # self.ui.tableWidget.setRowHeight(0, desired_size.height())
        # self.ui.tableWidget.setColumnWidth(0, desired_size.width())

        self.ui.tableWidget.setRowCount(12)


       
        for i in range(12):
            for j in range( 8):
                # self.item = QTableWidgetItem()
                pixmap = QPixmap(u":/image/image/RedOff.png")  # Replace with the path to your image
                # Scale the pixmap to the desired size, for example, 32x32
                desired_size = QSize(40, 40)
                scaled_pixmap = pixmap.scaled(desired_size, Qt.KeepAspectRatio)

                label = QLabel()
                # label.setFixedSize(150, 150)  # QLabel의 크기를 200x200으로 설정
                label.setPixmap(scaled_pixmap)
                label.setAlignment(Qt.AlignCenter)
                # label.setContentsMargins(5,5,5,5)
                self.ui.tableWidget.setCellWidget(i, j, label)
                self.ui.tableWidget.setRowHeight(i, desired_size.height()+5)
=======
        self.item = QTableWidgetItem()
        pixmap = QPixmap(u":/image/image/RedOff.png")  # Replace with the path to your image
        self.item.setIcon(QIcon(pixmap))
        self.item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)  # Center the item in the cell
        self.ui.tableWidget.setItem(0, 1, self.item)
        self.ui.tableWidget.setIconSize(QSize(32, 32))  # Set icon size
        self.ui.tableWidget.setRowHeight(0, 40)  # Set row height
        self.ui.tableWidget.setColumnWidth(1, 40)  # Set column width

        # Additionally, if you want to center the icon itself, set the horizontal and vertical alignment of the item:
        self.ui.tableWidget.item(0, 1).setTextAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
>>>>>>> eb94b4c7a8cb73d97e5730e6117a92f534196ecc

        
        # 버튼 Enable setting 
        self.ui.OpenAllBt.setEnabled(False)

        # ComboBox에 COM 포트 목록 추가
        self.populate_com_ports()
        self.ui.pushButton_2.hide()
        self.ui.dockWidget_2.hide()

        # 시리얼 객체 초기화
        self.serial_connection = None
        self.serial_thread = None

    def on_button_click(self):

        selected_port = self.ui.comboBox.currentText()
        if selected_port:
            self.connect_to_com_port(selected_port)
            self.ui.pushButton.hide()
            self.ui.pushButton_2.show()
            
        else:
            self.statusBar().showMessage("Please select a COM port", 2000)
            QMessageBox.warning(self, "Warning", "Please select a COM port")

    def populate_com_ports(self):
        ports = serial.tools.list_ports.comports()
        for port in ports:
            self.ui.comboBox.addItem(port.device)

    def connect_to_com_port(self, port_name):
        try:
            self.serial_connection = serial.Serial(port_name, baudrate=9600, timeout=1)
            self.statusBar().showMessage(f"Connected to {port_name}")
            # QMessageBox.information(self, "Success", f"Connected to {port_name}")

            # 시리얼 읽기 쓰레드 시작
            self.serial_thread = SerialReadThread(self.serial_connection)
            self.serial_thread.data_received.connect(self.handle_serial_data)
            self.serial_thread.start()
            
            # Enable setting 
            self.ui.pushButton_3.setEnabled(False)
            self.ui.OpenAllBt.setEnabled(True)
        except serial.SerialException as e:
            self.statusBar().showMessage(f"Failed to connect to {port_name}", 2000)
            QMessageBox.critical(self, "Error", f"Failed to connect to {port_name}\n{str(e)}")

    def handle_serial_data(self, data):
        if data == "Disconnected":
            self.statusBar().showMessage("Disconnected from COM port", 2000)
            QMessageBox.critical(self, "Error", "Disconnected from COM port")
            if self.serial_thread:
                self.serial_thread.stop()
                self.serial_thread = None
            self.serial_connection = None
        else:
            print(f"Received data: {data}")

        
    # 시리얼 통신 종료 
    def close_serial(self):
        if self.serial_thread and self.serial_thread.isRunning():
            self.serial_thread.stop()
            self.serial_thread.wait()
        if self.serial_connection and self.serial_connection.is_open:
            self.serial_connection.close()

        self.ui.pushButton.show()
        self.ui.pushButton_2.hide()
        #button Enable setting 
        self.ui.pushButton_3.setEnabled(True)
        self.ui.OpenAllBt.setEnabled(False)
        
        self.statusBar().showMessage(f"Disconnected from COM port ", 2000)
    
    def sendAllDoorOpen(self):
        print(f"all Door Open")
        
    def setting_serial(self):
        if self.ui.dockWidget_2.isVisible():
            self.ui.dockWidget_2.hide()
            self.ui.pushButton_3.setEnabled(True)
            self.ui.pushButton.setEnabled(True)
        else:
            self.ui.dockWidget_2.show()
            self.ui.pushButton_3.setEnabled(False)
            self.ui.pushButton.setEnabled(False)


    def uiopen(self):
        try:
            rowcnt = self.ui.tableWidget.rowCount()
            self.dialog = SubDialog(rowcnt)
            self.dialog.row_changed.connect(self.update_table_row)  # Connect signal to slot
            self.dialog.exec()
            
        except Exception as e:
            print("An error occurred:", e)
        
    def update_table_row(self, row_changed):
        self.ui.tableWidget.setRowCount(row_changed)  # Update the table row count
        print(row_changed)
        self.dialog.close()

        for i in range( row_changed):
            for j in range( 8):
                # self.item = QTableWidgetItem()
                pixmap = QPixmap(u":/image/image/RedOff.png")  # Replace with the path to your image
                # Scale the pixmap to the desired size, for example, 32x32
                desired_size = QSize(40, 40)
                scaled_pixmap = pixmap.scaled(desired_size, Qt.KeepAspectRatio)

                label = QLabel()
                # label.setFixedSize(150, 150)  # QLabel의 크기를 200x200으로 설정
                label.setPixmap(scaled_pixmap)
                label.setAlignment(Qt.AlignCenter)
                # label.setContentsMargins(5,5,5,5)
                self.ui.tableWidget.setCellWidget(i, j, label)
                self.ui.tableWidget.setRowHeight(i, desired_size.height()+5)

        
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
