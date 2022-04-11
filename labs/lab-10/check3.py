# TensorFlow and tf.keras
import tensorflow as tf

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageOps

fashion_mnist = tf.keras.datasets.fashion_mnist

(train_images, train_labels), (test_images,
                               test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

train_images = train_images / 255.0

test_images = test_images / 255.0

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(10)
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(
                  from_logits=True),
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=10)

test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

print('\nTest accuracy:', test_acc)

probability_model = tf.keras.Sequential([model,
                                         tf.keras.layers.Softmax()])

# predictions = probability_model.predict(test_images)


def plot_image(predictions_array, true_label, img):
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])

    plt.imshow(img, cmap=plt.cm.binary)

    predicted_label = np.argmax(predictions_array)
    if predicted_label == true_label:
        color = 'blue'
    else:
        color = 'red'

    plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                         100*np.max(predictions_array),
                                         class_names[true_label]),
               color=color)


def plot_value_array(predictions_array, true_label):
    plt.grid(False)
    plt.xticks(range(10))
    plt.yticks([])
    thisplot = plt.bar(range(10), predictions_array, color="#777777")
    plt.ylim([0, 1])
    predicted_label = np.argmax(predictions_array)

    thisplot[predicted_label].set_color('red')
    thisplot[true_label].set_color('blue')


lab_images = []

img = Image.open("./test_images/processed/shirt.png")
img = np.array(img)
img = img / 255.0
img = (np.expand_dims(img, 0))
lab_images.append((img, 0))

img = Image.open("./test_images/processed/hoodie.png")
img = np.array(img)
img = img / 255.0
img = (np.expand_dims(img, 0))
lab_images.append((img, 2))

img = Image.open("./test_images/processed/sneaker.png")
img = np.array(img)
img = img / 255.0
img = (np.expand_dims(img, 0))
lab_images.append((img, 7))

for img in lab_images:
    predictions_single = probability_model.predict(img[0])

    print(predictions_single[0])

    plt.figure(figsize=(4, 2))
    plt.subplot(1, 2, 1)
    plot_image(predictions_single[0], img[1], img[0][0])
    plt.subplot(1, 2, 2)
    plot_value_array(predictions_single[0], img[1])

    plt.tight_layout()
    plt.show()
