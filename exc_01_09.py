"""Exercise 1.9.
Write a small computer program to calculate the differences (in cents)
between the first 16 harmonics of the note C2 and the center frequencies
of the closest notes of the twelve-tone equal-tempered scale (see Figure 1.20).
What are the corresponding differences when considering the
harmonics of another note such as Bb4?
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

freq_A4 = 440
freq_pitch = lambda p: freq_A4 * 2**((p-69)/12)
freq_C2 = freq_pitch(36)

harmonics = np.arange(1, 16)
print(harmonics)

freq_harmonics = freq_C2 * harmonics
print(freq_harmonics)

# get the whole pitch range
freq_pitches = freq_pitch(np.arange(255))


def harmonics_diff(harmonics, freq_harmonics, freq_pitches):
    closest_pitches = []
    for cur_harmonic in freq_harmonics:
        distances = np.abs(cur_harmonic-freq_pitches)
        closest_pitches.append(np.argmin(distances))

    # difference in cents
    diff = np.log2(freq_harmonics/freq_pitches[closest_pitches])*1200

    return closest_pitches, diff

closest_pitches, diff = harmonics_diff(harmonics, freq_harmonics, freq_pitches)
print(zip(closest_pitches, diff))

plt.stem(harmonics, diff)
plt.title('Harmonic Series for C2')
plt.xlabel('Harmonic')
plt.ylabel('$\Delta$ Frequency (cents)')
plt.xticks(harmonics)
plt.ylim([-50, 50])
plt.grid()


freq_Bb4 = freq_pitch(70)
freq_harmonics = freq_Bb4 * harmonics
closest_pitches, diff = harmonics_diff(harmonics, freq_harmonics, freq_pitches)
print(zip(closest_pitches, diff))

plt.figure()
plt.stem(harmonics, diff)
plt.title('Harmonic Series for Bb4')
plt.xlabel('Harmonic')
plt.ylabel('$\Delta$ Frequency (cents)')
plt.xticks(harmonics)
plt.ylim([-50, 50])
plt.grid()

plt.show()
