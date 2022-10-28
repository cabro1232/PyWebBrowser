import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QToolBar, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize, QUrl
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GodSpeed Search")
        self.setWindowIcon(QIcon("Icons/browser.png"))
        self.setGeometry(200, 200, 900, 600)

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        self.backButton = QPushButton()
        self.backButton.setIcon(QIcon("Icons/left-arrow.png"))
        self.backButton.setIconSize(QSize(36, 36))
        self.backButton.clicked.connect(self.backBtn)
        toolbar.addWidget(self.backButton)

        self.reloadButton = QPushButton()
        self.reloadButton.setIcon(QIcon("Icons/reload.png"))
        self.reloadButton.setIconSize(QSize(36, 36))
        self.reloadButton.clicked.connect(self.reloadBtn)
        toolbar.addWidget(self.reloadButton)

        self.forwardButton = QPushButton()
        self.forwardButton.setIcon(QIcon("Icons/Right-arrow.png"))
        self.forwardButton.setIconSize(QSize(36, 36))
        self.forwardButton.clicked.connect(self.forwardBtn)
        toolbar.addWidget(self.forwardButton)

        self.homeButton = QPushButton()
        self.homeButton.setIcon(QIcon("Icons/home.png"))
        self.homeButton.setIconSize(QSize(36, 36))
        self.homeButton.clicked.connect(self.homeBtn)
        toolbar.addWidget(self.homeButton)

        self.adblockButton = QPushButton()
        self.adblockButton.setIcon(QIcon("Icons/ad-block.png"))
        self.adblockButton.setIconSize(QSize(36, 36))
        toolbar.addWidget(self.adblockButton)

        self.vpnButton = QPushButton()
        self.vpnButton.setIcon(QIcon("Icons/vpn.png"))
        self.vpnButton.setIconSize(QSize(36, 36))
        toolbar.addWidget(self.vpnButton)

        self.coockieblockButton = QPushButton()
        self.coockieblockButton.setIcon(QIcon("Icons/cookie-Block.png"))
        self.coockieblockButton.setIconSize(QSize(36, 36))
        toolbar.addWidget(self.coockieblockButton)

        self.addressLineEdit = QLineEdit()
        self.addressLineEdit.setFont(QFont("Sanserif", 18))
        self.addressLineEdit.returnPressed.connect(self.searchBtn)
        toolbar.addWidget(self.addressLineEdit)

        self.searchButton = QPushButton()
        self.searchButton.setIcon(QIcon("Icons/search.png"))
        self.searchButton.setIconSize(QSize(36, 36))
        self.searchButton.clicked.connect(self.searchBtn)
        toolbar.addWidget(self.searchButton)

        self.webEngineView = QWebEngineView()
        self.setCentralWidget(self.webEngineView)
        initialUrl = 'https://cabro12.wixsite.com/godspeed-search'
        self.addressLineEdit.setText(initialUrl)
        self.webEngineView.load(QUrl(initialUrl))

    def searchBtn(self):
        myurl = self.addressLineEdit.text()
        self.webEngineView.load(QUrl(myurl))

    def backBtn(self):
        self.webEngineView.back()

    def forwardBtn(self):
        self.webEngineView.forward()

    def reloadBtn(self):
        self.webEngineView.reload()

    def homeBtn(self):
        self.webEngineView.load(QUrl("https://cabro12.wixsite.com/godspeed-search"))


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
