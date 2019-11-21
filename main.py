#!/u/mhaghir/anaconda3/envs/tensorflow_env1/bin/python3


import sys


def readBedFile(filename):
	bed = []
	with open(filename, 'r') as f:
		for line in f:
			bed.append(line.strip().split())
	return bed


if __name__ == '__main__':
	filename = sys.argv[1]

	bed = readBedFile(filename)
	pos1 = [int(item[1]) for item in bed]
	pos2 = [int(item[2]) for item in bed]
	print(pos1[0:10])
	print(pos2[0:10])