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


<img width="627" alt="bayes empirical estimate" src="https://github.com/sylviemarie/Stalk-Eyed-Fly-Genomics/assets/116887272/32f6044f-0c84-4498-a183-87e2a06dbeb2">

- The Bayes Empirical Bayes (BEB) analysis was used in the PAML branch-site alternative model to identify specific amino acid sites in the protein-coding cob sequence that are likely under
positive selection promoting adaptive evolution, along particular branches. The results for the BEB analysis on cob are found in Table 8. There is a 53.4% probability that the amino acid
residue at site 34 (Asparagine) is likely under positive selection. For the Glycine amino acid at site 71, there is a 83.9% probability it is under positive selection. There is a 60.4% probability that Valine at site 191 is likely under positive selection and a 78.6% probability that Leucine at site 241 is under diversifying selection. Valine at site 273 has a 74.2% probability that it is under positive selection.

# Brief conclusion:
1) The _Teleopsis dalmanni_ mitochondrial genome retains many aspects of the highly conserved gene content and organization (e.g. all 37 genes - 2 rRNA, 22 tRNA, and 13 protein-coding), but was ~3.5kb longer than expected of an insect mitogenome.
   
3) Three mitochondrial genes (_cob, cox1,_ and _nad4_) in _Teleopsis dalmanni_ are evolving at a faster rate relative to the background branches, i.e. the five other insects used in the comparative study.
   
5) A clear and statistically significant signature of positive selection was detected in the _cob_ gene in Teleopsis dalmanni, as well as five potential sites within this sequence were identified to be under positive selection.










