import mlflow
import mlflow.tensorflow
import tensorflow as tf
import numpy as np


def create_model():
    model = tf.keras.Sequential([
        tf.keras.layers.LSTM(128, return_sequences=True, input_shape=(20, 1)),
        tf.keras.layers.LSTM(128, return_sequences=True),
        tf.keras.layers.LSTM(128),
        tf.keras.layers.Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    return model


def generate_data(n_steps=20, samples=1000):
    t = np.linspace(0, 100, samples + n_steps)
    signal = np.sin(t)
    X, y = [], []
    for i in range(samples):
        X.append(signal[i:i + n_steps])
        y.append(signal[i + n_steps])
    X = np.array(X)[..., None]
    y = np.array(y)
    return X, y


if __name__ == "__main__":
    mlflow.set_tracking_uri("http://mlflow:5000")
    mlflow.tensorflow.autolog()

    X, y = generate_data()
    model = create_model()
    model.fit(X, y, epochs=5, batch_size=32, validation_split=0.2)
