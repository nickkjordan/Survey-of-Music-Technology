# Module 4-6
# Additive Synthesis

from earsketch import *

#Initialize new effect:
additive = initEffect('basicAdd')

baseFreq = 440
output = createUGen(additive, OUTPUT)

# create and connect ugens: (note that there is no input)
for i in range(50):
    harmonic = i + 1
    freq = baseFreq * harmonic
    osc = createUGen(additive, SINE)
    times = createUGen(additive, TIMES)
    setParam(osc, FREQUENCY, freq)
    setParam(times, VALUE, 1.0 / harmonic)
    println(freq)
    println(1.0 / harmonic)
    connect(additive, osc, times)
    connect(additive, times, output)

#Must finish effect before using:
finishEffect(additive)