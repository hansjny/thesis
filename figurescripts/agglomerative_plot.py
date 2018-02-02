import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
x = np.random.uniform(0, 10, 10);
y = np.random.uniform(0, 10, 10);
colors = ["g", "r", "b","#000000", "#aacc00", "#bb0088","#ffa100", "#00ffff", "#ffee00", "#ff00dc"]

X = [[i] for i in [2, 8, 0, 4, 1, 9, 9, 0]]
print(X)
Z = linkage(X, 'single')
fig = plt.figure(figsize=(25, 10))
dendrogram(Z)
#plt.scatter(x,y, c=colors, linewidth=5, edgecolors=colors)
plt.show()

