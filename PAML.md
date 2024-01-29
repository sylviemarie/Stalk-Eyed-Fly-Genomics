##  PAML ##

All FASTA files need to be converted into PHYLIP format to be used in PAML, which is the preferred file format that stores a multiple sequence alignment. This is done using the script '12.convert-fasta-phylip.py'.

More specifically, the CODEML program in the PAML package was used to calculate the rate of ortholog evolution and detect
signatures of selection. While this software is complex, it is broken down more simplistically here by [Alvarez-Carretero et al. in 2023](https://academic.oup.com/mbe/article/40/4/msad041/7140562).



. More specifically,
the CODEML package in PAML was used to calculate the rate of ortholog evolution and detect
signatures of selection. PAML detects selection by estimating the ratio of non-synonymous to
synonymous mutations (i.e. 𝜔 = 𝑑𝑁⁄𝑑𝑆 ), which is an incredible simplistic, but powerful metric
used in evolutionary biology
