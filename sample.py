#!/u/mhaghir/anaconda3/envs/tensorflow_env1/bin/python3


from lincpedia import fastaReader
import sys
from random import sample
from Bio import SeqIO


if __name__ == '__main__':
	filename = sys.argv[1]
	r = fastaReader(filename)
	chrs_seq = [item[1] for item in r]
	chrs_seq_lngths = [len(item) for item in chrs_seq]
	dna_seq = ''.join(chrs_seq)

	starting_pos = [2000*i + x for i, x in enumerate(sorted(sample(range(int(len(dna_seq)/55000)), 50000)))]
	sequences = [dna_seq[item: item +  2000] for item in starting_pos]

	id_sequence = {}
	for i in range(1, len(sequences) + 1):
		id_sequence['sample{}'.format(i)] = sequences[i - 1]

	with open('sequences.txt', 'w') as f:
		for k,v in id_sequence.items():
			f.writelines(k + '\t' + v + '\n')

	SeqIO.convert('sequences.txt', 'tab', 'samples.fasta', 'fasta')




