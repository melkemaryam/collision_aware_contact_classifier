# import packages
import argparse
from arguments import Args

import cv2
import imutils
from imutils import paths
import numpy as np
import os
import random

import tensorflow as tf
from tensorflow.keras.models import load_model
from helper import Helper
from preprocessing import Preprocessing
from read_data import Read_data


class Predicting():

	def load_net(self):

		# create objects of classes
		arg = Args()
		args = arg.parse_arguments()

		# load the trained model
		print("[INFO] loading model...")
		model = load_model(args["model"])

		return model


	def prediction_process(self, **data):

		# create objects of classes
		arg = Args()
		args = arg.parse_arguments()
		h = Helper()
		r = Read_data()
		p = Preprocessing(None, None, None, None, None, None, None)

		# grab the paths to the input images, shuffle them, and grab a sample
		print("[INFO] predicting...")

		# get labels
		image_names = h.get_image_names()
		
		# get path
		path_pred = args["predictions"]

		# check if path is only folder
		if os.path.isdir(path_pred):  
			print("\n predicting images from directory")

		# check if path ends with h5 file
		elif os.path.isfile(path_pred):

			file_extension = os.path.splitext(path_pred)[1]
			if file_extension.lower() == ".h5":
				# generate new images
				print("\n generating new prediction images, this might take a while")
				r.create_predict_images(data["joint"], data["start"], data["end"])
				path_pred = "Predict"
			else:
				# print error message
				print("\n Please provide a .h5 to generate new images")
				path_pred = "../data/Predict"

		# get paths
		paths_to_image = list(paths.list_images(path_pred))
		random.shuffle(paths_to_image)

		model = self.load_net()

		# loop over the image paths
		for (i, path_to_image) in enumerate(paths_to_image):

			# perform CLAHE
			image = p.clahe(path_to_image)

			# preprocess the image by scaling it to the range [0, 1]
			image = image.astype("float32") / 255.0
			image = np.expand_dims(image, axis=0)

			# make predictions using the CNN
			predictions = model.predict(image)
			j = predictions.argmax(axis=1)[0]
			label = image_names[j]

			# load the image using OpenCV, resize it, and draw the label
			image = cv2.imread(path_to_image)
			image = imutils.resize(image, width=128)
			cv2.putText(image, label, (5, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

			# save the image to disk
			pr = os.path.sep.join(["Predict", "{}.png".format(i)])

			cv2.imwrite(pr, image)
