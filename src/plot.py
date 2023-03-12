from matplotlib import cm
import matplotlib.pyplot as plt


def plot_2d(x, y, z):
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(1, 1, 1)
    ax.contour(x, y, z, 90, cmap='jet')  # 绘制等高线
    plt.show()


def plot_3d(x, y, z):
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, alpha=.9, cmap=cm.coolwarm)  # 绘制三维平面
    plt.show()


def plot_2d_optim(x, y, z, iter_x, iter_y, iter_z):
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(1, 1, 1)
    ax.contour(x, y, z, 90, cmap='jet')

    plt.ion()
    for i in range(len(iter_x)):
        ax.plot(iter_x[:i], iter_y[:i], color='r', marker='x')
        plt.savefig('figures_2d/' + str(i) + '.png')
        plt.pause(0.001)


def plot_3d_optim(x, y, z, iter_x, iter_y, iter_z):
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, alpha=.4, cmap=cm.coolwarm)

    for i in range(len(iter_x)):
        ax.plot3D(iter_x[:i], iter_y[:i], iter_z[:i], 'red')
        plt.savefig('figures_3d/' + str(i) + '.png')
        plt.pause(0.001)

