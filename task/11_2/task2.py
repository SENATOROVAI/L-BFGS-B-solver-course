# FULL PYTHON SOLUTION

def main() -> None:
    vals = list(map(float, input().split()))
    g1, g2, s11, s12, y11, y12, s21, s22, y21, y22 = vals
    pairs = [
        ((s11, s12), (y11, y12)),
        ((s21, s22), (y21, y22)),
    ]

    q1, q2 = g1, g2
    alphas = []
    rhos = []

    for (s1, s2), (y1, y2) in reversed(pairs):
        rho = 1.0 / (y1 * s1 + y2 * s2)
        alpha = rho * (s1 * q1 + s2 * q2)
        q1 = q1 - alpha * y1
        q2 = q2 - alpha * y2
        alphas.append(alpha)
        rhos.append(rho)

    (sl1, sl2), (yl1, yl2) = pairs[-1]
    gamma = (sl1 * yl1 + sl2 * yl2) / (yl1 * yl1 + yl2 * yl2)
    r1 = gamma * q1
    r2 = gamma * q2

    for ((s1, s2), (y1, y2)), alpha, rho in zip(pairs, reversed(alphas), reversed(rhos)):
        beta = rho * (y1 * r1 + y2 * r2)
        r1 = r1 + s1 * (alpha - beta)
        r2 = r2 + s2 * (alpha - beta)

    print(f"{-r1:.6f} {-r2:.6f}")


if __name__ == '__main__':
    main()
