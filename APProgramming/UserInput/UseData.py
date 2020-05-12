

<<<<<<< Updated upstream
=======
sf, soundInput = wave.read("A Light Breeze from South West Redux.wav")
length = np.size(soundInput)
time = np.arange(0, length)

# ----------- CALCULATIONS FOR FREQUENCY CHANGE ---------#
freqSmall = resampleFreq(soundInput, 2)
print("Freq small")
freqMed = resampleFreq(soundInput, 5)
print("Freq med")
freqHigh = resampleFreq(soundInput, 10)
print("Freq high")
freqReallyHigh = resampleFreq(soundInput, 15)
print("Freq very high")
# plotGraph(freq, time)

# ----------- NORMALISATION FOR THE OTHER FUNCTIONS ------------ #
soundInput = soundInput[:] / 2 ** 15

# ------------ CALCULATIONS FOR ECHO ------------ #
echoSmall = echoEffect(soundInput, 0.5, sf)
print("echo small")
echoMed = echoEffect(soundInput, 1, sf)
print("echo mid")
echoHigh = echoEffect(soundInput, 1.5, sf)
print("echo high")
echoReallyHigh = echoEffect(soundInput, 2, sf)
print("echo small")

# ------------ CALCULATIONS FOR VIBRATO ------------ #
vibratoSmall = addVibrato(soundInput, 0.005, sf)
print("Vibrato small")
vibratoMed = addVibrato(soundInput, 0.01, sf)
print("Vibrato med")
vibratoHigh = addVibrato(soundInput, 0.05, sf)
print("Vibrato high")
vibratoReallyHigh = addVibrato(soundInput, 0.1, sf)
print("Vibrato very high")
# plotGraph(soundInput, vibrato, time)
# ------------ CALCULATIONS FOR CHORUS ------------ #
chorusSmall = chorusEffect(soundInput, 0.1, sf)
print("chorus small")
chorusMed = chorusEffect(soundInput, 0.5,sf)
print("chorus med")
chorusHigh = chorusEffect(soundInput, 1,sf)
print("chorus high")
chorusReallyHigh = chorusEffect(soundInput, 1.5,sf)
print("chorus very high")

print("Done Processing")


def soundEffect(lastValueID, sensorvalue=0, state=0):

    if state == 0:
        if lastValueID != 0:
            sd.play(soundInput, sf)
            lastValueID = 0

    if state == 1:
        if 0 <= sensorvalue <= 0.875:
            if lastValueID != 1:
                sd.play(freqSmall, sf)
                lastValueID = 1

        elif 0.875 < sensorvalue <= 1.75:
            if lastValueID != 2:
                sd.play(freqMed, sf)
                lastValueID = 2
        elif 1.75 < sensorvalue <= 2.625:
            if lastValueID != 3:
                sd.play(freqHigh, sf)
                lastValueID = 3
        elif 2.625 < sensorvalue:
            if lastValueID != 4:
                sd.play(freqReallyHigh, sf)
                lastValueID = 4

    if state == 2:
        if 0 <= sensorvalue <= 0.875:
            if lastValueID != 5:
                sd.play(echoSmall, sf)
                lastValueID = 5
        elif 0.875 < sensorvalue <= 1.75:
            if lastValueID != 6:
                sd.play(echoMed, sf)
                lastValueID = 6
        elif 1.75 < sensorvalue <= 2.625:
            if lastValueID != 7:
                sd.play(echoHigh, sf)
                lastValueID = 7
        elif 2.625 < sensorvalue:
            if lastValueID != 8:
                sd.play(echoReallyHigh, sf)
                lastValueID = 8

    if state == 3:
        if 0 <= sensorvalue <= 0.875:
            if lastValueID != 9:
                sd.play(vibratoSmall, sf)
                lastValueID = 9

        elif 0.875 < sensorvalue <= 1.75:
            if lastValueID != 10:
                sd.play(vibratoMed, sf)
                lastValueID = 10

        elif 1.75 < sensorvalue <= 2.625:
            if lastValueID != 11:
                sd.play(vibratoHigh, sf)
                lastValueID = 11

        elif 2.625 < sensorvalue:
            if lastValueID != 12:
                sd.play(vibratoReallyHigh, sf)
                lastValueID = 12

    if state == 4:
        if 0 <= sensorvalue <= 0.875:
            if lastValueID != 13:
                sd.play(chorusSmall, sf)
                lastValueID = 13

        elif 0.875 < sensorvalue <= 1.75:
            if lastValueID != 14:
                sd.play(chorusMed, sf)
                lastValueID = 14

        elif 1.75 < sensorvalue <= 2.625:
            if lastValueID != 15:
                sd.play(chorusHigh, sf)
                lastValueID = 15

        elif 2.625 < sensorvalue:
            if lastValueID != 16:
                sd.play(chorusReallyHigh, sf)
                lastValueID = 16

    return lastValueID
>>>>>>> Stashed changes
