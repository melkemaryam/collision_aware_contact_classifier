# import packages
import argparse
from arguments import Args

import matplotlib.pyplot as plot
import numpy as np
import h5py
import pandas as pd
import os
import glob

class Read_data():

	# create new folder: full_spectrograms/log_/alfred.telemetry/tau_ext/17/datetime
	#full_spec_path = os.makedirs('full_spectrograms/' + log + '/' + folder + '/' + topic + '/' + str(joint) + '/' + datetime.now().strftime("%Y%m%d-%H%M%S"))
	#raw_spec_path = os.makedirs('raw_spectrograms/' + log + '/' + folder + '/' + topic + '/' + str(joint) + '/' + datetime.now().strftime("%Y%m%d-%H%M%S"))
			
	def check_path(self):
		
		# create the folder
		if not os.path.exists('Predict'):
			os.makedirs('Predict')

		# empty Predict directory, so only new data is shown
		files = glob.glob('Predict/*')
		for f in files:
			os.remove(f)


	def sliding_window(self, joint, start, end):

		# check the correct path
		self.check_path()

		# create objects of class
		arg = Args()
		args = arg.parse_arguments()

		# Read the h5 file
		hf_path = args["predictions"]
		hf = pd.HDFStore(hf_path)

		# initialise robot details
		topic = 'tau_ext'
		folder = 'alfred.telemetry'
		log = os.path.splitext(os.path.basename(hf_path))[0]

		# initialise important parameters
		samplingFrequency = 1000
		window_len = 100
		stride = 1
		overlap = window_len * 0.5

		for i in range(start,end,stride):

			# slide window from start to end
			signalData = hf[folder][topic][joint][int((i - overlap)):int((i - overlap + window_len))]

			self.plot_full_spec(signalData, samplingFrequency, topic, joint, i, full_spec_path)
			self.plot_raw_spec(signalData, samplingFrequency, topic, joint, i, full_spec_path)

	def create_predict_images(self, joint, start, end):

		# check the correct path
		self.check_path()
		
		# create objects of class
		arg = Args()
		args = arg.parse_arguments()

		# Read the h5 file
		hf_path = args["predictions"]
		hf = pd.HDFStore(hf_path)

		# initialise robot details
		topic = 'tau_ext'
		folder = 'alfred.telemetry'
		log = os.path.splitext(os.path.basename(hf_path))[0]

		# initialise important parameters
		samplingFrequency = 1000
		window_len = 100
		stride = 1
		overlap = window_len * 0.5

		# slide the window from start to end with stride
		for i in range(start,end,stride):

			# slide window
			signalData = hf[folder][topic][joint][int((i - overlap)):int((i - overlap + window_len))]

			# create spectrogram
			self.plot_raw_spec(signalData, samplingFrequency, topic, joint, i, 'Predict')


	def plot_full_spec(self, signalData, samplingFrequency, topic, joint, i, full_spec_path):

		# close previous plot
		plot.close()

		# first subplot with Amplitude
		plot.subplot(211)
		plot.title('Spectrogram of ' + topic + '_' + str(joint) + ' Window ' + str(i))
		plot.plot(signalData)
		plot.xlabel('Time')
		plot.ylabel('Amplitude')

		# second subplot with spectrogram
		plot.subplot(212)
		spectrum, freqs, t, im = plot.specgram(signalData,Fs=samplingFrequency)
		plot.xlabel('Time')
		plot.ylabel('Frequency')
		plot.tight_layout()

		plot.savefig(full_spec_path + '/window_' + topic + '_' + str(joint) + '_plot_' + str(i))


	def plot_raw_spec(self, signalData, samplingFrequency, topic, joint, i, raw_spec_path):

		# close previous plot
		plot.close()

		# create spectrogram plot
		plot.specgram(signalData,Fs=samplingFrequency)
		plot.tight_layout()
		plot.axis('off')

		plot.savefig(raw_spec_path + '/window_' + topic + '_' + str(joint) + '_spec_' + str(i), bbox_inches='tight',transparent=True, pad_inches=0)

