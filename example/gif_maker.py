import imageio

images = []
filenames = ['figures_3d/' + str(i) + '.png' for i in range(150)]

imageio.plugins.freeimage.download()
print('  ...')
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('../pic/rosenbrock_3d.gif', images, format='GIF-FI', duration=0.001)