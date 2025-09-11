import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

days = np.arange(1,32)
print(days)

temperatures = np.array([
    32, 34, 33, 31, 30, 29, 28, 31, 32, 34,
    35, 33, 32, 31, 30, 29, 28, 30, 31, 33,
    34, 36, 35, 34, 33, 31, 30, 29, 28, 30, 32
])

plt.plot(days,temperatures, label='temperature',marker='d')
plt.show()

