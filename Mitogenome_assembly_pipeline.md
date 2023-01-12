# **MitoHiFi V2.2**

Using [MitoHiFi ](https://github.com/marcelauliano/MitoHiFi) to assemble and annotate  _T. dalmanni_ mitochondrial genome. Reads provided by [UCL](https://www.ucl.ac.uk/~ucbhpom/).

MitoHifi was installed manually with each dependency installed and exported to my PATH.

## Input

- Two options: raw PacBio HiFi reads (-f) or assembled contigs (-c)
- Reference mitochondrial genome in FASTA or GenBank format (for _Teleopsis dalmanni_ --> _Nothybus sumatranus_)

Reference genome identified using python script provided by MitoHiFi, which identifies and downloads most closely-related reference genome from NCBI.

## Code

Activate python
> conda activate py39

> py39 mitohifi.py --help

Run MitoHifi with raw reads (r), reference genome fasta file (f), and reference genome genebank file (gb).
Alter parameters if necessary (t/threads = 1, o/organism genetic code = 5 (for invertebrates).
> python /usr/local/extras/Genomics/bin/mitohifi.py -r /fastdata/bop22smp/sylvie/mitogenome/m64157e_210730_141553.hifi_reads.fasta -r /fastdata/bop22smp/sylvie/mitogenome/m64157e_211024_013127.hifi_reads.fasta -f /fastdata/bop22smp/sylvie/mitogenome/NC_059897.1.fasta -g /fastdata/bop22smp/sylvie/mitogenome/NC_059897.1.gb -t 1 -o 5


