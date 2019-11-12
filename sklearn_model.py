print("--> PCA Utilizando sklearn <--")
import numpy as np
from sklearn.decomposition import PCA

X = np.array([
        [2.5, 2.4],
        [0.5, 0.7],
        [2.2, 2.9],
        [1.9, 2.2],
        [3.1, 3.0],
        [2.3, 2.7],
        [2.0, 1.6],
        [1.0, 1.1],
        [1.5, 1.6],
        [1.1, 0.9]
])

X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
pca = PCA(n_components=2)
pca.fit(X) 
print(pca.explained_variance_ratio_)  
print(pca.singular_values_)
pca_transform = pca.fit_transform(X)
print(pca_transform)
