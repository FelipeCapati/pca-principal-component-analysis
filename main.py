import numpy as np
from pca import PCA, PcaType

data = np.array([
        [2.5, 0.5, 2.2, 1.9, 3.1, 2.3, 2.0, 1.0, 1.5, 1.1],
        [2.4, 0.7, 2.9, 2.2, 3.0, 2.7, 1.6, 1.1, 1.6, 0.9]
])

pca = PCA()
print(pca.fit(data=data, pcaType=PcaType.Two))