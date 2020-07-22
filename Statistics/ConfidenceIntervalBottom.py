from Calculator.Division import division
from Calculator.Subtraction import subtraction
from Calculator.Addition import addition
from Calculator.SquareRoot import square_root
from Statistics.PopulationMean import populationmean
from Statistics.StandardDeviation import stddev


def confidence_interval_bottom(num):
    try:
        num_values = len(num)
        z = 1.96
        sd = stddev(num)
        avg = populationmean(num)
        return round(avg - (z * sd / square_root(num_values)), 5)
    except ZeroDivisionError:
        print("Error:Insert a number greater than 0")
    except ValueError:
        print("Error: Enter correct data type ")