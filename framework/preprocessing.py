# import packages
import argparse
from arguments import Args
import imutils
from imutils import paths
import numpy as np
import os
import random
from skimage import transform
from skimage import exposure
from skimage import io

class Preprocessing():

	def __init__(self, train_X, train_Y, test_X, test_Y, num_images, total_images_class, total_weight_class):

		self.train_X = train_X
		self.train_Y = train_Y
		self.test_X = test_X
		self.test_Y = test_Y
		self.num_images = num_images
		self.total_weight_class = total_weight_class
		self.total_images_class = total_images_class

	# function to load and prepare necessary data
	# parameters: pwd, path_to_csv
	# returns: array of data and labels
	def load_images(self, pwd, path_to_csv):

		labels = []
		data = []

		# load data
		rows = open(path_to_csv).read().strip().split("\n")[1:]
		random.shuffle(rows)

		# loop over the rows of the CSV file
		for (i, row) in enumerate(rows):
			
			# print status update
			if i > 0 and i % 2000 == 0:
				print("[INFO] processed {} total images".format(i))

			# get classId and path to image
			(label, path_to_image) = row.strip().split(";")[-2:]

			# create full path to image
			path_to_image = os.path.sep.join([pwd, path_to_image])
			image = self.clahe(path_to_image)

			# update the list of data and labels
			data.append(image)
			labels.append(int(label))

		# convert the data and labels to NumPy arrays
		data = np.array(data)
		labels = np.array(labels)

		# return a tuple of the data and labels
		return (data, labels)

	# function to prepare data
	# parameters: pwd, path_to_csv
	# returns: array of data and labels
	def prepare_data(self):

		arg = Args()
		args = arg.parse_arguments()

		# derive the path to the training and testing CSV files
		path_to_train = os.path.sep.join([args["dataset"], "Train.csv"])
		path_to_test = os.path.sep.join([args["dataset"], "Test.csv"])

		# load the training and testing data
		print("[INFO] loading training and testing data...")
		(self.train_X, self.train_Y) = self.load_images(args["dataset"], path_to_train)
		(self.test_X, self.test_Y) = self.load_images(args["dataset"], path_to_test)

		# scale data to the range of [0, 1]
		self.train_X = self.train_X.astype("float32") / 255.0
		self.test_X = self.test_X.astype("float32") / 255.0

		# one-hot encode the training and testing labels
		self.num_images = len(np.unique(self.train_Y))
		self.train_Y = to_categorical(self.train_Y, self.num_images)
		self.test_Y = to_categorical(self.test_Y, self.num_images)

		# calculate the total number of images in each class and
		# initialize a dictionary to store the class weights
		self.total_images_class = self.train_Y.sum(axis=0)
		self.total_weight_class = dict()

		# loop over all classes and calculate the class weight
		for i in range(0, len(self.total_images_class)):
			self.total_weight_class[i] = self.total_images_class.max() / self.total_images_class[i]


	# function to perform CLAHE
	# parameters: path_to_image
	# returns: modified image
	def clahe(self, path_to_image):

		image = io.imread(path_to_image)

		# resize the image and perform CLAHE
		image = transform.resize(image, (32, 32))
		image = exposure.equalize_adapthist(image, clip_limit=0.1)

		return image

	# GET METHODS

	def get_train_x(self):
		return self.train_X

	def get_train_y(self):
		return self.train_Y

	def get_test_x(self):
		return self.test_X

	def get_test_y(self):
		return self.test_Y

	def get_weight(self):
		return self.total_weight_class




