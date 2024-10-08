import sys
import av
from PyQt6.QtCore import QThread, pyqtSignal, Qt
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QImage, QPixmap


class VideoStreamThread(QThread):
    frame_captured = pyqtSignal(QImage)

    def __init__(self, rtsp_url):
        super().__init__()
        self.rtsp_url = rtsp_url
        self.running = True

    def run(self):
        container = av.open(self.rtsp_url)
        while self.running:
            try:
                for frame in container.decode(video=0):
                    img = frame.to_image().convert("RGB")
                    width, height = img.size
                    qimg = QImage(img.tobytes(), width, height, QImage.Format.Format_RGB888)
                    self.frame_captured.emit(qimg)  # Emit the captured frame
                    break  # Only process one frame per iteration
            except Exception as e:
                print(f"Error: {e}")
                break

    def stop(self):
        self.running = False
        self.quit()
        self.wait()


class VideoStreamWidget(QWidget):
    def __init__(self, rtsp_url):
        super().__init__()

        self.video_label = QLabel(self)
        self.video_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.video_label)
        self.setLayout(layout)

        # Start video stream thread
        self.video_thread = VideoStreamThread(rtsp_url)
        self.video_thread.frame_captured.connect(self.update_frame)
        self.video_thread.start()

    def update_frame(self, qimg):
        # Convert QImage to QPixmap and set to QLabel
        self.video_label.setPixmap(QPixmap.fromImage(qimg))

    def closeEvent(self, event):
        self.video_thread.stop()  # Stop the thread when closing the window
        event.accept()


def main():
    app = QApplication(sys.argv)

    # Set the RTSP URL here
    rtsp_url = "rtsp here"

    widget = VideoStreamWidget(rtsp_url)
    widget.setWindowTitle("RTSP Stream Viewer")
    widget.resize(640, 480)
    widget.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
