
import numpy as np

def twoPtForwardDiff(x,y):
    """ takes derivative using the slope between current and forward point
    takes x and y(x)
    """
    dydx = np.zeros(y.shape,float)
    dydx[0:-1] = np.diff(y)/np.diff(x)
    dydx[-1] = (y[-1]-y[-2])/(x[-1]-x[-2])
    return dydx

def twoPtCenteredDiff(x,y):
    """takes the derivative using slope from each side of point
    takes x and y(x)
    """
    dydx = np.zeros(y.shape,float)
    dydx[1:-1] = (y[2:] - y[:-2])/(x[2:]-x[:-2])
    dydx[0] = (y[1]-y[0])/(x[1]-x[0])
    dydx[-1] = (y[-1]-y[-2])/(x[-1]-x[-2])
    return dydx

def fourPtCenteredDiff(x,y):
    """ takes derivative using fourpoints
    takes x and y(x)
    """
    dydx = np.zeros(y.shape,float)
    h = x[1]-x[0]
    dydx[2:-2] = (y[0:-4] - 8*y[1:-3]+8*y[3:-1]-y[4:])/(12*x[1]-x[0])
    dydx[0:2] = np.diff(y[0:2])/np.diff(x[0:2])
    dydx[-2:-1] = (y[-2:-1]-y[-1:])/(x[-2:-1]-x[-1:])
    return dydx