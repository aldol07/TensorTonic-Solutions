def seasonal_average(series: list, period: int) -> list:
    sums = [0.0] * period
    counts = [0] * period

    for i, x in enumerate(series):
        sums[i % period] += x
        counts[i % period] += 1

    return [sums[i] / counts[i] for i in range(period)]