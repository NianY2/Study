import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class window(QWidget):
   def __init__(self, parent = None):
      super(window, self).__init__(parent)
      self.resize(200,50)
      self.setWindowTitle("CY手机工具箱")
      self.label = QLabel(self)
      self.label.setText("CY手机工具箱")
      font = QFont()
      font.setFamily("Arial")
      font.setPointSize(16)
      self.label.setFont(font)
      self.label.move(50,20)
      
def window_main():
    app = QApplication(sys.argv)
    ex = window()
    ex.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    window_main()
