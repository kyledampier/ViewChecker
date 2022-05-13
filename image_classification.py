import tensorflow as tf
IMAGE_SHAPE=(224, 224, 3)

base_model = tf.keras.applications.VGG16(
    weights='imagenet',  # Load weights pre-trained on ImageNet.
    input_shape=IMAGE_SHAPE,
    include_top=True)

base_model.trainable = False
base_model.summary()

def classify(img):
    print(img)
    x =  tf.keras.applications.vgg16.preprocess_input(img)
    preds = base_model.predict(x)
    return preds