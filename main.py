#!/u/mhaghir/anaconda3/envs/tensorflow_env1/bin/python3


import sys
# from collections import Counter, OrderedDict
# from operator import itemgetter
import numpy as 
import matplotlib.pyplot as plot



THRESHOLD = 5

def readBedFile(filename):
	bed = []
	with open(filename, 'r') as f:
		for line in f:
			bed.append(line.strip().split())
	return bed

def repetitionFinder(pos_list):
	cnt = 0
	for i in range(1, len(pos_list)):
		if pos_list[i-1] == pos_list[i]:
			cnt += 1
		else:
			if cnt >= THRESHOLD:
				return pos_list[i - 1], cnt
			cnt = 0
	return None

def pairFinder(pos_list1, pos_list2, chrom):
	pairs = []
	while (len(pos_list1) > 0) and (repetitionFinder(pos_list1)) and (repetitionFinder(pos_list2)):
		r1, cnt1 = repetitionFinder(pos_list1)
		# p1 = np.where(pos_list1 == r1)
		p1 = pos_list1.index(r1)
		# print(p1)
		r2, cnt2 = repetitionFinder(pos_list2)
		# p2 = np.where(pos_list2 == r2)
		p2 = pos_list2.index(r2)
		if (pos_list2[p2] > pos_list1[p1]) and (chrom[p2] == chrom[p1]):
			pairs.append((pos_list1[p1], pos_list2[p2]))
		pos_list1 = pos_list1[p1 + cnt1:]
		pos_list2 = pos_list2[p2 + cnt2:]
	return pairs

if __name__ == '__main__':
	filename = sys.argv[1]

	bed = readBedFile(filename)
	pos1 = [int(item[1]) for item in bed]
	pos2 = [int(item[2]) for item in bed]
	chrom = [item[0] for item in bed]
	print(pos1[0:10])
	print(pos2[0:10])
	print(chrom[0:10])
	r = repetitionFinder(pos1)
	print(r)
	pairs = pairFinder(pos1, pos2, chrom)
	print(pairs[0:10])
	lengths = [item[1] - item[0] for item in pairs]
	fig, ax = plt.subplots(nrows = 1, ncols = 1, figsize = (32, 32))
	n, bins, patches = ax.hist(lengths)
	fig.savefig( 'plots/{}.png'.format(filename))   
	plt.close(fig)


	# for k, v in r.items():
	# 	print(k, v)
	# print(r[0:5])
	# print(type(r))