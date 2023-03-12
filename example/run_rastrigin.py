import torch
import numpy as np

from src.function.rastrigin import rastrigin
from src.pipeline import pipeline
from src.plot import plot_2d_optim, plot_3d_optim


if __name__ == "__main__":
    import os
    os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

    optimizer_class = torch.optim.Adam
    seed = 0

    initial_state = (-2.0, 3.5)
    steps = pipeline(
        optim=optimizer_class,
        init_state=initial_state,
        lr=1.103532088287447,
        fun=rastrigin,
        iter_num=150
    )

    x = np.linspace(-4.5, 4.5, 250)
    y = np.linspace(-4.5, 4.5, 250)
    X, Y = np.meshgrid(x, y)
    Z = rastrigin([X, Y])

    iter_x, iter_y = steps[0, :], steps[1, :]
    iter_z = rastrigin([iter_x, iter_y])

    # plot_2d_optim(X, Y, Z, iter_x, iter_y, iter_z)

    plot_3d_optim(X, Y, Z, iter_x, iter_y, iter_z)