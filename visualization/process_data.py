"""Utility functions to process raw data, including averaging, smoothing, etc."""
import numpy as np

def average_from_start(data):
    """Calculate the average from start.
    
    Args:
        data (list or nparray) : an array of data.
    
    Return:
        avg (list) : the averaged data.
    
    Info:
        Given the input X, the output Y is:
            Y[i] = SUM( X[0] ~ x[i] ) / ( i + 1 )

    """
    accum = 0
    avg = []
    for idx in range(len(data)):
        accum += data[idx]
        avg.append(accum / (idx + 1 + 1e-7))
    return avg


def running_average(data, interval=50):
    """Calculate the running average of given data.

    Args:
        data (list or nparray) : an array of data.
        
        interval (int) : the running average interval
    
    Return:
        avg (list) : the averaged data.
    
    Info:
        Given the input X, and the interval D, the output Y is:
            Y[i] = SUM( X[i] ~ x[i + D] ) / D
        
    Notice:
        The output is D elements shorter than the input X.

    """
    avg = []
    for i in range(len(data) - interval):
        left = i
        right = min(i + interval, len(data))
        avg.append(sum(data[left:right])/(right - left))
    return avg


def convolve_line(data, interval=200):
    """Convolve on an array of data, with interval specified as a parameter.

    Args:
        data (list or nparray) : an array of data.
        
        interval (int) : the running average interval
    
    Return:
        avg (list) : the averaged data.
    
    Info:
        Given the input X, and the interval D, the output Y is the convolve
            of data and a unit window with length D.
    
    Notice:
        The output is D elements shorter than the input X.

    """
    return np.convolve(
        data,
        np.ones((interval,))/interval, mode='same'
    )[:-1 * interval]


def smoothen_line(data, N=300):
    """Smoothen a line by interpolation.

    Args:
        data (list or nparray) : an array of data.
        
        N (int) : the number of dots at the middle of two data points.
    
    Return:
        xnew (list) : the new x axis data.

        power_smooth (list) : the new y axis data.
    
    """
    from scipy.interpolate import make_interp_spline, BSpline
    xold = range(len(data))
    xnew = np.linspace(xold[0], xold[-1], N) #300 represents number of points to make between T.min and T.max
    spl = make_interp_spline(xold, data, k=3) #BSpline object
    power_smooth = spl(xnew)
    return xnew, power_smooth


def load_csv_data(fname):
    """Load a csv type of data. Yes I know you can use the 'csv' package, but this works just fine."""
    with open(fname) as csv_file:
        lines = csv_file.readlines()
    lines = [i.strip().split(',') for i in lines]
    data = []
    for row in lines:
        data += row
    return data