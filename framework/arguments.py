import argparse


class Args():


	def parse_arguments(self):
		# create argument parser
		ap = argparse.ArgumentParser()
		ap.add_argument("-m", "--model", default='../output/hyperband.model', required=False, help="path to model")
		ap.add_argument("-op", "--optimiser", default=None, choices=['bayesian', 'hyperband', 'random'], required=False, help="optimisation method for classifier")
		ap.add_argument("-inop", "--inner_optimiser", default='adam', choices=['adam', 'sgd', 'rms'], required=False, help="inner optimisation method for classifier")
		ap.add_argument("-d", "--dataset", default='../data', required=False, help="path to input data")
		ap.add_argument("-pr", "--predictions", default='Predict',required=False, help="path to the directory with images to predict or path to file to create new images")
		ap.add_argument("-tr", "--train", default='pred', choices=['all', 'one', 'none', 'pred'], required=False, help="give info on how many parameters to optimise, 'pred' = no training")		
		args = vars(ap.parse_args())

		return args


'''

argument scenarios:

--train:
	train == all: build_net_opt + optimise_inner opt
	train == one: build_net + optimise_inner opt
	train == none: build_net + direct_inner opt
	train == pred: load model + direct_inner opt

'''