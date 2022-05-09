# Used numpy library to work with mathematical functions
import numpy as np
# Used re "regular expressions library" to use findall() function inside it
import re
from PyQt5.QtWidgets import QMessageBox

dangerous = ['import', 'subprocess', 'shutil', 'sys']


class Validation:
    inputString = ""

    def __init__(self, inputString, minimum, maximum):
        self.inputString = inputString.lower()
        self.minimum = minimum
        self.maximum = maximum

    def setNewInput(self, newInput):
        self.inputString = newInput

    def validate(self):
        # Some input validations
        if self.inputString == "" or self.inputString == " ":
            printCritical("Invalid function.")
            return 0
        try:
            self.minimum = float(self.minimum)
            self.maximum = float(self.maximum)
            if self.minimum > self.maximum:
                printCritical("Lower value is bigger than upper.")
                return 0
        except ValueError:
            printCritical("Please enter numbers in lower and upper.")
            return 0
        # Validate the string from any harmful command
        # See if there is any dangerous word that maybe will harm us
        for word in dangerous:
            if word in self.inputString:
                printCritical('"{}" is forbidden to use.'.format(word))
                return 0
        return 1

    def convertInputToFunction(self):
        # Find all words not symbols in the input except 'x' and replace them with valid syntax
        for word in re.findall('[a-zA-Z_]+', self.inputString):
            # For example if user wants sin(x) function .. it should be replaced with np.sin(x)
            # np.sin(x) takes an array of values of x in rad and returns array of sine values of x values
            if len(word) == 1:
                self.inputString = self.inputString.replace(word, 'x')
                continue
            self.inputString = self.inputString.replace(word, 'np.{}'.format(word))
        self.inputString = self.inputString.replace('^', '**')

        def function(x):
            # evaluate Python expressions from the input string
            return eval(self.inputString)

        # return a function to be called in plot function
        return function


def printCritical(message):
    messageBox = QMessageBox()
    messageBox.setIcon(QMessageBox.Critical)
    # Print the message
    messageBox.setText(message)
    messageBox.setWindowTitle("Critical")
    # Ok button
    messageBox.setStandardButtons(QMessageBox.Ok)
    # Execute
    messageBox.exec_()
    return

