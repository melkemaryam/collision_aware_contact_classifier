# import packages
import argparse
from arguments import Args
import os

from sklearn.metrics import classification_report
from sklearn.metrics import f1_score

import tensorflow as tf
from tensorflow.keras.losses import MSE

from helper import Helper
from preprocessing import Preprocessing
from training import Training

class Evaluating():

	def evaluate(self):

		# create objects of class
		h = Helper()
		p = Preprocessing(None, None, None, None, None, None, None)
		t = Training()

		# get values
		test_X = p.get_test_x()
		test_Y = p.get_test_y()

		# evaluate the network
		print("[INFO] evaluating network...")
		model = t.train()

		# get labels
		image_names = h.get_image_names()

		# test model
		predictions = model.predict(test_X)
		report = classification_report(test_Y.argmax(axis=1), predictions.argmax(axis=1), target_names=image_names)

		print(report)
		h.write_report(report)

		_, acc = model.evaluate(test_X, test_Y, verbose=0)
		print('> %.3f' % (acc * 100.0))
		h.write_report('> %.3f' % (acc * 100.0))