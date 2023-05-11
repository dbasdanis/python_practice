import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider

TWOPI = 2*np.pi

fig,ax =plt.subplots()

t = np.arange(0.0, TWOPI, 0.001)
initial_amp = .5
s = initial_amp*np.sin(t)
l, = plt.plot(t,s,lw=2)

ax = plt.axis([0,TWOPI,-1,1])

axamp = plt.axes([0.25, .03, 0.50, 0.02])

# Slider
samp = Slider(axamp, 'Amp', 0, 1, valinit = initial_amp)

def update(val):
    amp = samp.val
    l.set_ydata(amp*np.sin(t))
    fig.canvas.draw_idle()

samp.on_changed(update)

plt.show()