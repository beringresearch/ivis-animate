# ivis-animate

## Requirements

```
ffmpeg or mencoder  to save gifs
```


## Install

After cloning this repo run:
```
pip install --editable . from the root of the project.
```

## Examples

```python
from ivis import Ivis
from sklearn import datasets
from sklearn.preprocessing import MinMaxScaler
from ivis_animate import IvisAnimate

digits = datasets.load_digits()
X = digits.data
X = MinMaxScaler().fit_transform(X)


model = Ivis(embedding_dims=2, k=32,
        epochs=1)
animation = IvisAnimate(model, frames=500).animate(X, y=digits.target,
        c=digits.target)

animation.save('digits.mp4')
```

![digits](https://github.com/beringresearch/ivis-animate/blob/master/examples/digits.gif)
