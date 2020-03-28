import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

# from custom.stackedWidget import StackedWidget
from custom.treeView import FileSystemTreeView
from custom.videoPlayer import videoPlayer
from custom.modelwidgets import ReListWidget, FuncListWidget
from custom.customwidgets import MyLed

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()


        '以下是对主布局各部分分别实例化并设置属性'
        self.funcListWidget = FuncListWidget(self)   # 表示功能菜单
        self.fileSystemTreeView = FileSystemTreeView(self)  # 表示文件目录
        self.videoPlayer = videoPlayer(self)   # 视频播放器
        self.resultlist = ReListWidget(self)

        self.dock_file = QDockWidget(self)
        self.dock_file.setWidget(self.fileSystemTreeView)
        self.dock_file.setTitleBarWidget(QLabel('目录'))
        self.dock_file.setFeatures(QDockWidget.NoDockWidgetFeatures)

        self.dock_func = QDockWidget(self)
        self.dock_func.setWidget(self.funcListWidget)
        self.dock_func.setTitleBarWidget(QLabel('功能选项'))
        self.dock_func.setFeatures(QDockWidget.NoDockWidgetFeatures)

        self.dock_result = QDockWidget(self)
        self.dock_result.setWidget(self.resultlist)
        self.dock_result.setTitleBarWidget(QLabel('输出结果'))
        self.dock_result.setFeatures(QDockWidget.NoDockWidgetFeatures)

        '主页面布局'
        self.videoPlayer.player.setMedia(QMediaContent(QUrl("https://gss3.baidu.com/6LZ0ej3k1Qd3ote6lo7D0j9wehsv/tieba-smallvideo/60_24e01d9734b6b1cb51a9148ead8940c0.mp4")))
        self.setCentralWidget(self.videoPlayer)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock_file)
        self.addDockWidget(Qt.TopDockWidgetArea, self.dock_func)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock_result)
        self.led = MyLed()
        self.dock_led = QDockWidget(self)
        self.dock_led.setWidget(self.led)
        self.dock_led.setTitleBarWidget(QLabel('指示灯'))
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock_led)

        '设置标题栏样式'
        self.setWindowTitle('视频播放器')
        self.setWindowIcon(QIcon('icons/main.png'))

        '全局会用到的资源文件'
        self.src_img = None
        self.cur_img = None
        self.src_video = None


    '更改视频播放器的源'
    def changevideo(self, video):
        self.src_video = video
        self.videoPlayer.getfile(self.src_video)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(open('./custom/styleSheet.qss', encoding='utf-8').read())
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
