# Evolutionary rates analysis
## Overview of pipeline: 

1. Identify reciprocal orthologs
      - Only need to run the 00.get-longest-isoform.py script if there is more than one transcript per gene for each genome.
      - For 01.run-blastall.py script, need to select and download a series of input mitochondrial genomes (protein seq.) you want to blast against each other.
2. Identify open reading frames
      - BLASTX
4. Align orthologs
      - PRANK software
5. Mask alignments for poorly aligned regions
      - MEGA software
7. Calculate evolutionary rates
      - PAML CODEML --> branch model and branch-site model

## 1. Identify reciprocal orthologs

Pipeline which identifies reciprocal orthologs via BLAST from fasta files.
Naming of fasta files must be as follows: Speciesname.fa eg Oryziaslaptipes.fa

**python 00.get-longest-isoform.py**
- This script processes an Ensembl fasta file and picks the longest isoform for each gene. Outputs a new fasta file ending in _longest.fasta. This script will only work if fasta file is in Ensembl format.

**python 01.run-blastall.py**
- This script automatizes a complete reciprocal besthit blast analysis. A list of input genomes is blasted against each other and output is written in provided format. Name of outfile is db name.query name.bla. Run with "6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore sseq". Input genomes are fasta files containing one isoform per gene. Naming of fasta files must be as follows: Speciesname_longest.fasta eg Oryziaslaptipes_longest.fasta. [BLAST](http://blast.ncbi.nlm.nih.gov/Blast.cgi) must be compiled and added to the path of the user. *When it is added to PATH, no need to specify the path to blastn in the code.*

   > Template: python 1.run-blastall.py -e 10e-10 -b blastn -p 4 -f "6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore sseq" species1_longest.fasta species2_longest.fa species3_longest.fasta species4_longest.fa
   
   > Sylvie's code: python 01_run_blast_all.py -e 10e-10 -b blastn -p 4 -f "6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore sseq" Teleopsisdalmanni_longest.fasta Anophelesgambiae_longest.fasta Apismellifera_longest.fasta Drosophilamelanogaster_longest.fasta Heliconiusmelpomene_longest.fasta Zootermopsisnevadensis_longest.fasta

**python 02.top-blasthit.py**
- This script takes the outputs blast files of a reciprocal blast. 
First, identifies tophit for each blast. Minimum 30 pidentity, then picks the tophit with greatest bitscore. If bitscores are identical then the blast hit with greatest pidentity is picked as the tophit. If multiple sequenced have the same bitscore and pidentity, the ortholog is discarded. Second, finds 1-1 reciprocal orthologs. The blastout output format supported is:
"6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore sseq"

  >  Sylvie's code: python new_top_hit.py -i /fastdata/bop22smp/mitogenome/evol_rates/top_blast_hit/input_blast -o /fastdata/bop22smp/mitogenome/evol_rates/top_blast_hit

**python 03.ortho-cluster.py**
- This script takes the pickle output of reciprocal orthologs and identifies clusters of reciprocal orthologs.

  >  Sylvie's code: python ortho_cluster.py -i /fastdata/bop22smp/mitogenome/comp_gen_fasta/03_input.pkl -o 03_output -s Teleopsisdalmanni,Drosophilamelanogaster,Bactroceratryoni,Bombyxmori,Anophelesgambiae,Apismellifera


## 2. Identify open reading frames

Pipeline which identifies open reading frames of orthologous groups of sequences via BLASTx.

**python 04.make-blastx-input.py**
- This script prepares sequences for blastx analysis of orthologous sequences.Takes orthogroups and creates a folder for each. In each folder, a query fasta file is made with each nucleotide sequence. Users must specify a focal species and supply a fasta file containing protein sequences. This species forms the reference off which to identify open reading frames in the other species.Run with "6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore sseq".

**python 05.run-blastx.py**
- This script automatizes a blastx analysis of orthologous sequences. Takes each orthogroup folder and runs Blastx. [BLAST](http://blast.ncbi.nlm.nih.gov/Blast.cgi) must be compiled and added to the path of the user.This script takes the output of blastx for each orthogroup and identifies the open reading frame. Need blast format '6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore qframe sframe sseq'

    >Sylvie's code: python run-blastx.py Blastx_folder -e 10e-10 -f "6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore qframe sframe sseq" -b blastx

**python 06.orf-prediction.py**
- This script takes the output of blastx for each orthogroup and identifies the open reading frame. Need blast format '6 qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore qframe sframe sseq'

**OPTIONAL: python 07.orf-stats.py**
-This script calculates basic statistics about the length and number of open reading frames.

**OPTIONAL: python 08.check-protein.py**
- This script takes each orthogroup and checks that each species with an Ensembl protein file has a protein fasta sequence. 

## 3. Align orthologs

Pipeline which alignes open reading frames of reciprocal orthologs using PRANK. Alignments can then be filtered for length.

**python 09.make-prank-input.py**
- This script prepares sequences for prank alignment of orthologous sequences. Takes each folder of orthologous sequences and removes all files apart from cdna fasta file. Makes a new file with species names as the sequence id. Necessary for consistency with prank tree. Tree should be rooted eg (((Sp1,Sp2),Sp3),Sp4); and can contain branch lengths if available. 

**python 10.run-prank.py**
- This script automatizes a prank alignment between reciprocal orthologs.[PRANK](http://wasabiapp.org/software/prank/) must be compiled and added to the path of the user. See attached Chapter 10 in Multiple Sequence Alignment Methods, Methods in Molecular Biology for details on parameters to run. Automatically runs with -DNA, -codon and -once.

**python 11.check-gaps.py**
- Optional: This script calculates the alignment length after removing gaps in the alignment. It reports how many alignments fail the cutoff threshold specified.

**python 11.remove-gaps.py**
- This script removes gaps in the alignment of each orthogroup. It removes alignments where the length after gap removal fails the cutoff threshold specified.

## 4. Mask alignment for poorly aligned regions

Pipeline which masked alignments for poorly aligned regions using SWAMP. [SWAMP](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC4251194/) scans multiple-sequence alignments for short regions enriched with unreasonably high rates of nonsynonymous substitutions caused, for example, by sequence or alignment errors. Input for SWAMP is one-ratio model (model = 0, NSsites = 0) in codeml with clean data off.

**PAML one-ratio model (model = 0, NSsites = 0)** 

**python 12.convert-fasta-phylip.py**
- This script converts specified file in a folder of folders into phylip format. All other files are removed. This step is necessary for Paml.

**python 13.make-paml-input-cleandataoff.py**
- This script prepares sequences for [PAML](http://abacus.gene.ucl.ac.uk/software/paml.html). Takes each folder of orthologous sequences and removes all files apart from phylip file.
Tree should be unrooted eg ((Sp1,Sp2),Sp3,Sp4); Clean data option is turned off as this is recommended for running SWAMP.

     >python 13.make-paml-input-cleandataoff.py ~/Desktop/I ~/Desktop/tree_4sp_paml.txt -model 0 -nssites 0 -fixomega 0 -omega .4

**python 14.run-paml.py**
- This script automatizes a paml analysis. [PAML](http://abacus.gene.ucl.ac.uk/software/paml.html) must be compiled and added to the path of the user.

**SWAMP** 
- See [manual](https://github.com/peterwharrison/SWAMP) for running [SWAMP](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC4251194/). Often requires trying multiple windows and thresholds. Run branch-site model before and after masking to identify genes under positive selection. See if these genes are identified because the alignments are poor quality. Use this to guide the choice of masking criteria.

     > python SWAMP.py -i ~/Input -b ~/branchcodes.txt -m 150 -t 7 -w 15 > ~/swampoutput


## 5. Calculate evolutionary rates

**python 15.check-N.py**
- This script checks Ns in alignment are in multiples of 3. It checks that Ns are present in codons. Therefore, Ns can be removed in 15.remove-N.py without affecting the translation of the ORF.

**python 15.remove-N.py**
- This script removes masked sites (Ns) in the phylip alignment of each orthogroup. It removes alignments where the length after gap removal fails the cutoff threshold specified.

**python 12.convert-fasta-phylip.py**
- This script converts specified file in a folder of folders into phylip format. All other files are removed. This step is necessary for Paml.

- **python 13.make-paml-input.py**
This script prepares sequences for PAML. Takes each folder of orthologous sequences and removes all files apart from phylip file.
Tree should be unrooted eg ((Sp1,Sp2),Sp3,Sp4); Clean data option is turned on. The branch models allow the  ratio to vary among branches in the phylogeny and are useful for detecting positive selection acting on particular lineages

**python 14.run-paml.py**
- This script automatizes a paml analysis. [PAML](http://abacus.gene.ucl.ac.uk/software/paml.html) must be compiled and added to the path of the user.

###**Positive selection tests**

####**Branch-site model**
- Allows omega to vary both among lineages and among sites
- Assumes no positive selection on background. Therefore should run site model test to confirm this assumption is true.
- Use # to specify which branch to test for positive selection 
- Tree should be unrooted eg ((Sp1#,Sp2),Sp3,Sp4);
- **Alternative model: python 13.make-paml-input.py Input tree.txt -model 2 -nssites 2 -fixomega 0 -omega .4**
- **Null model: python 13.make-paml-input.py Input tree.txt -model 2 -nssites 2 -fixomega 1 -omega 1**

####**Site model test**
- Allows omega to vary among sites and is averaged across branches
- Tree should be unrooted eg ((Sp1,Sp2),Sp3,Sp4);
- Test 2A
  * **Alternative model: python 13.make-paml-input.py Input tree.txt -model 0 -nssites 2 -fixomega 0 -omega .4**
  * **Null model: python 13.make-paml-input.py Input tree.txt -model 0 -nssites 1 -fixomega 0 -omega .4**
- Test 8A - more conservation but should give same result as Test 2A
  * **Alternative model: python 13.make-paml-input.py Input tree.txt -model 0 -nssites 8 -fixomega 0 -omega .4**
  * **Null model: python 13.make-paml-input.py Input tree.txt -model 0 -nssites 8 -fixomega 1 -omega 1**
  
**python 16.paml-extract-loglikelihoods.py**
- This script takes the alternative and null model folders, extracts the log likelihoods and the difference: -2DL = -2*(likelihood_null-likelihood_alternative). To calculate the p-value use the Chisquared distribution. PAML has a function called Chi2 which takes the -2DL and degrees of freedom and outputs the p-value. Degrees of freedom are calculated as the difference in parameters between the null and alternative models. df = np_null - np_alternative.

###**Evolutionary rates**###

####**Branch model test**
- The branch models allow omega to vary among branches and are specified using the variable model.
- **Model = 0**
  * Calculates one omega for the whole tree**
  * Tree should be unrooted eg ((Sp1,Sp2),Sp3,Sp4);
  * **python 13.make-paml-input.py Input tree.txt -model 0 -nssites 0 -fixomega 0 -omega .4**
- **Model = 1**
  * Fits the so-called free-ratios model, which assumes an independent  ratio for each branch. This model is very parameter-rich and its use is discouraged. 
- **Model = 2**
  * Allows you to have several  ratios. You have to specify how many ratios and which branches should have which rates in the tree file by using branch labels.
  * Tree should be unrooted eg ((Sp1#,Sp2),Sp3,Sp4);
  * **python 13.make-paml-input.py Input tree.txt -model 2 -nssites 0 -fixomega 0 -omega .4**

**python 16.paml-extract-branch-lengths-dSfilter.py**
- This script takes an infolder containing folders with the output of branch model test and outputs branch lengths for the specified branch. Filters orthologs with branch-specific dS >= 2.

**python 16.paml-extract-branch-lengths-dSSdSfilter.py**
- This script takes an infolder containing folders with the output of branch model test and outputs branch lengths for the specified branch. Filters orthologs with branch-specific dS >= 2 or if SdS for that branch is <= 1.

## Tidying scripts

**python 00.clean-folder.py**
- Removes all files in folder of folders that do not end in string specified. 

**python 00.clean-folder-rename.py**
- Renames files in a folder of folders that end in string specified. 
