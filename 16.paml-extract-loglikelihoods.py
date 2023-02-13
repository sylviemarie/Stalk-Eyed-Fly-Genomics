#!/usr/bin/python2.6
# -*- coding: utf-8 -*-
''' Get Likelihoods
This script takes the alternative and null model folders, extracts the log likelihoods  
and the difference -2DL = -2*(likelihood_null-likelihood_alternative)
'''
#==============================================================================
import argparse
import sys
import os
from collections import defaultdict
#==============================================================================
#Command line options==========================================================
#==============================================================================
parser = argparse.ArgumentParser()
parser.add_argument("infolder_null", type=str,
					help="Folder containing folders with paml output files. Null model"
					"eg branch-site model omega is fixed")
parser.add_argument("infolder_alternative", type=str,
					help="Folder containing folders with paml output files. Alternative model"
					"eg branch-site model omega is estimated")
parser.add_argument("outfile", type=str,
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
	return [os.path.join(infolder, f) for f in os.listdir(infolder) if not f.endswith(".DS_Store")]

def list_files(current_dir):
	file_list = []
	for path, subdirs, files in os.walk(current_dir): # Walk directory tree
		for name in files:
			if name.endswith(".txt"):
				f = os.path.join(path, name)
				file_list.append(f)
	return file_list

def read_paml_branch(source):
	''' PAML branch parser
	Reads a PAML output file and extracts the branch of interest.
	'''
	try:
		with open(source, "r") as infile:
			for line in infile:
				if line.startswith("lnL"):
					likelihood = float(line.split(" ")[-7])
		return likelihood
	except IOError:
		print "File %s does not exit!" (source)
		raise

#==============================================================================
#Main==========================================================================
#==============================================================================

def main():
	#get files
	infiles_alternative = list_folder(args.infolder_alternative)
	infiles_null = list_folder(args.infolder_null)
	print "Number of infolders =", len(infiles_alternative), len(infiles_null)

	#find pairs of files
	filename_dict = defaultdict(list)
	for infile in infiles_alternative:
		for inf in list_files(infile):
			geneKey = os.path.dirname(inf).split("/")[-1].split("_")[1]
			filename_dict[geneKey].append(inf)
	for infile in infiles_null:
		for inf in list_files(infile):
			geneKey = os.path.dirname(inf).split("/")[-1].split("_")[1]
			filename_dict[geneKey].append(inf)
	print "Number of pairs of PAML output =", len(filename_dict)

	#extract likelihoods
	count = 0
	with open(args.outfile, "w") as outfile:
		outfile.write("Gene, lnL0, lnL1, -2DL")
		outfile.write("\n")
		for gene in filename_dict:
			count += 1
			sys.stdout.write('%d\r' % (count))
			sys.stdout.flush()
			alternative = filename_dict[gene][0]
			null = filename_dict[gene][1]
			likelihood_alternative =read_paml_branch(alternative)
			likelihood_null =read_paml_branch(null)
			minustwoDL = -2*(likelihood_null-likelihood_alternative)
			outfile.write(gene)
			outfile.write(",")
			outfile.write(str(likelihood_null))
			outfile.write(",")
			outfile.write(str(likelihood_alternative))
			outfile.write(",")
			outfile.write(str(minustwoDL))
			outfile.write("\n")

	print "Number of files processed =", count

if __name__ == "__main__":
	main()