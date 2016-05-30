import pylab



    
def euler(function, y0, yprime0, t0, tN, N):
    deltat = float(tN-t0)/N
    tVals = [t0]
    yVals = [y0]
    yPrimeVals = [yprime0]
    for k in xrange(N):
        mY, mYprime = function(yVals[-1], yPrimeVals[-1], tVals[-1])
        newY = yVals[-1]+deltat*mY
        newYprime = yPrimeVals[-1] + deltat*mYprime
        newT = tVals[-1]+deltat
        tVals.append(newT)
        yVals.append(newY)
        yPrimeVals.append(newYprime)
    return tVals, yVals, yPrimeVals

def plotEuler(function, y0, yprime0, t0, tN, N, label):
    tVals, yVals, yPrimeVals = euler(function, y0, yprime0, t0, tN, N)
    pylab.plot(tVals, yVals)
    pylab.xlim(tVals[0],tVals[-1])
    pylab.xlabel(label)
    pylab.show()
    
def makeNoDampingGraph():
    def f1(y,yprime, t):
        return yprime, -5*y
    plotEuler(f1, 0.5, 0, 0, 6, 10000, "NO DAMPING")

def makeUnderDampingGraph():
    def f1(y,yprime, t):
        return yprime, -30*y-6*yprime
    plotEuler(f1, 0.5, 0, 0, 6, 10000, "UNDERDAMPING")
    
def makeOverDampingGraph():
    def f1(y,yprime, t):
        return yprime, -6*y-9*yprime
    plotEuler(f1, 0.5, 0, 0, 6, 10000, "OVERDAMPING")
    
def makeCriticalDampingGraph():
    def f1(y,yprime, t):
        return yprime, -3*y-6*yprime
    plotEuler(f1, 0.5, 0, 0, 6, 10000, "CRITICAL DAMPING")