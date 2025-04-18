# ui_poc/ui/pyqt_ui.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt
import os

class PyQtUI(QWidget):
    def __init__(self, agent_interface, dev_mode=False):
        super().__init__()
        self.agent_interface = agent_interface
        self.dev_mode = dev_mode
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Sophia - UI PoC")
        self.setMinimumSize(480, 320)
        self.layout = QVBoxLayout()

        # Face display
        self.face_label = QLabel()
        gif_path = os.path.join("assets", "idle.gif")
        if os.path.exists(gif_path):
            movie = QMovie(gif_path)
            self.face_label.setMovie(movie)
            movie.start()
        else:
            self.face_label.setText("[Face Placeholder]")
            self.face_label.setAlignment(Qt.AlignCenter)

        # Input box
        self.input_box = QTextEdit()
        self.input_box.setFixedHeight(50)

        # Submit button
        self.submit_button = QPushButton("Ask")
        self.submit_button.clicked.connect(self.on_submit)

        # Result display
        self.output_label = QLabel("<i>Awaiting input...</i>")
        self.output_label.setWordWrap(True)
        self.output_label.setAlignment(Qt.AlignTop)

        # Layout setup
        self.layout.addWidget(self.face_label)
        self.layout.addWidget(self.input_box)
        self.layout.addWidget(self.submit_button)
        self.layout.addWidget(self.output_label)
        self.setLayout(self.layout)

    def on_submit(self):
        user_input = self.input_box.toPlainText().strip()
        if user_input:
            response = self.agent_interface.process_input(user_input)
            self.output_label.setText(response)
            self.input_box.clear()

