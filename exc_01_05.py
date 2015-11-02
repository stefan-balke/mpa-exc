"""Exercise 1.5.
Using (1.1), compute the center frequencies for all notes
of the C-major scale C4, D4, E4, F4, G4, A4, B4, C5 and for all notes
of the C-minor scale C4, D4, Eb4, F4, G4, Ab4, Bb4, C5 (see also Figure 1.5).
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

freq_A4 = 440
freq_pitch = lambda p: freq_A4 * 2**((p-69)/12)
print(freq_pitch(69))

# Define scales, one octave
template_scale_major = lambda start: np.array([start,
                                               start+2,
                                               start+4,
                                               start+5,
                                               start+7,
                                               start+9,
                                               start+11,
                                               start+12])

template_scale_minor = lambda start: np.array([start,
                                               start+2,
                                               start+3,
                                               start+5,
                                               start+7,
                                               start+8,
                                               start+10,
                                               start+12])

scale_c_maj = freq_pitch(template_scale_major(60))
scale_c_min = freq_pitch(template_scale_minor(60))

print(scale_c_maj)
print(scale_c_min)

plt.step(np.arange(len(scale_c_maj)), scale_c_maj, where='mid')
plt.title('Major Scale')
plt.xlabel('Scale Position')
plt.ylabel('Frequency (Hz)')

plt.figure()
plt.step(np.arange(len(scale_c_min)), scale_c_min, where='mid')
plt.title('Minor Scale')
plt.xlabel('Scale Position')
plt.ylabel('Frequency (Hz)')

plt.show()
