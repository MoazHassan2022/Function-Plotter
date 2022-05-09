# Used numpy library to work with mathematical functions
import numpy as np
# Used re "regular expressions library" to use findall() function inside it
import re
import pytest
dangerous = ['import', 'subprocess', 'shutil', 'sys']

# This is a test file for certain functions
# To test, install pytest: pip install pytest
# then type this command in terminal: pytest -v


@pytest.mark.parametrize("inputString, minimum, maximum, expected", [('x^2', '0', '10', 1), ('import', '0', '10', 0),
                                                                     ('sys', '0', '10', 0), ('sin(z)', '0', '10', 1),
                                                                     (' ', '0', '10', 0), ('x', '-10', '-20', 0),
                                                                     ('x', 'G', 'K', 0)])
def test_validate(inputString, minimum, maximum, expected):
    # Some input validations
    test = 1
    if inputString == "" or inputString == " ":
        test = 0
    try:
        minimumValue = float(minimum)
        maximumValue = float(maximum)
        if minimumValue > maximumValue:
            test = 0
    except ValueError:
        test = 0
    # Validates the string from any harmful command
    # See if there is any dangerous word that maybe will harm us
    for word in dangerous:
        if word in inputString:
            test = 0
    assert test == expected

@pytest.mark.parametrize("inputString, expected", [('x^2', 'x**2'), ('sin(x)', 'np.sin(x)'), ('x/2','x/2'), ('x + exp(x)', 'x + np.exp(x)')])
def test_convertInputToFunc(inputString, expected):
    # Find all words not symbols in the input except 'x' and replace them with valid syntax
    for word in re.findall('[a-zA-Z_]+', inputString):
        # For example if user wants sin(x) function .. it should be replaced with np.sin(x)
        # np.sin(x) takes an array of values of x in rad and returns array of sine values of x values
        if word == 'x':
            continue
        inputString = inputString.replace(word, 'np.{}'.format(word))
    inputString = inputString.replace('^', '**')
    assert inputString == expected