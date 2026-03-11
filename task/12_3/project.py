def project(x: np.ndarray, lower: np.ndarray, upper: np.ndarray) -> np.ndarray:
    return np.minimum(np.maximum(x, lower), upper)


def main() -> None:
    x1, x2, l1, l2, u1, u2 = map(float, input().split())
    x = np.array([x1, x2], dtype=float)
    lower = np.array([l1, l2], dtype=float)
    upper = np.array([u1, u2], dtype=float)
    p = project(x, lower, upper)
    print(f"{p[0]:.6f} {p[1]:.6f}")


if __name__ == '__main__':
    main()
