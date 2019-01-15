from PyQt5 import QtCore, QtWidgets

__doc__ = """An attempt at Firefox style tabs in Qt"""

# when tab is killed, dock

if __name__ == "__main__":
    import sys

    def except_hook(cls, exception, traceback):
        sys.__excepthook__(cls, exception, traceback)
    sys.excepthook = except_hook # Python Debug
    
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    window.setGeometry(256, 256, 512, 512)
    dock_01 = QtWidgets.QDockWidget('Tab 1')
    dock_02 = QtWidgets.QDockWidget('Tab 2')
    dock_03 = QtWidgets.QDockWidget('Tab 3')
    window.setTabPosition(QtCore.Qt.TopDockWidgetArea, QtWidgets.QTabWidget.North)
    window.addDockWidget(QtCore.Qt.TopDockWidgetArea, dock_01, QtCore.Qt.Vertical)
    window.tabifyDockWidget(dock_01, dock_02)
    window.tabifyDockWidget(dock_02, dock_03)
    window.show()

    sys.exit(app.exec_())
