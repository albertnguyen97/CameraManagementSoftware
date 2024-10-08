import sys
from PyQt6 import QtWidgets, QtCore, QtMultimedia, QtMultimediaWidgets

class VideoPlayer(QtWidgets.QWidget):
    def __init__(self, mrl):
        super().__init__()

        self.setWindowTitle("Video Player with QMediaPlayer")
        self.setGeometry(100, 100, 800, 600)

        # Create a QVBoxLayout
        self.layout = QtWidgets.QVBoxLayout(self)

        # Create a QVideoWidget for displaying video
        self.video_widget = QtMultimediaWidgets.QVideoWidget(self)
        self.layout.addWidget(self.video_widget)

        # Create a QMediaPlayer
        self.media_player = QtMultimedia.QMediaPlayer(self)
        self.media_player.setVideoOutput(self.video_widget)

        # Set the media to be played using setSource
        self.media_player.setSource(QtCore.QUrl(mrl))

        # Create a Play button
        self.play_button = QtWidgets.QPushButton("Play", self)
        self.play_button.clicked.connect(self.play_video)
        self.layout.addWidget(self.play_button)

    def play_video(self):
        self.media_player.play()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # Set the RTSP URL or any other media URL you want to play
    rtsp_url = "RTSP here"  # Replace with your RTSP URL
    player = VideoPlayer(rtsp_url)

    player.show()
    sys.exit(app.exec())
