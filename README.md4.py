import random
import math
from scipy.integrate import quad


def f(x):
    return x ** 2


def monte_carlo_integral(f, a, b, n=100000):
    """
    Обчислення визначеного інтеграла методом Монте-Карло.
    """
    y_max = max(f(a), f(b))

    points_inside = 0

    for _ in range(n):
        x = random.uniform(a, b)
        y = random.uniform(0, y_max)

        if y <= f(x):
            points_inside += 1

    rectangle_area = (b - a) * y_max
    return rectangle_area * points_inside / n


if __name__ == "__main__":
    a = 0
    b = 2

    mc_result = monte_carlo_integral(f, a, b)

    quad_result, error = quad(f, a, b)

    analytical = (b ** 3 - a ** 3) / 3

    print(f"Monte Carlo: {mc_result:.6f}")
    print(f"SciPy quad : {quad_result:.6f}")
    print(f"Analytical : {analytical:.6f}")
    print(f"Estimated error (quad): {error:e}")
