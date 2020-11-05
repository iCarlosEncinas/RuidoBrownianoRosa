import sys 
sys.path.insert(1,'dsp-modulo')

import numpy as np 
import thinkplot as plt

from thinkdsp import decorate
from thinkdsp import PinkNoise

pendientes = [0.0, 0.5, 2]

for pendiente in pendientes:
    senal = PinkNoise(beta=pendiente)
    wave = senal.make_wave(duration=0.5, framerate=22050)
    #wave.write("ruido_rosa.wav")

    #wave.plot()
    #decorate(xlabel="Tiempo", ylabel="Amplitud")
    #plt.show()

    etiqueta = f'pendiente={pendientes}'
    #etiqueta = "pendiente=" + pendiente

    espectro = wave.make_spectrum()
    espectro.plot_power(label=etiqueta, alpha=0.7)


loglog = dict(xscale="log", yscale="log")
decorate(xlabel="Frecuencia", ylabel="poder", **loglog)
plt.show()