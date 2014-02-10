#!/usr/bin/env python

#
# scratch work for doing impulse response analysis
#

import os
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import scipy.io.wavfile as spiowf
from numpy.fft import *

def get_amplitude_phase(IR,T_s):
    fourier = fft(IR)
    freq = fftfreq(fourier.size,d=T_s)
    fourier = fourier[:fourier.size/2]
    freq = freq[:freq.size/2]

    amplitude = np.absolute(fourier)
    phase = np.angle(fourier,deg=True)
    return (freq,amplitude,phase)

def plot_it(t,IR,freq,amplitude,phase,title):
    # make a class to bundle all this crap together

    x_max = 0.5*f_s

    plt.subplot(3,1,1)
    plt.plot(t,IR,".-")
    plt.ylabel("impulse response")
    plt.xlabel("time [secs]")
    plt.title(title)

    plt.subplot(3,1,2)
    plt.plot(freq,amplitude,".-")
    plt.ylabel("amplitude")
    plt.xlabel("frequency [Hz]")
    plt.xlim(0.0,x_max)

    plt.subplot(3,1,3)
    plt.plot(freq,phase,".-")
    plt.ylabel("phase [deg]")
    plt.xlabel("frequency [Hz]")
    plt.xlim(0.0,x_max)

    return

ir_dir = "./violin_irs/"
ir_files = [ f for f in os.listdir(ir_dir) if f.endswith("WAV")]

# generate amplitude and phase spectrum plots for violin impulse response test data.
for f in ir_files:
    f_s, IR = spiowf.read(ir_dir+f)
    T_s = 1.0/f_s

    freq,amplitude,phase = get_amplitude_phase(IR,T_s)

    duration = IR.size*T_s
    t = sp.arange(0,duration,T_s)

    plot_it(t,IR,freq,amplitude,phase,f)

    plt.savefig(ir_dir+f+".png")
    plt.clf()
