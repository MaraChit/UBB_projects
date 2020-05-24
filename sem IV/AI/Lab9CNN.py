'''
Develop a CNN and train it in order to recognise handwritten digits using MNIST database.
Tensor flow is recommended as a tool.
'''
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten
from keras.utils import to_categorical
from keras.optimizers import SGD
import numpy as np

#load data
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

'''
scaling the image (normalising the input)
we divide by 255 because the RGB values range between (0,255) and we want to
reduce the interval to (0,1)
'''
train_images = (train_images / 255)
test_images = (test_images / 255)

#rescale the array to use it as input for keras
train_images = np.expand_dims(train_images, axis=3)
test_images = np.expand_dims(test_images, axis=3)

'''
sequential is a neuronal network model
we use it to put the layers
'''
model = Sequential([
  Conv2D(8, 3, input_shape=(28, 28, 1), use_bias=False),
  MaxPooling2D(pool_size=2),
  Flatten(),#make it one dimensional array
  Dense(10, activation='softmax'),#output layer
])

#using the gradient descent algorithm, with a learning rate of 0.00
model.compile(SGD(lr=.005), loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(
  train_images,
  to_categorical(train_labels), #classify
  batch_size=1,
  epochs=3,
)

model.evaluate(test_images, to_categorical(test_labels))