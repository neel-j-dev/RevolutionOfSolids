import gif
import numpy as np
import matplotlib.pyplot as plt


@gif.frame
def plot_volume(angle):
    fig = plt.figure(figsize=(20, 15))

    ax2 = fig.add_subplot(1, 1, 1, projection='3d')
    angles = np.linspace(0, 360, 20)
    x = np.linspace(-1, 2, 60)
    v = np.linspace(0, 2 * angle, 60)

    U, V = np.meshgrid(x, v)
    Y1 = (U ** 2 + 1) * np.cos(V)
    Z1 = (U ** 2 + 1) * np.sin(V)
    Y2 = (U + 3) * np.cos(V)
    Z2 = (U + 3) * np.sin(V)
    X = U
    ax2.plot_surface(X, Y1, Z1, alpha=0.2, color='blue', rstride=6, cstride=6)
    ax2.plot_surface(X, Y2, Z2, alpha=0.2, color='red', rstride=6, cstride=6)
    ax2.set_xlim(-3, 3)
    ax2.set_ylim(-5, 5)
    ax2.set_zlim(-5, 5)
    ax2.view_init(elev=50, azim=30 * angle)
    ax2.plot_wireframe(X, Y2, Z2)
    ax2.plot_wireframe(X, Y1, Z1, color='black')
    ax2._axis3don = False


frames = []
for i in np.linspace(0, 2 * np.pi, 20):
    frame = plot_volume(i)
    frames.append(frame)

gif.save(frames, 'images/vol1.gif', duration=500)

from IPython.display import Image

Image('images/vol1.gif')
