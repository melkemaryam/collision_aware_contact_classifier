# Usage

# normal: python3 main.py --model ../output/neural_net.model --dataset ../data --predictions ../predictions --train none
# random search: python3 main.py --model ../output/random_search.model --optimiser random --inner_optimiser adam --dataset ../data --predictions ../predictions --train all
# hyperband: python3 main.py --model ../output/hyperband.model --optimiser hyperband --inner_optimiser adam --dataset ../data --predictions ../predictions --train all
# bayesian: python3 main.py --model ../output/bayesian.model --optimiser bayesian --inner_optimiser adam --dataset ../data --predictions ../predictions --train all

# just predict: python3 main.py

from arguments import Args
from build_model import Build_model
from tuning import Tuning
from training import Training
from read_data import Read_data
from preprocessing import Preprocessing
from predicting import Predicting
from inner_opt import Inner_opt
from helper import Helper
from evaluating import Evaluating

import os

if __name__ == '__main__':
	try:
		
		# create objects of all classes
		bu = Build_model(None)
		tu = Tuning(None)
		tr = Training()
		re = Read_data()
		prep = Preprocessing(None, None, None, None, None, None, None)
		pred = Predicting()
		ino = Inner_opt()
		he = Helper()
		ev = Evaluating()
		a = Args()
		args = a.parse_arguments()
		
		# set condition value
		cond = 0

		# check if .h5 file was provided
		path_pred = args["predictions"]
		if os.path.isfile(path_pred):

			file_extension = os.path.splitext(path_pred)[1]
			# check if it is a h5 file
			if file_extension.lower() == ".h5":
				cond = 1
				joint, start, end = he.get_robot_data()
		
		# predict images only with newly generated images
		if(args["train"] == 'pred' and cond == 1):
			pred.prediction_process(joint=joint, start=start, end=end)

		# predict images only with privided folder
		elif(args["train"] == 'pred' and cond == 0):
			pred.prediction_process()

		# train, test, optimise, and predict with generating images
		elif((args["train"] == "all" or args["train"] == "one" or args["train"] == "none") and cond == 1):
			prep.prepare_data()
			ev.evaluate()
			pred.prediction_process(joint=joint, start=start, end=end)

		# train, test, optimise, and predict with provided images
		elif((args["train"] == "all" or args["train"] == "one" or args["train"] == "none") and cond == 0):
			prep.prepare_data()
			ev.evaluate()
			pred.prediction_process()

	except KeyboardInterrupt:
		pass















