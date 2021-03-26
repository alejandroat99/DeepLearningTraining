# Especificaciones del Servidor

## Peticiones
Se necesita siempre de información para las funcionalidades del servidor, por lo que
solo se usarán prticiones de tipo **POST**.

Las peticiones se dicviden en dos bloques principales:
- La estructura de la red
- Lo que se quiere hacer con la red

### Estructura de la red

1. Lista con la información de cada capa:
	- type: nombre identificador de la capa. [dense, conv2d, maxpooling2d, flatten]
	- número de neuronas: cantidad de neuronas que hay en la capa
	- f. activación: función de activación de la capa. [relu, sigmoid, softmax, softplus, softsign, tanh, selu, elu, exponential]
	- kernel_size: tamaño del kernel para las neuronas de tipo conv2d
	- input_shape: shape de los datos de entrada de la red, debe aparecer
2. Características de la red
	- loss: función de coste de la red. [binary_crossentropy, categorical_crossentropy, sparse_categorical_crossentropy, mean_squared_error, mean_absolute_error]
	- optimizer: optimizador para realizar los ajustes. [adam, sgd, rmsprop, adadelta, adagrad, adamax, nadam, ftrl]
	- learning_rate: opcional
	- metrics: metricas que se usarán en el proceso. [acc/accuracy,  binary_accuracy, categorical_accuracy, ...]

Ejemplo:

```json
{
	"structure":{
		"layers": [
			{
				"type": "Dense",
				"n_neurons": 32,
				"activation": "relu",
				"input_shape": [2]
			},
			{
				"type": "Dense",
				"n_neurons": 64,
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
			"optimizer": "sgd",
			"metrics": ["accuracy"]
		}
	}
}
```