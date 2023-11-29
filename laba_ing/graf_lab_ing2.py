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



data = []
for i in range(8):
    for a in read_mas("data"+str(i*10)+".txt"):
        if (a - sr) > 0:
            data.append((a - sr) * k)
        else:
            data.append(0)


y = []
x = []
for m in range(8):
    step = 0
    q = 0
    for i in range(m*100, (m+1)*100-1):
        step += 1
        v = (data[i]*2/1.2)**0.5
        r = step * 0.06 * 0.001
        v1 = (data[i+1]*2/1.2)**0.5
        r1 = (step + 1) * 0.06 * 0.001
        q += 3.14*(r*v + r1*v1)*(r1 - r) * 1000 * 2
    x.append(m*10)
    y.append(q)






plt.plot(x, y)
plt.xlabel("Расстояние до центра сопла в мм")
plt.ylabel("Расход воздуха в г/c")
#включаем основную сетку
plt.grid(which='major', color = 'black')
# включаем дополнительную сетку
plt.grid(which='minor', linestyle=':', color = 'lightgray')
plt.tight_layout()
plt.show()

delta_p = 142
