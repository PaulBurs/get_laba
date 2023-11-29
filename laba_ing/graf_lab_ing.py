import matplotlib.pyplot as plt
import numpy as np
def read_mas(s):
    m = []
    data = np.loadtxt(s)
    for i in data:
        m.append(i[1])
    return m

k = 2.531
sr = 1011
x = [s[0]*0.06 for s in np.loadtxt("data0.txt")]
data = []
for i in range(8):
    for a in read_mas("data"+str(i*10)+".txt"):
        data.append((a-1011) * k )

y = []

for m in range(8):
    for i in range(m*100, (m+1)*100):
        y.append(data[i])

    x = x[0:50]
    y = y[0:50]

    plt.plot(x[::3], y[::3], label = "l ="+str(m*1)+"см")
    y=[]


plt.xlabel("Расстояние до центра сопла в мм")
plt.ylabel("Давление в струе")
#включаем основную сетку
plt.grid(which='major', color = 'black')
# включаем дополнительную сетку
plt.grid(which='minor', linestyle=':', color = 'lightgray')
plt.tight_layout()
plt.legend()
plt.show()

