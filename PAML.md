##  PAML ##

The CODEML program in the PAML package was used to calculate the rate of ortholog evolution and detect signatures of selection. While this software is complex, [Alvarez-Carretero et al. in 2023](https://academic.oup.com/mbe/article/40/4/msad041/7140562) does a good job of breaking down the bones of the package (e.e. what it does, how to use it, etc.).
Note: all FASTA files need to be converted into PHYLIP format to be used in PAML, which is the preferred file format that stores a multiple sequence alignment. This is done using the script '12.convert-fasta-phylip.py'.

PAML detects selection by estimating the ratio of non-synonymous to synonymous mutations (i.e. 𝜔 = 𝑑𝑁⁄𝑑𝑆 ), which is an incredible simplistic, but powerful metric used in evolutionary biology.
