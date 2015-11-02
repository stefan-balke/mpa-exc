"""Exercise 1.8.
Assume an equal-tempered scale that consists of 17 tones per octave
and a reference pitch p = 100 having a center frequency of 1000 Hz.
Specify a formula similar to (1.1), which yields the center frequencies
for the pitches p \in [0 : 255]. In particular, determine the center frequency
for the pitches p = 83, p = 66, and p = 49 in this scale. What is the difference (in cents)
between two subsequent pitches in this scale?
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

pitch_center = 100
pitch_center_freq = 1000
scale_divisions = 17
freq_pitch = lambda p: pitch_center_freq * 2**((p-pitch_center)/17)

chromatic_scale = np.arange(0, 255)

print(chromatic_scale)
print(freq_pitch(chromatic_scale))

plt.step(np.arange(len(chromatic_scale)), freq_pitch(chromatic_scale), where='mid')
plt.title('Chromatic Scale with 17 Tones per Octave')
plt.xlabel('Scale Position')
plt.ylabel('Frequency (Hz)')

plt.show()
