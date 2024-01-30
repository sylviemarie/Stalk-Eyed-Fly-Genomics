#!/usr/bin/python2.6
# -*- coding: utf-8 -*-

''' Prepare BLASTX
This script prepares sequences for blastx analysis of orthologous sequences.
Takes orthogroups and creates a folder for each. In each folder, a query fasta file
is made with each nucleotide sequence. A db fasta file is made with the protein sequence
of one of the species (ie the best annotated genome).
'''
# ==============================================================================
import argparse
import sys
import os
import pickle

# ==============================================================================
# Command line options==========================================================
# ==============================================================================
parser = argparse.ArgumentParser()
parser.add_argument("--db_proteome_focalspecies", "-p", type=str,
                    help="An Ensembl proteome")
parser.add_argument("--name_focalspecies", "-n", type=str,
                    help="Name of species with Ensembl proteome")
parser.add_argument("--orthogroups", "-o", type=str,
                    help="A pickle file containging validated and mapped orthogroups")
parser.add_argument("--ortho_seq_folder", "-f", type=str,
                    help="A folder containing sequence information for orthologs")
parser.add_argument("--outfolder", "-u", type=str,
                    help="A folder containing orthogroup blastx infolders")

# This checks if the user supplied any arguments. If not, help is printed.
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)
# Shorten the access to command line arguments.
args = parser.parse_args()


# ==============================================================================
# Functions=====================================================================
# ==============================================================================

def read_pkl(pkl_file):
    '''Reads in a pickled file and returns the stored object'''
    with open(pkl_file, "rb") as infile:
        return pickle.load(infile)


def list_folder(infolder):
    '''Returns a list of all files in a folder with the full path'''
    return [os.path.join(infolder, f) for f in os.listdir(infolder)]


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


def map_transcriptid_to_proteinid(proteome):
    ''' Read Ensembl fasta file and outputs a dictionary
    key [transcript id] values [protein id, sequence]
    '''
    tid_proteome = {}
    for p in proteome:
        seq = proteome[p][0]
        header = proteome[p][1]
        seq_tid = header.split()[4].split(":")[1]
        tid_proteome[seq_tid] = (p, seq)
    return tid_proteome


def read_seq_folder(seq_folder):
    seq_dict = {}
    for f in list_folder(seq_folder):
        if f.endswith("longest.fasta"):
            species = os.path.basename(f).split("_")[0]
            print
            species, f
            seq_dict[species] = read_fasta(f)
    return seq_dict


# ==============================================================================
# Main==========================================================================
# ==============================================================================m

def main():
    # Read pickle file of orthogroups
    orthogroups = read_pkl(args.orthogroups)
    print('%i orthogroups detected!' % len(orthogroups[0]))
    print('Starting to create input folders...')
    for o in orthogroups:
        print(o)
    # Get sequences of protein for focal species
    proteome = read_fasta(args.db_proteome_focalspecies)
    tid_proteome = map_transcriptid_to_proteinid(proteome)
    print('Number of protein db sequences  =', len(proteome), len(tid_proteome))

    # Get sequences of isoforms for each species
    isoform_seqs = read_seq_folder(args.ortho_seq_folder)
    print('Number of orthogroup sequences  =', len(isoform_seqs))
    for isoform in isoform_seqs:
        print(isoform)

    os.chdir(args.outfolder)
    pseudogenes = 0
    check = {}  # Initialize the check dictionary
    for i in orthogroups:
        # Get focal species
        focal_species = args.name_focalspecies
        
        group = i
        print(group)
        orthogroup_name = None
        for g in group:
            # Find the orthogroup name for the focal species
            if g.split("_")[0] == focal_species:
                orthogroup_name = g
            else:
                orthogroup_name = None

            if orthogroup_name:
                db_id = orthogroup_name.split("_")[1]

                # Make a new folder for each orthogroup [named after focal species]
                if not os.path.exists(orthogroup_name):
                    os.makedirs(orthogroup_name)

                # Write protein to db fasta
                db_outfile_path = os.path.join(orthogroup_name, db_id + "_DB.fasta")
                with open(db_outfile_path, "w") as db_outfile:
                    header = ">" + db_id + " " + tid_proteome[db_id][0] + "\n"
                    db_outfile.write(header)
                    db_outfile.write("%s\n" % tid_proteome[db_id][1])

                # Write orthogroup sequences to query fasta
                query_outfile_path = os.path.join(orthogroup_name, db_id + "_QUERY.fasta")
                with open(query_outfile_path, "w") as query_outfile:
                    for o in group:
                        species = o.split("_")[0]
                        isoform_id = o.split(species + "_")[1]
                        header = ">" + o + "\n"
                        query_outfile.write(header)
                        query_outfile.write("%s\n" % isoform_seqs[species][isoform_id][0])
                        if species not in check:
                            check[species] = 0
            else:
                pseudogenes += 1



if __name__ == '__main__':
    main()
