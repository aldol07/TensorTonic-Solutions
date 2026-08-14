import numpy as np

def streaming_minmax_init(D):
    return {
        "min": np.full(D, np.inf),
        "max": np.full(D, -np.inf)
    }

def streaming_minmax_update(state, X_batch, eps=1e-8):
    X_batch = np.asarray(X_batch)

    batch_min = np.min(X_batch, axis=0)
    batch_max = np.max(X_batch, axis=0)

    state["min"] = np.minimum(state["min"], batch_min)
    state["max"] = np.maximum(state["max"], batch_max)

    return (X_batch - state["min"]) / (state["max"] - state["min"] + eps)