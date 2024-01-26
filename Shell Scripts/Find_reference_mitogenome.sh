#!/bin/bash

#$ -l h_rt=12:00:00
#$ -l rmem=10G
#$ -pe smp 1
#$ -P ressexcon
#$ -q ressexcon.q


/usr/local/extras/Genomics/apps/anaconda_python/envs/mamba/bin/conda init bash

source ~/.bashrc

source activate py39

# Downloads most closely-related mitogenome based on species NCBI taxonomy into outfolder
python /usr/local/extras/Genomics/apps/MitoHiFi/findMitoReference.py --species "Teleopsis dalmanni" --email smparkus1@sheffield.ac.uk --outfolder /fastdata/bop22smp/sylvie/mitogenome --min_length 16000
