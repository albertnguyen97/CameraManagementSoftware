import sys
import cv2
import numpy as np
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtCore import QTimer

class VideoCaptureApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Thiết lập giao diện
        self.setWindowTitle("RTSP Stream Viewer")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.video_label = QLabel()
        self.video_label.setScaledContents(True)  # Cho phép tự động điều chỉnh kích thước
        self.layout.addWidget(self.video_label)

        self.start_button = QPushButton("Bắt đầu")
        self.start_button.clicked.connect(self.start_stream)
        self.layout.addWidget(self.start_button)

        self.stop_button = QPushButton("Dừng lại")
        self.stop_button.clicked.connect(self.stop_stream)
        self.layout.addWidget(self.stop_button)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)

        self.cap = None

    def start_stream(self):
        self.cap = cv2.VideoCapture("rtsp://admin:abcd1234@192.168.1.84/cam/realmonitor?channel=2&subtype=0&unicast=true&proto=Onvif")
        if not self.cap.isOpened():
            print("Không thể mở video stream")
            return
        self.timer.start(20)  # Thay đổi tần suất cập nhật khung hình (20 ms)

    def stop_stream(self):
        if self.cap is not None:
            self.cap.release()
            self.cap = None
        self.timer.stop()
        self.video_label.clear()

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            # Chuyển đổi BGR (OpenCV) sang RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Chuyển đổi sang QImage
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            q_img = QImage(frame.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
            # Cập nhật QLabel
            self.video_label.setPixmap(QPixmap.fromImage(q_img))
            # Cập nhật kích thước của QLabel
            self.video_label.setFixedSize(1000, 700)  # Đặt kích thước cho video

    def closeEvent(self, event):
        self.stop_stream()  # Dừng stream khi đóng cửa sổ
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VideoCaptureApp()
    window.show()
    sys.exit(app.exec())
