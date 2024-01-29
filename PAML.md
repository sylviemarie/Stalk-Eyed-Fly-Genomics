##  PAML ##

The CODEML program in the PAML package was used to calculate the rate of ortholog evolution and detect signatures of selection. While this program is known to be complex, [Alvarez-Carretero et al. in 2023](https://academic.oup.com/mbe/article/40/4/msad041/7140562) does a great job explaining it in an easily comprehensible way.

PAML detects selection by estimating the ratio of non-synonymous to synonymous mutations (i.e. 𝜔 = 𝑑𝑁⁄𝑑𝑆 ), which is an incredible simplistic, but powerful metric used across evolutionary biology. Within the CODEML program, there are three types of tests that can be run. This metric 𝜔, is a measure of the intensity and mode of natural selection acting on a protein-coding sequence.

𝜔 = 𝑑𝑁⁄𝑑𝑆, so...
- if 𝜔 = 1, then neutral evolution is occurring
- if 𝜔 > 1, then adaptive/diversifying selection is at work (positive selection)
- if 𝜔 < 1, the stabilizing selection is ongoing (under constraint)

### CODEML Tests ###
- The branch model = detect positive selection driving adaptive protein evolution within specific lineages of the species phylogeny; allows 𝜔 to vary among branches and are specified in the variable model; use unrooted tree
- The branch-site model = detect positive selection driving adaptive protein evolution within a subset of amino acids residues in the protein; allows 𝜔 to vary among lineages and across sites; specifies which branch to test for positive selection; use unrooted tree; compare null and alternate model
- The site model = detect positive selection driving adaptive protein evolution affecting a subset of sites along a lineage specified *a priori*

Note: all FASTA files need to be converted into PHYLIP format to be used in PAML, which is the preferred file format that stores a multiple sequence alignment. This is done using the script '12.convert-fasta-phylip.py'.

## Running PAML Models


<img width="641" alt="Screen Shot 2024-01-29 at 2 52 27 PM" src="https://github.com/sylviemarie/Stalk-Eyed-Fly-Genomics/assets/116887272/82060269-e7ab-457d-93be-6defe67fc2f2">


- The different models (m) represent the level of variation of ω between sites
  - m = 0 for one ω ratio for all lineages
  - m = 1 for independent ω ratio for each branch (i.e. the ‘free-ratio’ model)
  - m = 2 for more than 1 ω ratio, specified in unrooted phylogenetic tree.
    
- The nssites variable is the number of site classes being analyzed
  - n = 0 is used for one site class, where all sites in the gene evolve under the same ω
  - n = 1 is used for two site classes, where one site class has a fixed ω and the other site class can have a different ω
  - n = 2 is used for two site classes, where ω is allowed to vary in both
    
- To estimate the ω ratio, fixed ω is set to 0, and to test for significance, fixed ω is
set to 1.
- The variable ω represents the dN/dS ratio and implies the degree of selective pressure
(Alvarez-Carretero et al, 2023). 
