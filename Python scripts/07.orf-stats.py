#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-
#
''' Get STATS
This script calculates basic statistics about the length and number of open reading frames.
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
parser.add_argument("lengththreshold", type=str,
                    help="Length of protein")
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
    return [os.path.join(infolder, f) for f in os.listdir(infolder)]

def list_files(current_dir):
    file_list = []
    for path, subdirs, files in os.walk(current_dir): # Walk directory tree
        for name in files:
            f = os.path.join(path, name)
            file_list.append(f)
    return file_list

def read_fasta(source):
    ''' Read Ensembl fasta file and outputs a dictionary 
    key [seq name] values [sequence] [header]
    '''
    SG = {}
    try:
        with open(source, "r") as file:
            for line in file.readlines():
                if line[0] == ">":
                    name = line[1:].rstrip().split()[0]
                    header = line[1:].rstrip()
                    SG[name] = ["", header]
                else:
                    SG[name][0] += line.rstrip()
            return SG
    except IOError:
        print "File does not exit!"

#==============================================================================
#Main==========================================================================
#==============================================================================m
def main():
    protein_length = []
    small_groups = []
    count = 0
    for orthogroup in list_folder(args.infolder):
        for f in list_files(orthogroup):
            if f.endswith("pep.fa"):
                fasta = read_fasta(f)
                for s in fasta:
                    protein_length.append(len(fasta[s][0]))
                    if len(fasta[s][0]) < float(args.lengththreshold):
                        count += 1
                        small_groups.append(orthogroup)
    print "Number of protein sequences shorter than", args.lengththreshold, ": ", count
    print sum(protein_length)/ float(len(protein_length))
    print min(protein_length)
    print max(protein_length)
    print len(set(small_groups))
    # for p in set(small_groups):
    #     print p
        
if __name__ == '__main__':
    main()
