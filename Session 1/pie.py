import matplotlib.pyplot as plt
categori = ["Pizza 1", "Pizza 2", "Pizza 3", "Puzza 4"]
pretages = [25, 30, 15, 30]

explode = [0, 0.1, 0, 0]
colors = ['red', 'green', 'blue', 'yellow']

plt.pie(pretages, explode = explode, labels = categori, colors = colors, shadow = True)

plt.title("Tokos eli")
plt.legend(categori)
plt.show()

