#!/usr/bin/python

from scipy.signal import chirp
import matplotlib.pyplot as plt
import numpy as np
import pyaudio

t0 = 0.
t1 = 0.2
dt = t1 - t0
sr = 44.1e3
ns = sr*dt
t = np.linspace(t0,t1,ns)
f0 = 20.
f1 = 20.e3
w = chirp(t,f0,t1,f1,method="logarithmic")
nreps = 50
w = np.concatenate([w for i in range(nreps)])
#f = map(lambda t: f0*(f1/f0)**(t/t1),t)

p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=44100,
                output=True)
stream.write(w.astype(np.float32).tostring())
stream.close()
p.terminate()
