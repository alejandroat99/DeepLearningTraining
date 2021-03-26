from tensorflow import keras
import numpy as np

SYNTAX = {
	"neuron_type": ["DENSE", "CONV2D", "MAXPOOLING2D", "FLATTEN"],
	"activation_function": ["RELU", "SIGMOID", "SOFTMAX", "SOFTPLUS", "SOFTSIGN", "TANH", "SELU", "ELU", "EXPONENTIAL"],
	"loss_function": ["BINARY_CROSSENTROPY", "CATEGORICAL_CROSSENTROPY", "SPARSE_CATEGORICAL_CROSSENTROPY", "MEAN_SQUARED_ERROR", "MEAN_ABSOLUTE_ERROR"],
	"optimizer": ["ADAM", "SGD", "RMSPROP", "ADADELTA", "ADAGRAD", "ADAMAX", "NADAM", "FTRL"],
	"metrics": ["ACCURACY"],
	"valid_input_types": ["DENSE", "CONV2D"],
	"required_number_neurons": ["DENSE", "CONV2D"],
	"required_activation": ["DENSE", "CONV2D"]
}


def check_layers(layers):
	"""
	This function checks if the layers syntax of the net is valid
	"""
	for i, l in enumerate(layers):

		# LAYER TYPE CHECK
		if not "type" in l:
			raise SyntaxError(f"Layer {i}: missing \"type\" parameter")

		if not l['type'].upper() in SYNTAX['neuron_type']:
			raise SyntaxError(f"Layer {i}: invalid layer type, no type named \"{l['type']}\"")

		# NUMBER OF NEURONS CHECK
		if not "n_neurons" in l and l['type'].upper() in SYNTAX['required_number_neurons']:
			raise SyntaxError(f"Layer {i}: missing \"n_neurons\" parameter")

		if l['type'].upper() in SYNTAX['required_number_neurons'] and l['n_neurons'] <= 0:
			raise ValueError(f"Layer {i}: invalid number of neurons for the layer, use a positive value")
		
		# ACTIVATION FUNCTION CHECK
		if not "activation" in l and l['type'].upper() in SYNTAX['required_activation']:
			raise SyntaxError(f"Layer {i}: missing \"activation\" parameter")

		if l['type'].upper() in SYNTAX['required_activation'] and not l['activation'].upper() in SYNTAX['activation_function']:
			raise SyntaxError(f"Layer {i}: invalid activation function, no function named \"{l['activation']}\"")

		# KERNEL SIZE CHECK
		if l['type'].upper == "CONV2D":
			if "kernel_size" not in l:
				raise SyntaxError(f"Layer {i}: missing \"kernel_size\" parameter")

		# INPUT SHAPE CHECK
		if i == 0:
			if not "input_shape" in l:
				raise SyntaxError("missing \"input_shape\" parameter")

			if l['type'].upper() not in SYNTAX['valid_input_types']:
				raise ValueError("invalid input layer type")


def check_compilation(compilation):
	"""
	This function checks if the compile configuration is valid
	"""
	# CHECK IF THE REQUIERED PARAMETERS ARE PRESENT
	if "loss" not in compilation:
		raise SyntaxError("missing \"loss\" parameter")

	if "optimizer" not in compilation:
		raise SyntaxError("missing \"optimizer\" parameter")

	if "metrics" not in compilation:
		raise SyntaxError("missing \"metrics\" parameter")

	# CHECK THE VALUES OF THE PARAMETERS
	if not compilation['loss'].upper() in SYNTAX['loss_function']:
		raise ValueError(f"invalid loss function, no function named {compilation['loss']}")

	if compilation['optimizer'].upper() not in SYNTAX['optimizer']:
		raise ValueError(f"invalid optimizer, no optimizer named {compilation['optimizer']}")

	for m in compilation['metrics']:
		if m.upper() not in SYNTAX['metrics']:
			raise ValueError(f"invalid metric, no metric named {m}")


def create_layer(layer, is_input=False):
	l = None
	# CHECK IF THE LAYER NEEDS A NUMBER OF NEURONS
	if layer['type'].upper() in SYNTAX['required_number_neurons']:
		n_neurons = layer['n_neurons']

	# CHECK IF THE LAYER NEEDS AN ACTIVATION FUNCTION
	if layer['type'].upper() in SYNTAX['required_activation']:
		activation = layer['activation']
	
	# GENERATE AN INPUT LAYER
	if is_input:
		input_shape = [ dim for dim in layer['input_shape']]
		input_shape = np.array(input_shape)

		if layer['type'].upper() == "DENSE":
			l = keras.layers.Dense(n_neurons, activation=activation, input_shape=input_shape)
		elif layer['type'].upper() == "CONV2D":
			k_size = layer['kernel_size']
			kernel_size = np.array([k_size, k_size])
			l = keras.layers.Conv2D(n_neurons, activation=activation, input_shape=input_shape, kernel_size=kernel_size)
		else:
			raise RuntimeError("The input layer type does not match with any of the valid input layer types")
	
	# GENERATE A NORMAL LAYER
	else:
		if layer['type'].upper() == 'DENSE':
			l = keras.layers.Dense(n_neurons, activation=activation)
		elif layer['type'].upper() == 'CONV2D':
			k_size = layer['kernel_size']
			kernel_size = np.array([k_size, k_size])
			l = keras.layers.Conv2D(n_neurons, activation=activation, kernel_size=kernel_size)
		elif layer['type'].upper() == 'MAXPOOLING2D':
			l = keras.layers.MaxPooling2D()
		elif layer['type'].upper() == 'FLATTEN':
			l = keras.layers.Flatten()
		else: 
			raise RuntimeError("The layer type does not match with any valid layer type")

	return l

def built_model(layers):
	"""
	This function is in charge for generate de layers and pack them into the model
	"""
	model = keras.models.Sequential()

	for i, l in enumerate(layers):
		if i == 0:
			model.add(create_layer(l, is_input=True))
		else:
			model.add(create_layer(l))
	return model

def compile_model(model, compile_data):
	"""
	This function compiles the model of the neural network with the parameters of the petition
	"""
	loss = compile_data['loss']
	optimizer = compile_data['optimizer']
	metrics = compile_data['metrics']

	model.compile(loss=loss, optimizer=optimizer, metrics=metrics)


def create_net(structure):
	"""
	This function creates the neuronal net with the petition data
	"""
	if "layers" not in structure:
		raise SyntaxError("missing \"layers\" parameter")

	if "compilation" not in structure:
		raise SyntaxError("missing \"compilation\" parameter")

	check_layers(structure['layers'])
	check_compilation(structure['compilation'])

	model = built_model(structure['layers'])
	compile_model(model, structure['compilation'])
	return model
