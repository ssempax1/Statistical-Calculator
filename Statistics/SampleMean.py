from Calculator.Addition import addition
from Calculator.Division import division
from Statistics.Sampler import sampler


def samplemean(data, sample_size):
    total = 0
    sample = sampler(data, sample_size)
    num_values = len(sample)
    for num in sample:
        total = addition(total, num)
    return division(total, num_values)