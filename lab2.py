import numpy as np
import matplotlib.pyplot as plt
import unittest


def simpson_rule(f, a, b, n=1000):
    if n % 2 == 1:
        n += 1

    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)

    integral = (h / 3) * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])
    return integral


def f1(x):
    return 2 * x ** 2 + 1


def f2(x):
    return -2 * x ** 2 + 7


def calculate_area(a, b, n=1000):
    area = simpson_rule(lambda x: abs(f1(x) - f2(x)), a, b, n)
    return area


def plot_functions(a, b, area):
    x = np.linspace(a, b, 500)
    plt.figure(figsize=(10, 6))
    plt.plot(x, f1(x), label='y = 2x² + 1', color='blue')
    plt.plot(x, f2(x), label='y = -2x² + 7', color='red')
    plt.fill_between(x, f1(x), f2(x), where=(f1(x) > f2(x)), color='blue', alpha=0.2)
    plt.fill_between(x, f2(x), f1(x), where=(f2(x) > f1(x)), color='red', alpha=0.2)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Площадь между кривыми на [{a}, {b}]\nПлощадь = {area:.4f}')
    plt.legend()
    plt.grid(True)
    plt.show()


class TestIntegration(unittest.TestCase):
    def test_area_calculation(self):
        exact_value = 115.3333

        test_cases = [
            (100, 0.5),
            (1000, 0.05),
            (10000, 0.005)
        ]

        for n, tolerance in test_cases:
            with self.subTest(n=n):
                area = calculate_area(5, 6, n)
                self.assertAlmostEqual(area, exact_value, delta=tolerance,
                                       msg=f"Погрешность превышена при n={n}")


if __name__ == "__main__":
    a, b = 5, 6

    area = calculate_area(a, b)
    print(f"Площадь между кривыми на интервале [{a}, {b}]: {area:.4f}")

    plot_functions(a, b, area)

    unittest.main(argv=[''], verbosity=2, exit=False)
