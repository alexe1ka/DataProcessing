import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit

a = QApplication(sys.argv)
# The QWidget widget is the base class of all user interface objects in PyQt4.
w = QWidget()
# Set window size.
w.resize(320, 240)
# Set window title
w.setWindowTitle("Hello World!")

# Create textbox
textbox = QLineEdit(w)
textbox.move(20, 20)
textbox.resize(280,40)


# Show window
w.show()
sys.exit(a.exec_())