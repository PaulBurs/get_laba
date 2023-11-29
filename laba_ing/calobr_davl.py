import matplotlib.pyplot as plt
import numpy as np

f = np.loadtxt("calibr.txt")

m = []
for s in f:
    m.append(s[1])

sr = sum(m[10:])/len(m[10:])
k = 142/(max(m)-sr)
print(sr)
print(k)
x = [(s-sr)*k for s in m]
plt.plot(m, x)
plt.xlabel("Показания АЦП")
plt.ylabel("Давление в паскалях")
#включаем основную сетку
plt.grid(which='major', color = 'black')
# включаем дополнительную сетку
plt.grid(which='minor', linestyle=':', color = 'lightgray')
plt.text(1027,100, 'К = ' + f"{round(k, 3)} Па/value")
plt.tight_layout()
plt.show()



