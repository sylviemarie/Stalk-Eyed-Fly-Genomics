#!/usr/bin/python2.6
# -*- coding: utf-8 -*-
#
''' Clean FOLDER
Removes all files in folder that do not end in string specified. 
'''
#==============================================================================
import argparse
import sys
import os
#==============================================================================
#Command line options==========================================================
#==============================================================================
parser = argparse.ArgumentParser()
parser.add_argument("infolder", type=str,
                    help="Infolder containing folders of orthogroups")
parser.add_argument("uniq", type=str,nargs="+",
                    help="Unique identifier(s) which file to keep ends with")
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
            f = os.path.join(path, name)
            file_list.append(f)
    return file_list
#==============================================================================
#Main==========================================================================
#==============================================================================m
def main():
    uniqids = []
    for uniq in args.uniq:
        uniqids.append(uniq)
    print "Keeping ...", uniqids

    count = 0 
    for orthogroup in list_folder(args.infolder):
        count += 1
        for f in list_files(orthogroup):
            keep = None
            for uniq in uniqids:
                if f.endswith(uniq):
                    keep = "Yes"
            if keep is None:
                os.remove(f)
    print "Number of folders modified =", count

if __name__ == '__main__':
    main()