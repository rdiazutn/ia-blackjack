import tensorflow as tf
print(tf.reduce_sum(tf.random.normal([1000, 1000])))
print("IS WORKING IF IT LOOKS LIKE tf.Tensor(-1388.6987, shape=(), dtype=float32)")