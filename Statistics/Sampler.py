from random import random


def sampler(data, sample_size):
    random_values = []
    for i in range(sample_size):
        random_values.append(float(data[i]))
    return random_values
