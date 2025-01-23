from fractions import Fraction
from math import sin, cos, tan, sqrt, log, e, radians, pi

calculation = ""
last_answer = ""

def evaluate_expression(calc):
    try:
        if "sin" in calc:
            calc = calc.replace("sin", "sin(radians")
            calc += ")"
        elif "cos" in calc:
            calc = calc.replace("cos", "cos(radians")
            calc += ")"
        elif "tan" in calc:
            calc = calc.replace("tan", "tan(radians")
            calc += ")"
        elif "√" in calc:
            calc = calc.replace("sqrt", "√")
        elif "ln" in calc:
            calc = calc.replace("ln", "log")
        elif "x" in calc:
            calc = calc.replace("x", "*")
        elif "pi" in calc:
            calc = calc.replace("pi", str(pi))
        elif "%" in calc:
            calc = calc.replace("%", "*100")

        calc = calc.replace('x', '*')
        calc = calc.replace("^", "**")
        calc = calc.replace("√", "sqrt")
        calc = calc.replace('π', 'pi')
        calc = calc.replace("%", "*100")
        
        result = str(eval(calc))
        return result
    except:
        return "Error"

def convert_decimal_fraction(value):
    try:
        if '.' in value:
            return str(Fraction(value))
        return str(eval(value))
    except:
        return "Error"
