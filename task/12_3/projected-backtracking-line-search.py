# FULL PYTHON SOLUTION

def f(x1, x2):
    return (x1 - 3.0) ** 2 + (x2 - 0.5) ** 2


def project(x1, x2, l1, l2, u1, u2):
    return min(max(x1, l1), u1), min(max(x2, l2), u2)


def backtracking_line_search_with_projection(x1, x2, p1, p2, l1, l2, u1, u2, g1, g2):
    alpha = 1.0
    beta = 0.5
    c = 1e-4
    fx = f(x1, x2)
    gp = g1 * p1 + g2 * p2

    while True:
        t1, t2 = project(x1 + alpha * p1, x2 + alpha * p2, l1, l2, u1, u2)
        if f(t1, t2) <= fx + c * alpha * gp:
            return alpha
        alpha *= beta
        if alpha < 1e-12:
            return alpha


def main() -> None:
    x1, x2, p1, p2, l1, l2, u1, u2, g1, g2 = map(float, input().split())
    alpha = backtracking_line_search_with_projection(x1, x2, p1, p2, l1, l2, u1, u2, g1, g2)
    print(f"{alpha:.6f}")


if __name__ == '__main__':
    main()
