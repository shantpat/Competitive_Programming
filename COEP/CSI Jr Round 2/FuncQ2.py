import pylab
import time
import random

dat=[0,1]
pylab.plot(dat)
pylab.ion()
pylab.draw()    
for i in range (18):
    dat.append(random.uniform(0,1))
    pylab.plot(dat)
    pylab.draw()
    time.sleep(1)