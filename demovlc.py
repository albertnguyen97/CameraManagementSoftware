import sys
import vlc
from PyQt6 import QtWidgets, QtCore

class VideoPlayer(QtWidgets.QWidget):
    def __init__(self, rtsp_url):
        super().__init__()

        self.setWindowTitle("VLC Video Player")
        self.setGeometry(100, 100, 800, 600)

        # Tạo trình phát VLC
        self.vlc_instance = vlc.Instance()
        self.media_player = self.vlc_instance.media_player_new()

        # Tạo layout
        self.container = QtWidgets.QVBoxLayout(self)

        # Tạo nút phát video
        self.play_button = QtWidgets.QPushButton("Play Video")
        self.play_button.clicked.connect(self.play_video)
        self.container.addWidget(self.play_button)

        # Khung chứa video
        self.video_frame = QtWidgets.QFrame(self)
        self.container.addWidget(self.video_frame)

        # Thiết lập kích thước cho khung chứa video
        self.video_frame.setMinimumSize(800, 600)
        self.media_player.set_hwnd(self.video_frame.winId())  # Chỉ định khung cho VLC

        self.rtsp_url = rtsp_url

    def play_video(self):
        # Mở video từ nguồn RTSP
        media = self.vlc_instance.media_new(self.rtsp_url)
        self.media_player.set_media(media)
        self.media_player.play()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    rtsp_url = "RTSP here"  # Thay thế bằng URL RTSP của bạn
    player = VideoPlayer(rtsp_url)
    player.show()
    sys.exit(app.exec())
