# **Stalk-eyed fly comparative genomic analysis** 

- Identify orthologs, which are genes in different species that evolved from a common ancestor, across species
- Align the orthologs to estimate rates of evolution in mitochondrial coding sequences and detect putative signatures of positive selection

    <img width="624" alt="Screen Shot 2024-01-26 at 4 05 58 PM" src="https://github.com/sylviemarie/Stalk-Eyed-Fly-Genomics/assets/116887272/769faf8b-bff1-44dc-b547-76531cf464ac">


## Python scripts pipeline (Python2 scripts from Dr. Alison Wright and updated to run on Python3)
1. Identify reciprocal orthologs - via BLASTn reciprocal besthit analysis
2. Identify open reading frames - select focal species and run a BLASTx analysis of ortologous sequences
3. Align orthologs - using PRANK, a phylogeny-aware probabilistic multiple alignment software 
4. Mask alignments for poorly aligned regions - MEGA to manually delete poorly aligned regions and python to remove gaps
5. Calculate evolutionary rates and detect positive selection - PAML branch and branch-site models
