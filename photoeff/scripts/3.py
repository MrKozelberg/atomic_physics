import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import c
from scipy.constants import e

nu = np.asarray([6,5.86,5.70,5.54,5.38,5.22,5.05,4.86, 4.68, 4.44, 4.20, 3.98, 3.72, 3.46, 3.32, 3.16]) * 10**14
v = np.asarray([7,6,6,6,5.5,5.2,4.8,4.4,4,3.4,3,2.4,1.6,1,0.4,0])*0.25

h = np.mean(v / nu) * e

err = np.std(v/nu)*e

print(h, "+-", err)
