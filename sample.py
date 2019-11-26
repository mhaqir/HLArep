#!/u/mhaghir/anaconda3/envs/tensorflow_env1/bin/python3


from lincpedia import fastaReader
import sys




if __name__ == '__main__':
	filename = sys.argv[1]
	r = fastaReader(filename)
	chrs_seq = [item[1] for item in r]
	chrs_seq_lngths = [len(item) for item in chrs_seq]
	print(chrs_seq_lngths)
	print(sum(chrs_seq_lngths))



