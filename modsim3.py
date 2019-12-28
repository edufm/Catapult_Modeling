# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 16:46:17 2016

@author: Nois
"""

from Catapult_Model import Calculos

from pylab import *
from matplotlib.widgets import Slider, Button

def update(val):
    mbola = smbola.val
    tbrac = stbrac.val
    ang = sang.val
    vcord = svcord.val
    ncord = sncord.val
    l.set_xdata((Calculos(ang/57.35, tbrac, vcord, mbola, ncord))[0])
    l.set_ydata((Calculos(ang/57.35, tbrac, vcord, mbola, ncord))[1])
    draw()    

def reset(event):
    smbola.reset()
    stbrac.reset()
    sang.reset()
    svcord.reset()
    sncord.reset()
    
ax = subplot(111)
ax.grid(True)

subplots_adjust(left=0.25, bottom=0.32)
m0 = 0.200
b0 = 4
a0 = 70
V0 = 7.5
N0 = 2

l, = plot((Calculos(a0/57.35, b0, V0, m0, N0))[0], (Calculos(a0/57.35, b0, V0, m0, N0))[1], lw=2, color='red')
axis([0, 100, 0, 40])
xlabel("Distancia")
ylabel("Altura")

axcolor = 'lightgoldenrodyellow'
axmbola  = axes([0.25, 0.20, 0.65, 0.03], facecolor=axcolor)
axtbrac  = axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
axang  = axes([0.25, 0.10, 0.65, 0.03], facecolor=axcolor)
axvcord  = axes([0.25, 0.05, 0.65, 0.03], facecolor=axcolor)
axncord  = axes([0.25, 0.0, 0.65, 0.03], facecolor=axcolor)

smbola = Slider(axmbola, 'Massa da bola', 0.01, 1.0, valinit=m0)
stbrac = Slider(axtbrac, 'Tamanho do braço', 0.1, 10.0, valinit=b0)
sang = Slider(axang, 'Angulo', 0.01, 90, valinit=a0)
svcord = Slider(axvcord, 'Voltas na corda', 1, 12, valinit=V0)
sncord = Slider(axncord, 'Numero de cordas lado', 1, 4, valinit=N0)
    
smbola.on_changed(update)
stbrac.on_changed(update)
sang.on_changed(update)
svcord.on_changed(update)
sncord.on_changed(update)

resetax = axes([0.1, 0.4, 0.1, 0.04])

button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')
button.on_clicked(reset)

show()