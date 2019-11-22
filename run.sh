#!/bin/bash

module unload python/2.7.16
module load python/3.6.8
cd /N/u/mhaghir/Carbonate/HLArep


python main.py /N/slate/mhaghir/HLArep/3784_dedup-lncipedia-intersect_sep19.sorted.bed
