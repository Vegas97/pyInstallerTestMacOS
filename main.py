import sys
import os
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PySide6.QtGui import QPixmap, QImage, QPainter
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtCore import Qt


def resource_path0(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def resource_path(relative):
    return os.path.join(
        os.environ.get(
            "_MEIPASS",
            os.path.abspath(".")
        ),
        relative
    )


def resource_path2(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def resource_path3(relative_path):
    bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
    return os.path.abspath(os.path.join(bundle_dir, relative_path))


class ImageWindow(QWidget):
    def __init__(self, image_path):
        super().__init__()

        # Load an SVG file using QSvgRenderer and render it into QPixmap
        if image_path.lower().endswith('.svg'):
            renderer = QSvgRenderer(image_path)
            image = QImage(renderer.defaultSize(), QImage.Format_ARGB32)
            image.fill(Qt.transparent)
            painter = QPainter(image)
            renderer.render(painter)
            pixmap = QPixmap.fromImage(image)
        else:
            pixmap = QPixmap(image_path)

        # Create a label and set the QPixmap as its content
        label = QLabel(self)
        label.setPixmap(pixmap)

        # Create a layout and add the label to it
        layout = QVBoxLayout(self)
        layout.addWidget(label)

        # Set layout
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Use resource_path to get the correct path for the image
    image_path = resource_path3("images/test.png")  # Provide your image path here

    print(image_path)

    window = ImageWindow(image_path)
    window.show()

    sys.exit(app.exec())
