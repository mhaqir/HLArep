#!/u/mhaghir/anaconda3/envs/tensorflow_env1/bin/python3


import sys
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns




if __name__ == '__main__':
	filename = sys.argv[1]
	pairs = []
	with open(filename) as f:
		lines = f.readlines()
	for line in lines:
		pairs.append(tuple(line.rstrip().split('\t')))


	lengths = [int(item[1]) - int(item[0]) for item in pairs]
	fig, ax = plt.subplots(nrows = 1, ncols = 1, figsize = (32, 32))
	n, bins, patches = ax.hist(lengths)
	fig.savefig( 'plots/{}.png'.format('3784_hist'))   
	plt.close(fig)


	sns.set()
	fig, ax = plt.subplots(nrows = 1, ncols = 1, figsize = (32, 32))
	sns.distplot(lengths, ax = ax)   # , bins = np.arange(0, 40000, 2000), norm_hist = True , bins = 100
	plt.xlim(0, 600000)
	# plt.xticks(np.arange(0, 40000, 2000))
	fig.savefig( 'plots/{}.png'.format('3784_dist')) 
	plt.close(fig)