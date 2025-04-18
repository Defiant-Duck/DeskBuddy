
# ui_poc/main.py
import sys
from PyQt5.QtWidgets import QApplication
from ui.pyqt_ui import PyQtUI
from agent_interface import AgentInterface

def run_ui(agent, dev_mode=False):
    app = QApplication(sys.argv)
    window = PyQtUI(agent_interface=agent, dev_mode=dev_mode)
    if dev_mode:
        window.show()
    else:
        window.showFullScreen()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run_ui(AgentInterface(), dev_mode=True)

