# import packages
import argparse
from arguments import Args

from datetime import datetime

from sklearn.metrics import classification_report
from sklearn.metrics import f1_score

import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.callbacks import TensorBoard
from tensorflow.keras.losses import MSE

from preprocessing import Preprocessing
from helper import Helper
from build_model import Build_model
from tuning import Tuning

class Training():


	def train(self):

		# create objects of classes
		p = Preprocessing(None, None, None, None, None, None, None)
		h = Helper()
		b = Build_model(None)
		t = Tuning(None)

		# get values
		train_X = p.get_train_x()
		train_Y = p.get_train_y()
		test_X = p.get_test_x()
		test_Y = p.get_test_y()
		weight = p.get_weight()
		best_hyperparameters = t.get_best_parameters()

		arg = Args()
		args = arg.parse_arguments()

		# train the network
		print("[INFO] training network...")

		# create logs for Tensorboard
		log_dir = "../logs/fit/" + datetime.now().strftime("%Y%m%d-%H%M%S")
		tensorboard = TensorBoard(log_dir=log_dir, histogram_freq=1)

		# create Early Stopping
		callback = EarlyStopping(monitor='loss', patience=3)

		# get the correct model
		if (args["train"] == 'all' or args["train"] == 'one'):
			tuner = t.return_tuner()
			model = tuner.hypermodel.build(best_hyperparameters)
		elif (args["train"] == 'none' or args["train"] == 'pred'):
			model = b.build_net()

		# train the model
		trained_model = model.fit(
			validation_data=(test_X, test_Y),
			epochs=200, 
			callbacks=[callback, tensorboard],
			class_weight=weight,
			verbose=1)

		# save the network to disk
		print("[INFO] serializing network to '{}'...".format(args["model"]))
		model.save(args["model"])

		return model
