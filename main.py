# ui_poc/main.py
import sys
from PyQt5.QtWidgets import QApplication
from ui.pyqt_ui import MainWindow, DebugConsole
from agent_interface import AgentInterface

def run_ui(agent, dev_mode=False):
    app = QApplication(sys.argv)

    debug_console = DebugConsole() if dev_mode else None
    window = MainWindow(agent_interface=agent, dev_mode=dev_mode, debug_console=debug_console)

    if debug_console:
        debug_console.show()

    if dev_mode:
        window.show()
    else:
        window.showFullScreen()

    sys.exit(app.exec_())

if __name__ == "__main__":
    run_ui(AgentInterface(), dev_mode=True)

