import numpy as np

class Model:
    def predict(self, X):
        # Un modelo simple que predice ceros por defecto
        return np.zeros(len(X), dtype=int)