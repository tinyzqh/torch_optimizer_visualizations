import torch
import numpy as np


def pipeline(optim, init_state, lr, fun, iter_num):
    x = torch.Tensor(init_state).requires_grad_(True)
    optimizer = optim([x], lr=lr)
    steps = np.zeros((2, iter_num + 1))
    steps[:, 0] = np.array(init_state)
    for i in range(1, iter_num + 1):
        optimizer.zero_grad()
        f = fun(x)
        f.backward(create_graph=True, retain_graph=True)
        torch.nn.utils.clip_grad_norm_(x, 1.0)
        optimizer.step()
        steps[:, i] = x.detach().numpy()
    return steps

