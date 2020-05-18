# ----------- NORMALISATION ------------ #
#soundInput = soundInput[:, 0]/2**15

# ------------ CALCULATIONS FOR ECHO ------------ #
# echo = echoEffect(soundInput, 0.5, sf)

# ------------ CALCULATIONS FOR VIBRATO ------------ #
# vibrato = addVibrato(soundInput, sf)
# plotGraph(soundInput, vibrato, time)
# ------------ CALCULATIONS FOR CHORUS ------------ #
#chorus = chorusEffect(soundInput, sf)
#plotGraph(soundInput, chorus, time)

# counter = np.int(input("Please enter an integer from 0-4: "))

# if counter == 1:
# sd.play(echo, sf)
# elif counter == 2:
# sd.play(vibrato, sf)
# elif counter == 3:
#sd.play(chorus, sf)
# elif counter == 4:
# sd.play(freq, sf)
# else:
# sd.play(soundInput, sf)
# status = sd.wait()

readInput()