from keys import KeyboardUI # import keyboard main window
from PyQt5.QtWidgets import QApplication 
import sys

import os
# set environment variable to remove a warning
os.environ["XDG_RUNTIME_DIR"] = "/tmp/runtime-runner"

def airuimain():
    app = QApplication(sys.argv)
    gui = KeyboardUI()
    gui.show()
    app.exec_()

airuimain()