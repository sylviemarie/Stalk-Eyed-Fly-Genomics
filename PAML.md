##  PAML ##

The CODEML program in the PAML package was used to calculate the rate of ortholog evolution and detect signatures of selection. While this program is known to be complex, [Alvarez-Carretero et al. in 2023](https://academic.oup.com/mbe/article/40/4/msad041/7140562) does a great job explaining it in an easily comprehensible way.

PAML detects selection by estimating the ratio of non-synonymous to synonymous mutations (i.e. 𝜔 = 𝑑𝑁⁄𝑑𝑆 ), which is an incredible simplistic, but powerful metric used across evolutionary biology. Within the CODEML program, there are three types of tests that can be run.

### CODEML tests ###
- The branch model = detect positive selection driving adaptive protein evolution within specific lineages of the species phylogeny
- The branch-site model = detect positive selection driving adaptive protein evolution within a subset of amino acids residues in the protein
- The site model = detect positive selection driving adaptive protein evolution affecting a subset of sites along a lineage specified *a priori*

Here, we provide a step-by-step protocol to illustrate the commonly used tests available in the program, including the branch models, the site models, and the branch-site models, which can be used to detect positive selection driving adaptive protein evolution affecting particular lineages of the species phylogeny, affecting a subset of amino acid residues in the protein, and affecting a subset of sites along prespecified lineages, respectivel


Note: all FASTA files need to be converted into PHYLIP format to be used in PAML, which is the preferred file format that stores a multiple sequence alignment. This is done using the script '12.convert-fasta-phylip.py'.
