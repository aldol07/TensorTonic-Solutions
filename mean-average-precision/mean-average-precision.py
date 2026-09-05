import numpy as np

def mean_average_precision(y_true_list: list, y_score_list: list, k: int | None = None) -> dict:
    """
    Returns a dictionary with map_value and ap_per_query.
    """
    ap_per_query = []

    for y_true, y_score in zip(y_true_list, y_score_list):
        y_true = np.asarray(y_true)
        y_score = np.asarray(y_score)

        order = np.argsort(-y_score)
        sorted_true = y_true[order]

        total_relevant = np.sum(sorted_true)

        if total_relevant == 0:
            ap_per_query.append(0.0)
            continue

        limit = len(sorted_true) if k is None else min(k, len(sorted_true))
        relevant = sorted_true[:limit]

        precision = np.cumsum(relevant) / np.arange(1, limit + 1)
        ap = np.sum(precision * relevant) / total_relevant

        ap_per_query.append(ap)

    map_value = np.mean(ap_per_query) if ap_per_query else 0.0

    return {
        "map_value": float(map_value),
        "ap_per_query": [float(ap) for ap in ap_per_query]
    }