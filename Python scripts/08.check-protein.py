#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-
#
''' Checks VALID PROTEIN SEQUENCES
This script takes each orthogroup and checks that each species with an 
Ensembl protein file has a protein fasta sequence.
'''
#==============================================================================
import argparse
import sys
import os
import cPickle as pickle
from Bio.Seq import Seq
#==============================================================================
#Command line options==========================================================
#==============================================================================
parser = argparse.ArgumentParser()
parser.add_argument("infolder", type=str,
                    help="An input folder containing folders of sequences of orthogroups")
parser.add_argument("invalid_folder", type=str,
                    help="An output folder for invalid orthogroups")
parser.add_argument("protein", type=str,
                    help="")
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
            if f.endswith(".fa"):
                file_list.append(f)
    return file_list

def read_fasta_cdna(source):
    ''' Read Ensembl fasta file and outputs a dictionary 
    key [transcript name] values [sequence] [header]
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

def read_fasta_protein(source):
    ''' Read Ensembl fasta file and outputs a dictionary 
    key [protein name] values [sequence] [header]
    '''
    SG = {}
    try:
        with open(source, "r") as file:
            for line in file.readlines():
                if line[0] == ">":
                    name = line[1:].rstrip().split()[0]
                    transcript_id = line[1:].split("transcript:")[1].split(" ")[0]
                    header = line[1:].rstrip()
                    SG[transcript_id] = ["", header]
                else:
                    SG[transcript_id][0] += line.rstrip()
            return SG
    except IOError:
        print "File does not exit!"

#==============================================================================
#Main==========================================================================
#==============================================================================m
def main():
    invalid_proteins = []
    keep = 0
    remove =0
    protein_dict = {}
    species_list = []

    for protein in list_files(args.protein):
        print protein
        if protein.endswith("pep.all.fa"):
            prot_name = os.path.basename(protein).split(".")[0]
            prot_fasta = read_fasta_protein(protein)
            protein_dict[prot_name] = prot_fasta
            species_list.append(prot_name)
    print species_list

    for orthogroup in list_folder(args.infolder):
        for f in list_files(orthogroup):
            if f.endswith("cdna.fa"):
                count =0
                fasta = read_fasta_cdna(f)
                for s in fasta:
                    species = s.split("_")[0]
                    if species in species_list:
                        name_id = s.split("_")[1].rstrip()
                        if name_id in protein_dict[species]:
                            count +=1
                if count == len(list_files(args.protein)):
                    keep +=1
                else:
                    remove += 1
                    invalid_proteins.append(orthogroup)
                    
    print "Number of orthogroups all with Ensembl proteins =", keep
    print "Number of invalid orthogroups =", remove
    if not os.path.isdir(args.invalid_folder): os.mkdir(args.invalid_folder)
    for o in list(set(invalid_proteins)):
        import shutil
        shutil.move(o, args.invalid_folder)

if __name__ == '__main__':
    main()
