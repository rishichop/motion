import tensorflow as tf

# Check if TensorFlow is using GPU
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

# Alternatively, you can list all devices being used
print("Available devices:", tf.config.list_physical_devices())