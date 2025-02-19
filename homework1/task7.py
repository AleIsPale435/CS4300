import numpy as np
import pytest

# This function will take an array and calculate the mean, median, and the standard deviation of the array using the numpy package.
def calculateArrayStats(array):

    data = np.array(array)
    return{
        'Mean': np.mean(data),
        'Median': np.median(data),
        'StdDeviation': np.std(data),
    }

# This function will test the calculateArrayStats function with only integers.
def testArrayStatisticsIntegers():
    data = [1, 2, 3, 4, 5]
    correctStats = calculateArrayStats(data)
    correctMean = 3.0
    correctMedian = 3.0
    correctStdDeviation = np.std(np.array(data))

    assert correctStats['Mean'] == pytest.approx(correctMean)
    assert correctStats['Median'] == pytest.approx(correctMedian)
    assert correctStats['StdDeviation'] == pytest.approx(correctStdDeviation)

# This function will test the calculateArrayStats function with only floats.
def testArrayStatisticsFloats():
    data = [7.8, 9.1, 15.72, 23.89, 32.34]
    correctStats = calculateArrayStats(data)
    correctMean = 17.77
    correctMedian = 15.72
    correctStdDeviation = np.std(np.array(data))

    assert correctStats['Mean'] == pytest.approx(correctMean)
    assert correctStats['Median'] == pytest.approx(correctMedian)
    assert correctStats['StdDeviation'] == pytest.approx(correctStdDeviation)

# This function will test the calculateArrayStats function with both integers and floats.
def testArrayStatisticsMixedVariables():
    data = [4.5, 5, 10.2, 16.23, 20.7]
    correctStats = calculateArrayStats(data)
    correctMean = 11.326
    correctMedian = 10.2
    correctStdDeviation = np.std(np.array(data))

    assert correctStats['Mean'] == pytest.approx(correctMean)
    assert correctStats['Median'] == pytest.approx(correctMedian)
    assert correctStats['StdDeviation'] == pytest.approx(correctStdDeviation)