import nashpy as nash
import numpy as np

# Strategie A: Rossa, Gialla, Bianca
# Strategie B: Rossa, Gialla, Bianca

A = np.array([
    [4, 6, 4],
    [4, 4, 6],
    [5, 3, 3]
])

B = np.array([
    [5, 4, 6],
    [7, 4, 4],
    [5, 5, 4]
])

game = nash.Game(A, B)

equilibria = game.support_enumeration()

for eq in equilibria:
    print(eq)
