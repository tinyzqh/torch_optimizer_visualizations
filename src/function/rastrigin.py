import math
import numpy as np
import torch

from src.plot import plot_2d, plot_3d


def rastrigin(tensor):
    """
    # https://en.wikipedia.org/wiki/Test_functions_for_optimization
    :param tensor: input
    :return: result of function
    """

    x, y = tensor
    A = 10
    if isinstance(tensor, torch.Tensor):
        f = (
                A * 2
                + (x ** 2 - A * torch.cos(x * math.pi * 2))
                + (y ** 2 - A * torch.cos(y * math.pi * 2))
        )
    else:
        f = (
            A * 2
            + (x ** 2 - A * np.cos(x * math.pi * 2))
            + (y ** 2 - A * np.cos(y * math.pi * 2))
        )
    return f


if __name__ == "__main__":
    data_x = np.linspace(-2, 2, 250)
    data_y = np.linspace(-1, 3, 250)
    X, Y = np.meshgrid(data_x, data_y)
    Z = rastrigin([X, Y])

    plot_2d(X, Y, Z)

    plot_3d(X, Y, Z)

