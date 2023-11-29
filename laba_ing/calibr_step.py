import matplotlib.pyplot as plt
import numpy as np

x = [i for i in range(0, 500, 5)]
y = [i/10 for i in range(0, 300, 3)]
plt.plot(x, y)
plt.xlabel("Количесвто step в программе")
plt.ylabel("Расстояние, пройденное трубкой Пито")
#включаем основную сетку
plt.grid(which='major', color = 'black')
# включаем дополнительную сетку
plt.grid(which='minor', linestyle=':', color = 'lightgray')
plt.text(210,5.5, 'К = ' + f"{30/500} мм/step")
plt.tight_layout()
plt.show()


