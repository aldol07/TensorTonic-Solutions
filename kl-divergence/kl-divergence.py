import numpy as np

def kl_divergence(p: list, q: list, eps: float = 1e-12) -> float:
    p = np.asarray(p)
    q = np.asarray(q)

    mask = p > 0
    return float(np.sum(p[mask] * np.log(p[mask] / np.maximum(q[mask], eps))))