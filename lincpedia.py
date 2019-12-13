#!/u/mhaghir/anaconda3/envs/tensorflow_env1/bin/python3

import sys
from itertools import groupby
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def fastaReader(filename):
	f = open(filename, 'r')
	hdrs = (h[1] for h in groupby(f, lambda line: line[0] == '>'))
	for hdr in hdrs:
		hdrStr = hdr.__next__()[1:].strip()
		seq = ''.join(s.strip() for s in hdrs.__next__())
		yield hdrStr, seq




if __name__ == '__main__':
	filename = sys.argv[1]
	r = fastaReader(filename)
	lnc_seqs = [item[1] for item in r]
	lnc_seqs_lngths = [len(item) for item in lnc_seqs]

	# fig, ax = plt.subplots(nrows = 1, ncols = 1, figsize = (32, 32))
	# n, bins, patches = ax.hist(lnc_seqs_lngths)
	# fig.savefig( 'plots/{}.png'.format('lincpedia_hist'))   
	# plt.close(fig)

	sns.set()
	fig, ax = plt.subplots(nrows = 1, ncols = 1, figsize = (32, 32))
	sns.distplot(lnc_seqs_lngths, ax = ax, bins = 100)   # , bins = np.arange(0, 40000, 2000), norm_hist = True
	plt.xlim(0, 40000)
	# plt.xticks(np.arange(0, 40000, 2000))
	fig.savefig( 'plots/{}.png'.format('lincpedia_dist')) 
	plt.close(fig)	





