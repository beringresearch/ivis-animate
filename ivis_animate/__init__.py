import numpy as np
import matplotlib.pyplot as plt
from celluloid import Camera

class IvisAnimate():
    def __init__(self, ivis, frames=100):
        self.ivis=ivis
        self.frames=frames

    def animate(self, X, y=None, figsize=(6,6), dpi=200, c=None, **kwargs):

        if y is not None:
            unique_labels = list(set(y))
 
        fig = plt.figure(figsize=figsize, dpi=dpi)
        camera = Camera(fig)

        if c is None:
            c =  [0 for i in range(X.shape[0])]

        for iteration in range(self.frames):
            while True:
                try:
                    embeddings = self.ivis.fit_transform(X)

                    if y is not None:
                        coordinates = []
                        for l in unique_labels:
                            coordinates.append((np.average(embeddings[np.where(y==l),0]),
                                np.average(embeddings[np.where(y==l), 1])))
                            labels = {key: value for (key, value) in zip(unique_labels, coordinates)}


                    plt.scatter(x=embeddings[:, 0], y=embeddings[:, 1],
                            c=c, **kwargs)

                    if y is not None:
                        for l in unique_labels:
                            plt.annotate(l, labels[l])

                    camera.snap()
                except IndexError:
                    continue
                else:
                    break

        animation = camera.animate()

        return animation

