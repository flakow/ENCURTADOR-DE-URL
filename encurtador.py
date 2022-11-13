from  PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QFrame, QLineEdit, QPushButton
from PySide2.QtCore import QSize,Qt
import sys
import pyshorteners

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Encurtador De Url')
        self.resize(400,300)

        layout = QVBoxLayout()

        self.frame = QFrame()

        self.link = QLineEdit(self.frame)
        self.link.setPlaceholderText("Coloque Seu Link Aqui")

        self.btn = QPushButton(self.frame)
        self.btn.setText("Executar")

        self.result = QLineEdit(self.frame)

        layout.addWidget(self.link)
        layout.addWidget(self.btn)
        layout.addWidget(self.result)

        self.frame.setLayout(layout)

        self.btn.clicked.connect(self.link_shortners) #SINAL PARA CHAMAR A FUNÇÃO

        self.setCentralWidget(self.frame)

#FUNÇÃO PARA ENCURTAR LINK
    def link_shortners(self):
        short = pyshorteners.Shortener()
        new_link = short.tinyurl.short(self.link.text()) #ENTRADA DE TEXTO
        self.result.setText(new_link) #RESULTADO
        


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()