import matplotlib.pyplot as plt
import numpy as np
x = np.array(["A","B","C","D","E"])
y = np.array([10,20,15,25,30])
plt.bar(x,y)
plt.title("Bar Plot")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()