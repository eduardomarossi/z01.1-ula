import sys
from PySide2.QtWidgets import QMainWindow, QApplication
from mainwindow import Ui_MainWindow
from ula import compute_ula


class MyUlaWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        window_setup = Ui_MainWindow()
        window_setup.setupUi(self)

        for componentName, component in window_setup.__dict__.items():
            if componentName.endswith('Spin'):
                component.valueChanged.connect(self.recalculate)

        self.window_setup = window_setup
        self.setWindowTitle('z01.1-ula')
        self.show()

    def recalculate(self, f):
        ula_data = {}
        for componentName, component in self.window_setup.__dict__.items():
            if componentName.endswith('Spin'):
                ula_data[componentName.replace('Spin', '')] = component.value()

        result = compute_ula(**ula_data)
        ws = self.window_setup
        ws.outLabel.setText(str(result[2]))
        ws.ngLabel.setText(str(result[1]))
        ws.zrLabel.setText(str(result[0]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyUlaWindow()
    sys.exit(app.exec_())