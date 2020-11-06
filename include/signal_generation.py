import matplotlib.pyplot as plt
import numpy as np
import math as m

freq_ech = 100
freq_sig = 5
ampl = 8

p_ech = 1./freq_ech
signal_start = 5
sign_end = 10

time = np.arange(signal_start, sign_end+p_ech, p_ech)
y=ampl*np.sin(2*np.pi*freq_sig*time)
#print (time)
#print(y)

fig, ax = plt.subplots()
ax.plot(time,y,'-o')
plt.show()