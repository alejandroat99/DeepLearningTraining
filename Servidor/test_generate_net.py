import neural_network_util as util

petition1 = {
    "structure": {
        "layers": [
            {
                "type": "Dense",
                "n_neurons": 4,
                "activation": "relu",
                "input_shape": [2,1]
            },
            {
                "type": "Dense",
                "n_neurons": 8,
                "activation": "relu"
            },
            {
                "type": "Dense",
                "n_neurons": 1,
                "activation": "sigmoid"
            }
        ],
        "compilation": {
            "loss": "binary_crossentropy",
            "optimizer": "adam",
            "metrics": ["accuracy"]
        }
    }
}

petition2 = {
    "structure": {
        "layers": [
            {
                "type": "Conv2D",
                "n_neurons": 32,
                "activation": "relu",
                "input_shape": [28, 28, 1],
                "kernel_size": 3
            },
            {
                "type": "MaxPooling2D"
            },
            {
                "type": "Conv2D",
                "n_neurons": 64,
                "activation": "relu",
                "kernel_size": 3
            },
            {
                "type": "Flatten"
            },
            {
                "type": "Dense",
                "n_neurons": 10,
                "activation": "softmax"
            }
        ],
        "compilation": {
            "loss": "categorical_crossentropy",
            "optimizer": "adam",
            "metrics": ["accuracy"]
        }
    }
}

m = util.create_net(petition2['structure'])
m.summary()