import matplotlib.pyplot as plt
import random

random.seed(42)
data = [random.normalvariate(0, 1) for i in range(1000)]

plt.hist(data, bins = 30, color = 'black', alpha = 0.5)
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Frequency catch")
plt.show()

