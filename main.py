import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Back',self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction("Forward", self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction("Reload", self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)


        self.address_bar = QLineEdit()
        self.address_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.address_bar)

        self.address_bar = QLineEdit()
        self.address_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.address_bar)


        self.setStyleSheet("background-color: #8b008b;")

        self.browser.loadFinished.connect(self.apply_fade_in_effect)

        self.add_home_page_shortcuts()

    def add_home_page_shortcuts(self):
        shortcuts = {
            "YouTube": "https://www.youtube.com",
            "Twitter": "https://www.twitter.com",
            # Add more shortcuts here if needed
        }

        for name, url in shortcuts.items():
            shortcut_btn = QPushButton(name)
            shortcut_btn.clicked.connect(lambda _, url=url: self.browser.setUrl(QUrl(url)))
            self.centralWidget().layout().addWidget(shortcut_btn)

    def apply_fade_in_effect(self):

        animation = QPropertyAnimation(self.browser, b"opacity")
        animation.setDuration(1000)
        animation.setStartValue(0.0)
        animation.setEndValue(1.0)
        animation.start(QPropertyAnimation.DeleteWhenStopped)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://zworld.com'))
    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))




if __name__ == "__main__":
    app = QApplication(sys.argv)
    QApplication.setApplicationName('Z world')
    window = MainWindow()
    app.exec_()
