import sys
from PySide6.QtWidgets import QMainWindow, QApplication
from mainwindow import Ui_MainWindow
from ula import compute_ula, convert_output

VERSION = '1.1.1'


class MyUlaWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        window_setup = Ui_MainWindow()
        window_setup.setupUi(self)

        for componentName, component in window_setup.__dict__.items():
            if componentName.endswith('Spin'):
                component.valueChanged.connect(self.recalculate)
            elif componentName.endswith('Edit'):
                 component.textEdited.connect(self.recalculate)

        self.window_setup = window_setup
        self.window_setup.xEdit.setText('01110011'.zfill(8))
        self.window_setup.yEdit.setText('01011111'.zfill(8))
        self.setWindowTitle('z01.1-ula v' + VERSION)
        self.recalculate()
        self.show()


    def recalculate(self):
        ula_data = {}
        for componentName, component in self.window_setup.__dict__.items():
            if componentName.endswith('Spin'):
                ula_data[componentName.replace('Spin', '')] = component.value()
            elif componentName.endswith('Edit'):
                text = component.text().strip().replace(' ', '')
                component.setText(text)
                try:
                    val = int(text, 2)
                except ValueError:
                    if len(text) > 0:
                        component.setText(text[:-1])
                    else:
                        component.setText('0')
                    val = 0

                ula_data[componentName.replace('Edit', '')] = val

        result = compute_ula(**ula_data)
        ws = self.window_setup

        ws.outLabel.setText(convert_output(result[2]))
        ws.ngLabel.setText(str(result[1]))
        ws.zrLabel.setText(str(result[0]))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyUlaWindow()
    sys.exit(app.exec_())
