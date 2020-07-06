from Statistics.ZScore import zscore


def correlation(data, data1):
    try:
        z1 = zscore(data)
        z2 = zscore(data1)
        z1_z2 = list(map(lambda x, y: x * y, z1, z2))
        corr = sum(z1_z2) / len(z1_z2)
        return round(corr, 7)
    except ZeroDivisionError:
        print("Error: Enter values greater than 0")
    except ValueError:
        print("Error: insert the correct data type")