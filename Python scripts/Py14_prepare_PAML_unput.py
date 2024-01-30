#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
''' Prepare PAML
This script prepares sequences for PAML.
Takes each folder of orthologous sequences and removes all files apart from phylip file.
'''
#==============================================================================
import argparse
import sys
import os
#==============================================================================
#Command line options==========================================================
#==============================================================================
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--infolder", type=str,
                    help="Infolder containing folders of orthogroups")
parser.add_argument("-t", "--tree", type=str,
                    help="path to tree for paml")
parser.add_argument("-m", "--model", type=str,
                    help="")
parser.add_argument("-n","--nssites", type=str,
                    help="")
parser.add_argument("-f","--fixomega", type=str,
                    help="")
parser.add_argument("-o","--omega", type=str,
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
            f = os.path.join(path, name)
            file_list.append(f)
    return file_list
#==============================================================================
#Main==========================================================================
#==============================================================================m
def main():
    count = 0
    for orthogroup in list_folder(args.infolder):
        for f in list_files(orthogroup):
            if not f.endswith(".phy"):
                os.remove(f)
            else:
                count +=1
                control_file = f[:-3]+"m"+args.model+"ns"+args.nssites+"w"+args.fixomega+args.omega+".ctl"
                seq = f
                out_file = f[:-3]+"m"+args.model+"ns"+args.nssites+"w"+args.fixomega+args.omega+".txt"

                try:
                    with open(control_file,"wb") as outfile:
                        outfile.write("      seqfile = ".encode() +seq.encode() + b" * sequence data filename"+ b"\n")
                        outfile.write("     treefile = ".encode() +args.tree.encode() + b"      * tree structure file name"+ b"\n")
                        outfile.write("      outfile = ".encode() +out_file.encode() + b"           * main result file name"+ b"\n")
                        outfile.write(b""+b"\n")
                        outfile.write("        noisy = 9  * 0,1,2,3,9: how much rubbish on the screen".encode()+b"\n")
                        outfile.write("      verbose = 1  * 0: concise; 1: detailed, 2: too much".encode()+b"\n")
                        outfile.write("      runmode = 0  * 0: user tree;  1: semi-automatic;  2: automatic".encode()+b"\n")
                        outfile.write("                   * 3: StepwiseAddition; (4,5):PerturbationNNI; -2: pairwise".encode()+b"\n")
                        outfile.write("".encode()+b"\n")
                        outfile.write("      seqtype = 1  * 1:codons; 2:AAs; 3:codons-->AAs".encode()+b"\n")
                        outfile.write("    CodonFreq = 2  * 0:1/61 each, 1:F1X4, 2:F3X4, 3:codon table".encode()+b"\n")
                        outfile.write("".encode()+b"\n")
                        outfile.write("*        ndata = 10".encode()+b"\n")
                        outfile.write("        clock = 0  * 0:no clock, 1:clock; 2:local clock; 3:CombinedAnalysis".encode()+b"\n")
                        outfile.write("       aaDist = 0  * 0:equal, +:geometric; -:linear, 1-6:G1974,Miyata,c,p,v,a".encode()+b"\n")
                        outfile.write("   aaRatefile = dat/jones.dat  * only used for aa seqs with model=empirical(_F)".encode()+b"\n")
                        outfile.write("                   * dayhoff.dat, jones.dat, wag.dat, mtmam.dat, or your own".encode()+b"\n")
                        outfile.write("".encode()+b"\n")
                        outfile.write("        model = ".encode()+args.model.encode()+b"\n")
                        outfile.write("                   * models for codons:".encode()+b"\n")
                        outfile.write("                       * 0:one, 1:b, 2:2 or more dN/dS ratios for branches".encode()+b"\n")
                        outfile.write("                   * models for AAs or codon-translated AAs:".encode()+b"\n")
                        outfile.write("                       * 0:poisson, 1:proportional, 2:Empirical, 3:Empirical+F".encode()+b"\n")
                        outfile.write("                       * 6:FromCodon, 7:AAClasses, 8:REVaa_0, 9:REVaa(nr=189)".encode()+b"\n")
                        outfile.write("".encode()+b"\n")
                        outfile.write("      NSsites = ".encode()+args.nssites.encode()+"  * 0:one w;1:neutral;2:selection; 3:discrete;4:freqs;".encode()+b"\n")
                        outfile.write("                   * 5:gamma;6:2gamma;7:beta;8:beta&w;9:beta&gamma;".encode()+b"\n")
                        outfile.write("                   * 10:beta&gamma+1; 11:beta&normal>1; 12:0&2normal>1;".encode()+b"\n")
                        outfile.write("                   * 13:3normal>0".encode()+b"\n")
                        outfile.write("".encode()+b"\n")
                        outfile.write("        icode = 4  * 0:universal code; 1:mammalian mt; 2-10:see below".encode()+b"\n")
                        outfile.write("        Mgene = 0".encode()+b"\n")
                        outfile.write("                   * codon: 0:rates, 1:separate; 2:diff pi, 3:diff kapa, 4:all diff".encode()+b"\n")
                        outfile.write("                   * AA: 0:rates, 1:separate".encode()+b"\n")
                        outfile.write("".encode()+b"\n")
                        outfile.write("    fix_kappa = 0  * 1: kappa fixed, 0: kappa to be estimated".encode()+b"\n")
                        outfile.write("        kappa = 2  * initial or fixed kappa".encode()+b"\n")
                        outfile.write("    fix_omega = ".encode()+args.fixomega.encode()+"  * 1: omega or omega_1 fixed, 0: estimate ".encode()+b"\n")
                        outfile.write("        omega = ".encode()+args.omega.encode()+" * initial or fixed omega, for codons or codon-based AAs".encode()+b"\n")
                        outfile.write("".encode()+b"\n")
                        outfile.write("    fix_alpha = 1  * 0: estimate gamma shape parameter; 1: fix it at alpha".encode()+b"\n")
                        outfile.write("        alpha = 0. * initial or fixed alpha, 0:infinity (constant rate)".encode()+b"\n")
                        outfile.write("       Malpha = 0  * different alphas for genes".encode()+b"\n")
                        outfile.write("        ncatG = 8  * # of categories in dG of NSsites models".encode()+b"\n")
                        outfile.write("".encode()+b"\n")
                        outfile.write("        getSE = 0  * 0: don't want them, 1: want S.E.s of estimates".encode()+b"\n")
                        outfile.write(" RateAncestor = 1  * (0,1,2): rates (alpha>0) or ancestral states (1 or 2)".encode()+b"\n")
                        outfile.write("".encode()+b"\n")
                        outfile.write("   Small_Diff = .5e-6".encode()+b"\n")
                        outfile.write("    cleandata = 1  * remove sites with ambiguity data (1:yes, 0:no)?".encode()+b"\n")
                        outfile.write("*  fix_blength = -1  * 0: ignore, -1: random, 1: initial, 2: fixed".encode()+b"\n")
                        outfile.write("       method = 0  * Optimization method 0: simultaneous; 1: one branch a time".encode()+b"\n")
                        outfile.write("".encode()+b"\n")
                        outfile.write("* Genetic codes: 0:universal, 1:mammalian mt., 2:yeast mt., 3:mold mt.,".encode()+b"\n")
                        outfile.write("* 4: invertebrate mt., 5: ciliate nuclear, 6: echinoderm mt., ".encode()+b"\n")
                        outfile.write("* 7: euplotid mt., 8: alternative yeast nu. 9: ascidian mt., ".encode()+b"\n")
                        outfile.write("* 10: blepharisma nu.".encode()+b"\n")
                        outfile.write("* These codes correspond to transl_table 1 to 11 of GENEBANK.".encode()+b"\n")
                        outfile.write("".encode()+b"\n")

                except IOError:
                    print('File does not exit!')

    print('Number of folders modified =', count)

if __name__ == '__main__':
    main()
