from Calculator.Square import square
from Calculator.Division import division
from Statistics.PopulationMean import populationmean


def variance(num):
    try:
        pop_mean = populationmean(num)
        num_values = len(num)
        x = 0
        for i in num:
            x = x + square(i-pop_mean)
        return division(x, num_values)
    except ZeroDivisionError:
        print("Error: Enter number greater than  0")
    except ValueError:
        print ("Error: Enter correct data type")