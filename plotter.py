# Used numpy library to work with mathematical functions
import numpy as np
# Used matplotlib to plot points of a function
from matplotlib import pyplot as plt
from validation import printCritical

class Plotter:
    def __init__(self, inputString, function, minimum, maximum):
        self.minimum = minimum
        self.maximum = maximum
        self.function = function
        self.inputString = inputString

    def plot(self):
        # Get an array of ordered elements between a and b "ASSUMPTION": we will deal with maximum 10^6 elements(points)
        x = np.linspace(self.minimum, self.maximum, 1000000)
        try:
            # Set figure title
            plt.figure(num='Function Plotter')
            # Plot the function >> give it the array x and the corresponding array of value of the function
            plt.plot(x, self.function(x))
            # set x axis limits
            plt.xlim(self.minimum, self.maximum)
            # Setting some parameters
            # Set graph's title
            plt.title(self.inputString)
            # Set X axis title
            plt.xlabel("X")
            # Set Y axis title
            plt.ylabel("Y")
            # Show function graph
            plt.show()
        except Exception:
            printCritical("Invalid function.")
            return
