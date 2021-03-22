import matplotlib.pyplot as plt
import numpy as np


n = np.linspace(1, 10 ** 123)
plt.plot(n, n ** 0.1, label="n ^ .1")
plt.plot(n, np.log(n) ** 5, label="(log n) ^ 5")
plt.legend(loc="upper left")
plt.show()
