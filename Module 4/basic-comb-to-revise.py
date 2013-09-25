# Module 4-6
# Subtractive Techniques
# Comb Processing Example

from earsketch import *

combEffect = initEffect('combLpfFilter')

# create ugens used by combEffect:
track = createUGen(combEffect, INPUT)
delay = createUGen(combEffect, ECHO)
add = createUGen(combEffect, ADD)
multiplier = createUGen(combEffect, TIMES)
output = createUGen(combEffect, OUTPUT)
lowPass = createUGen(combEffect, FILTERLP6)

connect(combEffect, track, lowPass)
connect(combEffect, lowPass, add)
connect(combEffect, multiplier, add, 0, 1)
connect(combEffect, add, output)
connect(combEffect, add, delay)
connect(combEffect, delay, multiplier)

#Set the min, max, and default value for the low-pass filter
setParamMin(lowPass, FREQUENCY, 0)
setParamMax(lowPass, FREQUENCY, 10000)
setParam(lowPass, FREQUENCY, 100)
createControl(combEffect, lowPass, FREQUENCY, 'lpf cutoff frequency')

#Set the min, max, and default delay times
# shorter delay time (ms) = higher base frequency
setParamMin(delay, TIME, 0)
setParamMax(delay, TIME, 2)
setParam(delay, TIME, 0.5)
createControl(combEffect, delay, TIME, 'delay time')

#Set the min, max, and default value for the feedback amount
setParamMin(multiplier, VALUE, 0)
setParamMax(multiplier, VALUE, 1)
setParam(multiplier, VALUE, 0.6)
createControl(combEffect, multiplier, VALUE, 'feedback amount')

#Must finish effect before using:
finishEffect(combEffect)