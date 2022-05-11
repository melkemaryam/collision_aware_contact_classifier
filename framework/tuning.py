# import packages
import argparse
from arguments import Args

import kerastuner
from kerastuner.tuners import RandomSearch, Hyperband, BayesianOptimization

from sklearn.metrics import classification_report
from sklearn.metrics import f1_score
import tensorflow as tf

from helper import Helper
from preprocessing import Preprocessing
from build_model import Build_model


class Tuning():

	def __init__(self, best_hyperparameters):
		self.best_hyperparameters = best_hyperparameters

	def get_best_parameters(self):
		return self.best_hyperparameters

	def return_tuner(self):

		# create objects of class
		arg = Args()
		args = arg.parse_arguments()

		# return the correct tuner
		if (args["optimiser"] == 'bayesian'):
			return self.tuning_bayesian
		elif (args["optimiser"] == 'hyperband'):
			return self.tuning_hyperband
		elif (args["optimiser"] == 'random'):
			return self.tuning_random_search

	def search_tuner(self, tuner):

		# create objects of class
		p = Preprocessing(None, None, None, None, None, None, None)
		
		# get values
		train_X = p.get_train_x()
		train_Y = p.get_train_y()
		test_X = p.get_test_x()
		test_Y = p.get_test_y()

		# tune the hyperparameters
		tuner.search(train_X, train_Y,
			epochs=20,
			validation_data=(test_X, test_Y))

	def tuner_info(self, tuner):

		# create objects of class
		h = Helper()

		# get best parameters
		self.best_hyperparameters = tuner.get_best_hyperparameters(1)[0]
		print(self.best_hyperparameters.values)
		h.write_report(self.best_hyperparameters.values)

		for data in tuner.get_best_hyperparameters(1):
			print(data.values)
			h.write_report(data.values)

		n_best_models = tuner.get_best_models(num_models=1)
		print(n_best_models[0].summary())

	def tuning_random_search(self):
		
		# create objects of class
		b = Build_model(None)

		# optimise with Random Search
		tuner = RandomSearch(
			b.return_model,
			objective='accuracy',
			max_trials=10,
			executions_per_trial=1,
			directory='randoms_data') #change the directory name here  when rerunning the cell else it gives "Oracle exit error" 

		self.search_tuner(tuner)
		self.tuner_info(tuner)

		return tuner


	def tuning_hyperband(self):
		
		# create objects of class
		b = Build_model(None)

		# optimise with Hyperband
		tuner = Hyperband(
			b.return_model,
			objective='accuracy',
			max_epochs=10,
			hyperband_iterations=1,
			directory='hyperband_data') #change the directory name here  when rerunning the cell else it gives "Oracle exit error" 

		self.search_tuner()
		self.tuner_info(tuner)

		return tuner


	def tuning_bayesian(self):

		# create objects of class
		b = Build_model(None)
		
		# optimise with Bayesian Optimisation
		tuner = BayesianOptimization(
			b.return_model,
			objective='accuracy',
			max_trials=10,
			executions_per_trial=1,
			directory='bayesian_data') #change the directory name here  when rerunning the cell else it gives "Oracle exit error" 

		self.search_tuner(tuner)
		self.tuner_info(tuner)

		return tuner
