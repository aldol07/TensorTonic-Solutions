def histogram_equalize(image: list) -> list:
    """
    Returns the histogram-equalized grayscale image.
    """
    # 1. Build histogram
    hist = [0] * 256

    for row in image:
        for pixel in row:
            hist[pixel] += 1

    # 2. Compute CDF
    cdf = [0] * 256
    cdf[0] = hist[0]

    for i in range(1, 256):
        cdf[i] = cdf[i - 1] + hist[i]

    # 3. Find smallest non-zero CDF value
    cdf_min = next(value for value in cdf if value > 0)

    total_pixels = sum(len(row) for row in image)

    # 4. Edge case: all pixels have same intensity
    if total_pixels == cdf_min:
        return [[0 for _ in row] for row in image]

    # 5. Create lookup table for intensity mapping
    mapping = [0] * 256

    for i in range(256):
        if cdf[i] == 0:
            mapping[i] = 0
        else:
            mapping[i] = round(
                (cdf[i] - cdf_min) / (total_pixels - cdf_min) * 255
            )

    # 6. Apply mapping
    return [[mapping[pixel] for pixel in row] for row in image]