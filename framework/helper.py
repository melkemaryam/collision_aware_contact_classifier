# import packages
import argparse
from arguments import Args
import os
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("Agg")

from datetime import datetime
import tensorflow as tf

from tensorflow.keras.preprocessing.image import ImageDataGenerator


class Helper():

	def get_image_names(self):
		
		# load sign names
		image_names = open("../labels.csv").read().strip().split("\n")[1:]
		image_names = [s.split(";")[1] for s in image_names]

		return image_names

	def get_robot_data(self):

		# collect data for 
		print("[USER INPUT] before we start, we need some details on the images.")
		print("[USER INPUT] The prediction images are taken from your .h5 file from alfred.telemetry/tau_ext.")
		joint = int(input("[USER INPUT] Which tau_ext joint do you want to use? Please enter a number between 0 and 43: \n"))
		start = int(input("[USER INPUT] At which millisecond do you want to start? i.e. 12678 \n"))
		end = int(input("[USER INPUT] At which millisecond do you want to end? i.e. 20000. Please make sure that this number is greater than the start number. \n"))

		if (end <= start):
			end = int(input("[USER INPUT] This number must be greater than the start number. Please try again.\n"))

		return joint, start, end

	def get_augmentation(self):
		
		# construct the image generator for data augmentation
		aug = ImageDataGenerator(
			rotation_range=10,
			zoom_range=0.15,
			width_shift_range=0.1,
			height_shift_range=0.1,
			shear_range=0.15,
			horizontal_flip=False,
			vertical_flip=False,
			fill_mode="nearest")

		return aug

	def write_report(self, report):

		# create report
		file = open("../reports/report_" + datetime.now().strftime("%Y%m%d-%H%M%S") + ".txt", "a")

		file.write(str(report))
		file.write("\n")
		file.close()

		print("[INFO] report written")