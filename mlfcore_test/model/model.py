import tensorflow as tf


class Autoencoder():

    def __init__(self, input_shape, layer_sizes, latent_size):
        self.input_shape = input_shape
        self.layer_sizes = layer_sizes
        self.latent_size = latent_size



    def build(self):
        """
        Build the model
        """
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(self.layer_sizes[0],  activation="relu", name="encoder1"),
            tf.keras.layers.Dense(self.layer_sizes[1],  activation="relu", name="encoder2"),
            tf.keras.layers.Dense(self.layer_sizes[2],  activation="relu", name="encoder3"),
            tf.keras.layers.Dense(self.latent_size,     activation="relu", name="latent"),
            tf.keras.layers.Dense(self.layer_sizes[2],  activation="relu", name="decoder1"),
            tf.keras.layers.Dense(self.layer_sizes[1],  activation="relu", name="decoder2"),
            tf.keras.layers.Dense(self.layer_sizes[0],  actviation="relu", name="decoder3"),
            tf.keras.layers.Dense(self.input_shape,     activation="linear", name="out_layer")
        ])

        return model








def create_model(input_shape):
    autoencoder = Autoencoder(input_shape=input_shape, layer_sizes=[128, 64, 32], latent_size=2)
    model = autoencoder.build()
    return model

