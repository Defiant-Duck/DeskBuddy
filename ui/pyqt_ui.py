# ui_poc/ui/pyqt_ui.py
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton, QStackedLayout, QHBoxLayout, QMainWindow
)
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt, QTimer
import os

class DebugConsole(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Debug Console")
        self.resize(500, 300)
        self.text_area = QTextEdit(self)
        self.text_area.setReadOnly(True)
        self.setCentralWidget(self.text_area)

    def append_log(self, message: str):
        self.text_area.append(message)

class FaceOnlyWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.face_label = QLabel()
        gif_path = os.path.join("assets", "idle.gif")
        if os.path.exists(gif_path):
            movie = QMovie(gif_path)
            self.face_label.setMovie(movie)
            movie.start()
        else:
            self.face_label.setText("[Face Placeholder]")
            self.face_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.face_label)
        self.setLayout(layout)

class FaceWithOverlayWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.face_label = QLabel("[Face with Overlay]")
        self.overlay_label = QLabel("<Overlay Info>")
        self.overlay_label.setStyleSheet("background-color: rgba(0, 0, 0, 150); color: white; padding: 4px;")
        self.overlay_label.setAlignment(Qt.AlignBottom)
        layout.addWidget(self.face_label)
        layout.addWidget(self.overlay_label)
        self.setLayout(layout)

class InfoPanelWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.info_label = QLabel("[Information Panel]")
        self.info_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.info_label)
        self.setLayout(layout)

class MainWindow(QWidget):
    def __init__(self, agent_interface, dev_mode=False, debug_console=None):
        super().__init__()
        self.setWindowTitle("Sophia - UI PoC")
        self.setMinimumSize(480, 320)
        self.agent_interface = agent_interface
        self.dev_mode = dev_mode
        self.debug_console = debug_console

        self.stacked_layout = QStackedLayout()
        self.face_only = FaceOnlyWidget()
        self.overlay_mode = FaceWithOverlayWidget()
        self.info_panel = InfoPanelWidget()

        self.stacked_layout.addWidget(self.face_only)
        self.stacked_layout.addWidget(self.overlay_mode)
        self.stacked_layout.addWidget(self.info_panel)

        self.input_box = QTextEdit()
        self.input_box.setFixedHeight(50)

        self.submit_button = QPushButton("Ask")
        self.submit_button.clicked.connect(self.on_submit)

        input_layout = QHBoxLayout()
        input_layout.addWidget(self.input_box)
        input_layout.addWidget(self.submit_button)

        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.stacked_layout)
        self.main_layout.addLayout(input_layout)
        self.setLayout(self.main_layout)

        self.show_face_only()

    def show_face_only(self):
        self.stacked_layout.setCurrentWidget(self.face_only)

    def show_overlay(self):
        self.stacked_layout.setCurrentWidget(self.overlay_mode)

    def show_info_panel(self):
        self.stacked_layout.setCurrentWidget(self.info_panel)

    def on_submit(self):
        user_input = self.input_box.toPlainText().strip()
        if user_input:
            if self.debug_console:
                self.debug_console.append_log(f"User: {user_input}")

            self.show_overlay()
            self.overlay_mode.overlay_label.setText("Thinking...")

            QTimer.singleShot(1000, lambda: self.display_response(user_input))
            self.input_box.clear()

    def display_response(self, user_input):
        response = self.agent_interface.process_input(user_input)
        self.overlay_mode.overlay_label.setText(response)

        if self.debug_console:
            self.debug_console.append_log(f"Sophia: {response}")

