from Calculator.Square import square
from Calculator.Division import division
from Calculator.Addition import addition
from Statistics.PopulationMean import populationmean


def proportion(num):
    try:
        p_list = list()
        x = sum(num)
        for i in num:
            y = division(i, x)
            p_list.append(y)
        return p_list
    except ZeroDivisionError:
        print("Error: Insert value greater than 0")
    except ValueError:
        print("Error: insert correct data type")