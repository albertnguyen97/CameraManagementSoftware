import sys
import vlc
from PyQt6 import QtWidgets, QtCore

class VideoPlayer(QtWidgets.QWidget):
    def __init__(self, rtsp_url):
        super().__init__()

        # Thiết lập kích thước và tên của widget
        self.setWindowTitle("VLC Video Player")
        self.setMinimumSize(400, 300)  # Kích thước cho từng khung video

        # Tạo trình phát VLC
        self.vlc_instance = vlc.Instance()
        self.media_player = self.vlc_instance.media_player_new()

        # Tạo layout
        self.container = QtWidgets.QVBoxLayout(self)

        # Khung chứa video
        self.video_frame = QtWidgets.QFrame(self)
        self.container.addWidget(self.video_frame)

        # Thiết lập khung chứa video
        self.video_frame.setMinimumSize(400, 300)
        self.media_player.set_hwnd(self.video_frame.winId())  # Chỉ định khung cho VLC

        self.rtsp_url = rtsp_url

    def play_video(self):
        # Mở video từ nguồn RTSP với tùy chọn 'rtsp-tcp'
        self.vlc_instance = vlc.Instance("--avcodec-hw=any")  # Kích hoạt tăng tốc phần cứng
        media = self.vlc_instance.media_new(self.rtsp_url, ":rtsp-tcp")  # Thêm tùy chọn ':rtsp-tcp'
        self.media_player.set_media(media)
        self.media_player.play()

class MainWindow(QtWidgets.QWidget):
    def __init__(self, rtsp_urls):
        super().__init__()

        self.setWindowTitle("20 Camera Grid")
        self.setGeometry(100, 100, 1600, 1200)  # Tăng kích thước cửa sổ để phù hợp với nhiều camera hơn

        # Tạo GridLayout cho 20 camera
        self.grid_layout = QtWidgets.QGridLayout(self)        # Tạo các VideoPlayer cho từng camera
        self.video_players = []
        for idx, url in enumerate(rtsp_urls):
            player = VideoPlayer(url)
            self.video_players.append(player)

            # Thêm mỗi camera vào trong grid (4x5 lưới)
            row, col = divmod(idx, 5)
            self.grid_layout.addWidget(player, row, col)

        # Phát video từ các camera
        for player in self.video_players:
            player.play_video()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # Danh sách 20 URL RTSP từ các camera
    rtsp_urls = [
        "RTSP here"
    ]

    # Tạo cửa sổ chính
    window = MainWindow(rtsp_urls)
    window.show()

    sys.exit(app.exec())
