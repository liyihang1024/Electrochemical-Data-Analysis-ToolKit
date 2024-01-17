from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

class MyWindow(QMainWindow):
    def __init__(self, ui_file):
        super(MyWindow, self).__init__()
        loader = QUiLoader()
        file = QFile(ui_file)
        file.open(QFile.ReadOnly)
        self.ui = loader.load(file, self)
        file.close()

# 主函数
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mainWindow = MyWindow("FunctionWindow.ui")  # 替换为您的 .ui 文件的路径
    mainWindow.ui.show()
    sys.exit(app.exec())
