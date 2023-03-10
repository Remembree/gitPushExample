import tkinter as tk
import pandas as pn
import matplotlib.pyplot as plt
import numpy as np

# CONSTANTS


r = tk.Tk()
r.title('Counting Seconds')
button = tk.Button(r, text='Stop', width=20, command=r.destroy)
button.pack()
r.mainloop()

# Data for plotting
v = [0, 1, 2.1, 3.2, 4.3, 5.4]
t = [0, 1, 2, 3, 4, 5]
# v_arranged = np.arange(v)
# t_arranged = np.arange(t)

fig, ax = plt.subplots()
ax.plot(v, t)

ax.set(xlabel='time (s)',
       ylabel='voltage (mV)',
       title='V vs T')
ax.grid()

fig.savefig("test.png")
plt.show()
