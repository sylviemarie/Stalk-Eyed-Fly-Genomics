#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
#
''' Checks LENGTH OF GAPS IN ALIGNMENT
This script calculates the alignment length after removing gaps in the alignment.
It reports how many alignments fail the cutoff threshold specified.
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
parser.add_argument("-i", "--infolder", type=str,
                    help="An input folder containing folders of sequences of orthogroups")
parser.add_argument("-c", "--cutoff", type=str,
                    help="cutoff in bp")
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
                if name.endswith("prank.best.fas"):
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
        print('File does not exit!')

#==============================================================================
#Main==========================================================================
#==============================================================================m
def main():
    ammend = 0
    count = 0
    files = 0
    for orthogroup in list_folder(args.infolder):
        files += 1
        for aln in list_files(orthogroup):
            ammend += 1
            check_length = []
            fasta = read_fasta(aln)
            sites_with_gaps = {}
            for s in fasta:
                check_length.append(len(fasta[s][0]))
                for i, p in enumerate(fasta[s][0]):
                    if p == "-":
                        sites_with_gaps[i] = 0
            final_length  = float(len(sites_with_gaps))
            original_length = float(len(fasta[s][0]))
            if original_length - final_length < int(args.cutoff):
                count +=1
            if len(set(check_length)) != 1:
                print('ERROR-PRANK sequence lengths differ')

    print('Number of original orthogroup =', files)
    print('Number of orthogroups under cutoff ',args.cutoff,"=",count)
    print('Number of orthogroups after length filtering =', files-count)
    print('Total number of orthogroups processed =', ammend)

if __name__ == '__main__':
    main()
