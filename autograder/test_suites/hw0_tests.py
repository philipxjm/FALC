import sys
# from homeworks.hw0.unzipped.assignment import Model  # noqa
from tensorflow.examples.tutorials.mnist import input_data  # noqa
import os  # noqa
import tensorflow as tf  # noqa
import importlib.util

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


def accuracy(model):
    correct_prediction = tf.equal(tf.argmax(model.prediction, 1),
                                  tf.argmax(model.label, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    return accuracy


def acc_test(assignment, threshold=0.85):
    mnist = input_data.read_data_sets("../data/mnist/", one_hot=True)
    image = tf.placeholder(tf.float32, [None, 784])
    label = tf.placeholder(tf.float32, [None, 10])

    try:
        model = assignment.Model(image, label)
        sess = tf.Session()
        sess.run(tf.global_variables_initializer())

        for _ in range(10):
            images, labels = mnist.test.images, mnist.test.labels
            error = sess.run(model.error, {image: images, label: labels})
            print('Test error {:6.2f}%'.format(100 * error))
            for _ in range(60):
                images, labels = mnist.train.next_batch(100)
                sess.run(model.optimize, {image: images, label: labels})
        images, labels = mnist.test.images, mnist.test.labels
        acc = sess.run(accuracy(model), {image: images, label: labels})
        if acc > threshold:
            return True
        return False
    except Exception as e:
        print(e)
        return False


def run_suite_on_file(file_path):
    tf.reset_default_graph()
    spec = importlib.util.spec_from_file_location(
                    "assignment", file_path)
    assignment = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(assignment)
    score = 0
    if acc_test(assignment):
        score += 1
    return score

# print(run_suite_on_file("../homeworks/hw0/unzipped/jx24/assignment.py"))
