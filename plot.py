import numpy as np
import matplotlib.pyplot as plt

# Valori del danno d
d = np.linspace(0, 15, 300)

# Quote all'equilibrio evolutivo
aggressivi = 3 / (d + 3)
prudenti = d / (d + 3)

# Grafico
plt.figure(figsize=(9, 5))

plt.plot(d, aggressivi, label="Aggressivi = 3 / (d + 3)")
plt.plot(d, prudenti, label="Prudenti = d / (d + 3)")

# Punto esempio d = 3
d_esempio = 3
agg_esempio = 3 / (d_esempio + 3)
prud_esempio = d_esempio / (d_esempio + 3)

plt.scatter(d_esempio, agg_esempio)
plt.scatter(d_esempio, prud_esempio)

plt.text(d_esempio + 0.2, agg_esempio, "d = 3, Aggressivi = 50%")
plt.text(d_esempio + 0.2, prud_esempio - 0.06, "d = 3, Prudenti = 50%")

plt.title("Equilibrio evolutivo al variare del danno d")
plt.xlabel("Danno da collisione d")
plt.ylabel("Quota nella popolazione")

plt.ylim(0, 1)
plt.grid(True)
plt.legend()

plt.show()
