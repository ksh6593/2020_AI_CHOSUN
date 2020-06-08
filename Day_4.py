import tensorflow as tf
import numpy as np
# 데이터 받아오기.
mnist = tf.keras.datasets.mnist
# 데이터 로드하기.
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# 뉴럴 네트워크
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(30, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])
#
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

#
print(np.shape(x_train), np.shape(y_train))
print(type(x_train), type(y_train))
model.fit(x_train, y_train, epochs=5)

# 검증
print(model.predict(x_test[0:3]))
print(y_test[0:3])


model.save_weights('save_model')