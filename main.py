import numpy as np


def predict(transition, state):
    return transition @ state

def update(measurement, prediction):
    val = measurement * prediction
    normalizer = np.sum(val)
    return val / normalizer

# open closed
state = np.array([0.5, 0.5])
transition = np.array([[1, 0], [0, 1]]).T

prediction = predict(transition, state)
measurement = np.array([0.6, 0.2])
updated = update(measurement, prediction)
print(updated)


transition = np.array([[1, 0.8], [0, 0.2]])
prediction = predict(transition, updated)
print(prediction)
measurement = np.array([0.6, 0.2])
print(update(measurement, prediction))

