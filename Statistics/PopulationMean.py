# from Calculator.Addition import addition
from Calculator.Division import division


def populationmean(num):
    try:
        num_values = len(num)
        total = sum(num)
        return division(total, num_values)
    except ZeroDivisionError:
        print("Error: Enter values greater than 0")
    except ValueError:
        print("Error: insert correct data type")