import unittest
from CsvReader.CsvReader import CsvReader
from Statistics.Statistics import Statistics
from pprint import pprint


class MyTestCase(unittest.TestCase):
    test_data = CsvReader('Tests/Data/TestData.csv').data
    column1 = [int(row['Value 1']) for row in test_data]
    column2 = [int(row['Value 2']) for row in test_data]
    p_answers = CsvReader().data
    z_answers = CsvReader().data
    column_proportion = [float(row['Proportion']) for row in p_answers]
    column_z_score = [float(row['Z-Score']) for row in z_answers]
    test_answer = CsvReader('').data
    sample_data = CsvReader('').data
    column3 = [int(row['']) for row in sample_data]
    sample_answer = CsvReader('').data


if __name__ == '__main__':
    unittest.main()
