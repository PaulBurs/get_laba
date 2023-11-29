import matplotlib.pyplot as plt
import numpy as np
k = 2.531
sr = 1011
def read_mas(s):
    m = []
    data = np.loadtxt(s)
    for i in data:
        m.append(i[1])
    return m


x = [s[0]*0.06 for s in np.loadtxt("data0.txt")]
x = x[:-1]
data = []
for i in range(8):
    m = read_mas("data"+str(i*10)+".txt")
    for a in m:
        if (a - sr) > 0:
            data.append((a - sr)*k)
        else:
            data.append(0)


for m in range(8):
    step = 0
    q = 0
    y = []
    for i in range(m*100, (m+1)*100-1):
        step += 1
        v = (data[i] * 2 / 1.2) ** 0.5
        r = step * 0.06 * 0.001
        v1 = (data[i + 1] * 2 / 1.2) ** 0.5
        r1 = (step + 1) * 0.06 * 0.001
        q += 3.14 * (r * v + r1 * v1) * (r1 - r) * 1000 * 2
        y.append((data[i]*2/1.2)**0.5)


    plt.plot(x[:80:3], y[:80:3], label = ("l = " + str(m) + " см, расход = " + str(round(q, 3))+" г/с"))



plt.xlabel("Расстояние до центра сопла в мм")
plt.ylabel("Скорость воздуха м/с")
#включаем основную сетку
plt.grid(which='major', color = 'black')
# включаем дополнительную сетку
plt.grid(which='minor', linestyle=':', color = 'lightgray')
plt.tight_layout()
plt.legend()
plt.show()
