import sys
__author__ = "Grzegorz Bokota"


def my_excepthook(type, value, tback):
    # log the exception here

    # then call the default handler
    sys.__excepthook__(type, value, tback)

sys.excepthook = my_excepthook


if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.INFO)
    from qt_import import QApplication
    from stackseg.stack_gui_main import MainWindow
    import sys
    myApp = QApplication(sys.argv)
    wind = MainWindow("StackSeg")
    wind.show()
    myApp.exec_()
    sys.exit()
