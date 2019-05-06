from ivis import Ivis
from sklearn import datasets
from sklearn.preprocessing import MinMaxScaler
from ivis_animate import IvisAnimate

iris = datasets.load_iris()
X = iris.data
X = MinMaxScaler().fit_transform(X)


model = Ivis(embedding_dims=2, k=30,
        epochs=1)
animation = IvisAnimate(model).animate(X)

animation.save('animation.mp4')
