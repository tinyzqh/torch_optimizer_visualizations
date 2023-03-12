import matplotlib.pyplot as plt
import torch
import numpy as np

from src.function.rosenbrock import rosenbrock
from src.pipeline import pipeline
from src.plot import plot_2d_optim, plot_3d_optim


if __name__ == "__main__":
    import os
    os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

    optimizer_class = torch.optim.Adam
    seed = 0

    initial_state = (-2.0, 2.0)
    steps = pipeline(
        optim=optimizer_class,
        init_state=initial_state,
        lr=0.1428,
        fun=rosenbrock,
        iter_num=150
    )

    x = np.linspace(-2, 2, 250)
    y = np.linspace(-1, 3, 250)
    X, Y = np.meshgrid(x, y)
    Z = rosenbrock([X, Y])

    iter_x, iter_y = steps[0, :], steps[1, :]
    iter_z = rosenbrock([iter_x, iter_y])

    # plot_2d_optim(X, Y, Z, iter_x, iter_y, iter_z)

    plot_3d_optim(X, Y, Z, iter_x, iter_y, iter_z)

