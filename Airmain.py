from Air import keys
from PyQt5.QtWidgets import QApplication
import sys

import os
#seems we have to set this environment variable to remove a warning
os.environ["XDG_RUNTIME_DIR"] = "/tmp/runtime-runner"

def airmain():
    app = QApplication(sys.argv)
    gui = keys()
    gui.show()
    app.exec_()

airmain()