# FULL PYTHON SOLUTION

def project(x: np.ndarray, lower: np.ndarray, upper: np.ndarray) -> np.ndarray:
    return np.minimum(np.maximum(x, lower), upper)


def generalized_cauchy_point(
    x: np.ndarray,
    g: np.ndarray,
    lower: np.ndarray,
    upper: np.ndarray
) -> np.ndarray:
    return project(x - g, lower, upper)


def main() -> None:
    x1, x2, g1, g2, l1, l2, u1, u2 = map(float, input().split())
    x = np.array([x1, x2], dtype=float)
    g = np.array([g1, g2], dtype=float)
    lower = np.array([l1, l2], dtype=float)
    upper = np.array([u1, u2], dtype=float)
    xc = generalized_cauchy_point(x, g, lower, upper)
    print(f"{xc[0]:.6f} {xc[1]:.6f}")


if __name__ == '__main__':
    main()
