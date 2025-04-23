import numpy as np
import random

# Constants:
c = 3e8

# Colour of Light Source:
while True:
    spectrum = input("Enter the colour/type of the electromagnetic ray from the wave source: ")
    if spectrum.lower() == "red":
        wLength = random.randint(626,750)
        break
    elif spectrum.lower() == "orange":
        wLength = random.randint(591,625)
        break
    elif spectrum.lower() == "yellow":
        wLength = random.randint(566,590)
        break
    elif spectrum.lower() == "green":
        wLength = random.randint(521,565)
        break
    elif spectrum.lower() == "cyan":
        wLength = random.randint(496,520)
        break
    elif spectrum.lower() == "blue":
        wLength = random.randint(476,495)
        break
    elif spectrum.lower() == "indigo":
        wLength = random.randint(451,475)
        break
    elif spectrum.lower() == "violet":
        wLength = random.randint(381,450)
        break
    elif spectrum.lower() == "radio":
        wLength = random.randint(1e9+1,1e10)
        break
    elif spectrum.lower() == "micro":
        wLength = random.randint(1e6+1,1e9)
        break
    elif spectrum.lower() == "infrared":
        wLength = random.randint(751,1e6)
        break
    elif spectrum.lower() == "ultraviolet":
        wLength = random.randint(11,380)
        break
    elif spectrum.lower() == "X":
        wLength = random.randint(1,1000) / 100
        break
    elif spectrum.lower() == "gamma":
        wLength = random.randint(1,10) / 1000
        break
    else:
        print("\nPlease enter a colour/type from [red, orange, yellow, green, cyan, blue, indigo, violet, radio, micro, infrared, ultraviolet, X, gamma]")
        continue

f = c / (wLength * 10**(-9))

# Relative Speeds:
while True:
    v = float(input("Enter the relative speed of the wave source (c): ")) * c
    theta = float(input("Enter the angle of recession (°): "))
    if v > c:
        print("\nPlease enter a valid speed (smaller than or equal to the speed of light): ")
    else:
        vL = v * np.cos(np.radians(theta))
        vT = np.abs(v * np.sin(np.radians(theta)))
        break

# Generated Information:
print(f"\nFrequency: {f} Hz\nWavelength: {wLength} nm\nColour/Type of Electromagnetic Ray: {spectrum}")
print(f"\nRelative Longitudinal Velocity: {vL} m/s\nRelative Transverse Speed: {vT} m/s")

# Fractional Change in Frequency (Longitudinal):
def fFactor_L():
    k = np.sqrt((1 - (vL / c)) / (1 + (vL / c)))
    return k

# Fractional Change in Frequency (Transverse):
def fFactor_T():
    k = np.sqrt(1 - (vT / c)**2)
    return k

# Apparent Frequency:
fO = f * fFactor_L() * fFactor_T()

# Observed Colour:
wLengthO = c / fO * 10**9

if 625 < wLengthO <= 750:
    spectrumO = "red"
elif 590 < wLengthO <= 625:
    spectrumO = "orange"
elif 565 < wLengthO <= 590:
    spectrumO = "yellow"
elif 520 < wLengthO <= 565:
    spectrumO = "green"
elif 495 < wLengthO <= 520:
    spectrumO = "cyan"
elif 475 < wLengthO <= 495:
    spectrumO = "blue"
elif 450 < wLengthO <= 475:
    spectrumO = "indigo"
elif 380 < wLengthO <= 450:
    spectrumO = "violet"
elif wLengthO > 1e9:
    spectrumO = "radio"
elif 1e6 < wLengthO <= 1e9:
    spectrumO = "micro"
elif 750 < wLengthO <= 1e6:
    spectrumO = "infrared"
elif 10 < wLengthO <= 380:
    spectrumO = "ultraviolet"
elif 0.01 < wLengthO <= 10:
    spectrumO = "X"
elif wLengthO <= 0.01:
    spectrumO = "gamma"

# Results:
print(f"\nObserved Frequency: {fO} Hz\nObserved Wavelength: {wLengthO} nm\nColour/Type of Observed Electromagnetic Ray: {spectrumO}")