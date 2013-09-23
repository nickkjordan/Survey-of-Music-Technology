# Module 4 - 4
# Our first EarSketch Script
# Modifying the amplitude of audio on the track

from earsketch import *

#Initialize new effect:
volumeEffect = initEffect('basicVolume')

#create ugens used by volumeEffect:
track = createUGen(volumeEffect, INPUT)
multiply = createUGen(volumeEffect, TIMES)
out = createUGen(volumeEffect, OUTPUT)

#Connect ugens according to block diagram:
connect(volumeEffect, track, multiply)  # INPUT is connected to TIMES
connect(volumeEffect, multiply, out)     # TIMES is connected to OUTPUT

#set the multiplier
setParam(multiply, VALUE, 0.5) # multiply all amplitude values by 0.25

#Must finish effect before using:
finishEffect(volumeEffect)