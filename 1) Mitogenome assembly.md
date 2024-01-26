# **MitoHiFi V2.2**

Using [MitoHiFi ](https://github.com/marcelauliano/MitoHiFi) to assemble and annotate  _T. dalmanni_ mitochondrial genome, with HiFi raw reads provided by [UCL](https://www.ucl.ac.uk/~ucbhpom/).

Initially, MitoHifi was installed manually with each dependency installed and exported to my PATH on Sheffield HPC. However, this presented a plethora of issues getting MitoHiFi to ***start*** running and then getting it to do a complete run. 

## Input data

- Two options: raw PacBio HiFi reads (-f) or assembled contigs (-c)
- Reference mitochondrial genome in FASTA or GenBank format

Reference genome identified using python script provided by MitoHiFi, which identifies and downloads most closely-related reference genome from NCBI. For *Teleopsis dalmanni* this was identified as *Loxocera sinica* (i.e. rust fly), for more info refer to the [NCBI website](https://www.ncbi.nlm.nih.gov/nuccore/NC_065368.1).

## Code

Activate python
> conda activate py39

> py39 mitohifi.py --help

Run MitoHiFi with raw reads (r), reference genome fasta file (f), and reference genome genebank file (gb).
Alter parameters if necessary (t/threads = 1, o/organism genetic code = 5 (for invertebrates).
> python /usr/local/extras/Genomics/bin/mitohifi.py -r /fastdata/bop22smp/sylvie/mitogenome/m64157e_210730_141553.hifi_reads.fasta -r /fastdata/bop22smp/sylvie/mitogenome/m64157e_211024_013127.hifi_reads.fasta -f /fastdata/bop22smp/sylvie/mitogenome/NC_065368.1.fasta -g /fastdata/bop22smp/sylvie/mitogenome/NC_065368.1.gb -t 1 -o 5

Alternatively, run MitoHiFi on a merged HiFi reads file (merged.fasta)
> python /usr/local/extras/Genomics/bin/mitohifi.py -r /fastdata/bop22smp/mitogenome/reads_ref/merged.fasta -f /fastdata/bop22smp/mitogenome/reads_ref/NC_065368.1.fasta -g /fastdata/bop22smp/mitogenome/reads_ref/NC_065368.1.gb -t 1 -o 5

## Output files

Successful completion of MitoHiFi should produce a series of output files.
- final_mitogenome.fasta - the final mitochondria circularized and rotated to start at tRNA-Phe
- final_mitogenome.gb - the final mitochondria annotated in GenBank format.
- final_mitogenome.coverage.png - the sequencing coverage throughout the final mitogenome
- final_mitogenome.annotation.png - the predicted genes throughout the final mitogenome
- contigs_annotations.png - annotation plots for all potential contigs
- coverage_plot.png - reads coverage plot of filtered reads mapped to all potential contigs
- contigs_stats.tsv - it will show you the statistics of your assembled mitos such as the number of genes, size, whether it was circularized or not, if the sequence has frameshifts and etc...
- shared_genes.tsv - show comparison of annotation between close-related mitogenome and all potential contigs assembled

For more detailed description of output files, refer back to [MitoHiFi ](https://github.com/marcelauliano/MitoHiFi)

