# FULL PYTHON SOLUTION

def projected_gradient(
    x: np.ndarray,
    g: np.ndarray,
    lower: np.ndarray,
    upper: np.ndarray
) -> np.ndarray:
    pg = g.copy()
    for i in range(len(x)):
        if x[i] <= lower[i] and g[i] > 0:
            pg[i] = 0.0
        elif x[i] >= upper[i] and g[i] < 0:
            pg[i] = 0.0
    return pg


def main() -> None:
    x1, x2, g1, g2, l1, l2, u1, u2 = map(float, input().split())
    x = np.array([x1, x2], dtype=float)
    g = np.array([g1, g2], dtype=float)
    lower = np.array([l1, l2], dtype=float)
    upper = np.array([u1, u2], dtype=float)
    pg = projected_gradient(x, g, lower, upper)
    print(f"{pg[0]:.6f} {pg[1]:.6f}")


if __name__ == '__main__':
    main()
