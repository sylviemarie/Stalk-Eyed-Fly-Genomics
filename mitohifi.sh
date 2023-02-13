#!/bin/bash

#$ -l h_rt=12:00:00

#$ -l rmem=25G

#$ -pe smp 1

#$ -P ressexcon
#$ -q ressexcon.q

#$ -wd /fastdata/bop22smp/sylvie/mitogenome/wdir

source /usr/local/extras/Genomics/.bashrc

/usr/local/extras/Genomics/apps/anaconda_python/envs/mamba/bin/conda init bash

source ~/.bashrc

source activate /usr/local/extras/Genomics/apps/anaconda_python/envs/mamba/envs/py39

python /usr/local/extras/Genomics/bin/mitohifi.py -r /fastdata/bop22smp/mitogenome/reads_ref/merged.fasta -f /fastdata/bop22smp/mitogenome/reads_ref/NC_065368.1.fasta -g /fastdata/bop22smp/mitogenome/reads_ref/NC_065368.1.gb -t 1 -o 5
