# Used PyQt5 to implement the GUI
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtWidgets, uic
import sys
# I implemented this class to validate and process the input string
from validation import Validation, printCritical
from plotter import Plotter


class Window(QDialog):
    def __init__(self):
        super(Window, self).__init__()
        # Load the implemented UI window
        uic.loadUi('mainWindow.ui', self)
        # When plotButton is clicked, We have to start plotting
        self.plotButton.clicked.connect(self.start)
        self.setWindowTitle("Function Plotter")
        self.show()

    def start(self):
        inputString = self.function.text()
        minimum = self.minimumValue.text()
        maximum = self.maximumValue.text()
        validator = Validation(inputString, minimum, maximum)
        if validator.validate():
            function = validator.convertInputToFunction()
            plotter = Plotter(inputString, function, validator.minimum, validator.maximum)
            plotter.plot()

        return


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    appWindow = Window()
    sys.exit(app.exec_())