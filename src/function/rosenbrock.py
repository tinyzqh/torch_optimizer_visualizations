import numpy as np

from src.plot import plot_2d, plot_3d


def rosenbrock(tensor):
    """
    # https://en.wikipedia.org/wiki/Test_functions_for_optimization
    :param tensor: input
    :return: result of function
    """
    x, y = tensor
    return (1 - x) ** 2 + 100 * (y - x ** 2) ** 2


if __name__ == "__main__":
    data_x = np.linspace(-2, 2, 250)
    data_y = np.linspace(-1, 3, 250)
    X, Y = np.meshgrid(data_x, data_y)
    Z = rosenbrock([X, Y])

    plot_2d(X, Y, Z)

    plot_3d(X, Y, Z)

