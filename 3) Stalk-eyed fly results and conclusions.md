# Mitochondrial genome assembly
Using MitoHiFi, a circular mitochondrial genome for the Malaysian stalk-eyed fly *Teleopis dalmanni* was assembled with all 37 genes, including 2 rRNA, 13 protein-coding, and 22 tRNA genes. The entire mitogenome was 20,708 base pairs.


<img width="622" alt="circular mitogenome" src="https://github.com/sylviemarie/Stalk-Eyed-Fly-Genomics/assets/116887272/91a6273f-a7ee-4310-8750-c99c027b0f8f">


# PAML

<img width="621" alt="phylogenetic tree" src="https://github.com/sylviemarie/Stalk-Eyed-Fly-Genomics/assets/116887272/928eb57c-9f73-4b44-87a6-e6ece138cf01">


## Estimating evolutionary rates with PAML's branch model

<img width="624" alt="branch model branch lengths" src="https://github.com/sylviemarie/Stalk-Eyed-Fly-Genomics/assets/116887272/904ba0ca-950a-439c-a0ba-fb0dff9ef205">

- Cob, cox1, and nad4 showed higher foreground ω values relative to the background ω values, which indicates that these three orthologs in particular are evolving at a faster rate in the foreground branch (Teleopsis dalmanni) relative to the other lineages. In contrast, cox 3, nad4, and nad5 have lower foreground ω relative to background ω, and therefore, are accumulating evolutionary changes at a slower pace in T. dalmanni than other species. Both cob and nad5 have the highest total tree lengths at 27.028 and 116.648, respectively. Nad5 has a particularly high dS tree length, which represent the cumulative length of branches that have experienced synonymous (silent) mutations. Estimates of ω suggest that cox1 is the only gene with dN/dS ratio of > 1 on the
foreground branch, while all other genes have ω < 1.


<img width="622" alt="branch model metrics" src="https://github.com/sylviemarie/Stalk-Eyed-Fly-Genomics/assets/116887272/7c907536-2083-41d0-8fcb-be80d0c70f87">

- The PAML branch model also estimates each branch length for the 6 genes, see Table 5. Branch length quantifies genetic divergence and evolutionary change. Once again, nad5 demonstrates a particularly high total tree length, much of which is attributed to the 9 ... 3 foreground branch and the 7 ... 6 branch that represents the Apis mellifera lineage after divergence from Bombyx mori. The gene cob has the second largest tree length estimate, with the majority of genetic diversity originating from the 8 ... 4 branch (Anopheles gambiae lineage) and 7 ... 6 branch (Apis mellifera).



## Detecting positive selection with PAML's branch-site model

<img width="621" alt="LRT" src="https://github.com/sylviemarie/Stalk-Eyed-Fly-Genomics/assets/116887272/60edb98b-918d-41d2-9127-c46dfa8ee596">

- The likelihood ratio statistic (2ΔlnL), degrees of freedom, and a chi-square distribution were used to estimate a p-value corresponding to each gene, see Table 6. For the cob gene, the alternative
model was accepted by a statistically significant p-value < 0.05 as this model provided a better fit to explain the sequence alignment data over the null model. The p-value for cox1, cox3, nad1, nad4, and nad5 was high (> 0.05), and the null model was accepted as a better fit for the data. The PAML branch-site models were used to elucidate the selective pressure acting on different
site classes within the cob gene.


<img width="628" alt="MLE" src="https://github.com/sylviemarie/Stalk-Eyed-Fly-Genomics/assets/116887272/87d7a5f8-c2b8-4cdb-96ea-8229fb22b46b">

- Maximum Likelihood Estimates (MLEs) for both the null and alternative models are summarized in Table 7, where site classes are used to model different patterns of sequence evolution and selective pressures. The null model assumes uniform selection across all sites, while the alternative model is more flexible and allows positive selection (ω > 1) in specific site classes. For site class 0 in cob, 93.9% of sites in the alt. model (ω = 0.006) and 95.8% of sites in the null model (ω = 0.012) are under negative selection with low ω values. For site class 1, 2.7% of sites in the alt. model and 4.2% in the null model are under neutral evolution or weak selection with ω = 1 for both models. For site class 2a, 3.2% of sites in the alt. model (background ω = 0.006, foreground ω = 216.967) and 0% of sites in the null model (background ω = 0.012, foreground ω = 1) are under moderate positive selection. For site class 2b, 0.1% of sites in the alt. model (background ω = 1, foreground ω = 216.967) and 0% of sites in the null model (background ω = 1, foreground ω = 1) are under moderate positive selection.
















