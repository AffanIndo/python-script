"""
This neural network predict what output should be based on this table:
            |    Inputs     | Outputs
Example 1   |   0   0   1   |    0
Example 2   |   1   1   1   |    1
Example 3   |   1   0   1   |    1
Example 4   |   0   1   1   |    0
New Input   |   1   0   0   |    ?

The output only look at first collumn, but the computer doesn't know it yet.
So, it will do the training until it find the pattern
"""

import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

training_inputs = np.array([[0, 0, 1],
                            [1, 1, 1],
                            [1, 0, 1],
                            [0, 1, 1]])

training_outputs = np.array([[0, 1, 1, 0]]).T

np.random.seed(1)

synaptic_weights = 2 * np.random.random((3, 1)) - 1

print('Random starting synaptic weights: ')
print(synaptic_weights)

for iteration in range(20000):
    input_layer = training_inputs

    outputs = sigmoid(np.dot(input_layer, synaptic_weights))

    error = training_outputs - outputs

    adjustments = error * sigmoid_derivative(outputs)

    synaptic_weights += np.dot(input_layer.T, adjustments)

print('Synaptic weights after training: ')
print(synaptic_weights)

print('Outputs after training: ')
print(outputs)
