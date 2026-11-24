import matplotlib.pyplot as plt
import numpy as np
data = np.array([10,20,20,30,30,30,40,40,50,])
plt.hist(data, bins=5, edgecolor='black')
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()