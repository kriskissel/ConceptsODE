import pylab
import math

def f(x,y):
    return y*(3-y)

def dfieldPlot(g, xmin=-10, xmax=10, ymin=-10, ymax=10, xpoints=11, ypoints=11, marklength=0.3):  
    dh = marklength*(xmax-xmin)/(float(xpoints))
    pylab.figure()
    for k in range(0,xpoints):
        for l in range(0,ypoints):
            x = xmin + k*(xmax-xmin)/float(xpoints-1)
            y = ymin + l*(ymax-ymin)/float(ypoints-1)
            m = g(x,y)
            dx =dh/float(math.sqrt(1+m**2))
            dy = dx*g(x,y)
            xendpoints=[x-dx,x+dx]
            yendpoints=[y-dy,y+dy]
            pylab.plot(xendpoints,yendpoints, "-k")
            pylab.xlim(xmin-10*dx, xmax+10*dx)
            pylab.ylim(ymin-10*dy, ymax+10*dy)
    pylab.show()

dfieldPlot(f, xmin=-2, xmax=4, ymin=-2, ymax=4, xpoints=31, ypoints=31)