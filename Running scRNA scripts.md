# Integrate and normalize filtered scRNA data
  - [Find script here](https://github.com/petedprice/MeioticDrive2022/blob/main/R_analyses/scripts/prep/2.Integrate_normalise.R)
 
## Load R and install packages
This can be done on R/RStudio/Linux environment. But it's more efficient to run these analyses using R on an HPC cluster if using large datasets. If running it on a Linux environment, intiate a interactive or tmux session. If issues with R arise when trying to install all the R packages needed for Seurat, create a Conda environment.

> qrsh

> conda create -n seurat_scRNA -c bioconda -c conda-forge r-seurat r-base r-optparse r-tidyverse r-matrix r-scales r-cowplot r-rcurl r-stringr r-ggpubr

> module load apps/R/4.2.1/gcc-8.2.0

> R

Now check if R packages installed properly 'library("Seurat")', if not install them manually one-by-one
> install.packages("Seurat")

> install.packages("tidyverse")

> install.packages("dplyr") ... Matrix ... scales ... cowplot ... Rcurl ... stringr ... ggpubr ... future ... future.apply

## Personal library for R packages
> cd /home/bop22smp/R/x86_64-pc-linux-gnu-library/4.0 <-- where my R packages on cluster should be installed

## Start interactive or tmux session 
Request 64GB of memory, 4 nodes on cluster, specifically these nodes
> qrshx -l rmem=64G -pe smp 4 -P ressexcon -q ressexcon.q

## Submit intergrate_normalize R script
> Rscript Integrate_normalize.R -d /fastdata/bop22smp/stalkie_scRNA/R_Data/filtered_seurat.RData -o /fastdata/bop22smp/stalkie_scRNA/Integrate_output -t 1 -s /fastdata/bop22smp/stalkie_scRNA/R_Data/samples.txt -c /fastdata/bop22smp/stalkie_scRNA/R_Data/cell_cycle_markers_complete.csv

| Parameter | Path | Description |
| --- | --- | --- |
| -d | Path to seurat object |/fastdata/bop22smp/stalkie_scRNA/R_Data/filtered_seurat.RData  |
| -o | Path to output file | /fastdata/bop22smp/stalkie_scRNA/Integrate_output | 
| -t |  No. of threads | N/A |
| -s | Path to samples | /fastdata/bop22smp/stalkie_scRNA/R_Data/samples.txt | 
| -c | Path to cell markers | /fastdata/bop22smp/stalkie_scRNA/R_Data/cell_cycle_markers_complete.csv | 



