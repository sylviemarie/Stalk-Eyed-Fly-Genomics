#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-
#
''' Checks Ns IN ALIGNMENT are in multiples of 3
This script checks that Ns are present in codons. Therefore, Ns can be removed in 
15.remove-N.py without affecting the translation of the ORF.
'''
#==============================================================================
import argparse
import sys
import os
from Bio.Seq import Seq
#==============================================================================
#Command line options==========================================================
#==============================================================================
parser = argparse.ArgumentParser()
parser.add_argument("infolder", type=str,
                    help="An input folder containing folders of sequences of orthogroups")
parser.add_argument("species", type=str,
                    help="List of species names eg Poeciliareticulata,Poeciliaformosa,Xiphophorusmaculatus ")
# This checks if the user supplied any arguments. If not, help is printed.
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)
# Shorten the access to command line arguments.
args = parser.parse_args()
#==============================================================================
#Functions=====================================================================
#==============================================================================
def list_folder(infolder):
    '''Returns a list of all files in a folder with the full path'''
    return [os.path.join(infolder, f) for f in os.listdir(infolder) if not f.endswith(".DS_Store")]

def list_files(current_dir):
    file_list = []
    for path, subdirs, files in os.walk(current_dir): # Walk directory tree
        for name in files:
            if not name.endswith(".DS_Store"):
                if name.endswith("_masked.phy"):
                    f = os.path.join(path, name)
                    file_list.append(f)
    return file_list

def read_phylip(source, species):
    ''' Read Ensembl phylip file and outputs a dictionary 
    key [seq name] values [sequence] [header]
    '''
    species = species.split(",")
    SG = {}
    try:
        with open(source, "r") as file:
            for line in file.readlines():
                line = line.rstrip()
                if not line.startswith(" "):
                    if line in species:
                        name = line
                        header = line
                        SG[name] = ["", header]
                    else:
                        SG[name][0] += line
            return SG
    except IOError:
        print "File does not exit!"

#==============================================================================
#Main==========================================================================
#==============================================================================m
def main():
    ammend = 0
    invalid_orthogroups = []
    for orthogroup in list_folder(args.infolder):
        for aln in list_files(orthogroup):
            ammend = ammend+1
            final_remove = {}
            phylip = read_phylip(aln, args.species)
            for s in phylip:
            	triplets = [phylip[s][0][i:i +3] for i in range(0, len(phylip[s][0]), 3)]
            	for codon in triplets:
            		if codon.count("N") != 0:
            			if codon.count("N") != 3:
            				print "ERROR - Ns not in multiple of 3"

if __name__ == '__main__':
    main()
