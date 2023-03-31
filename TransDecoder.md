## TransDecoder software

[TransDecoder](https://github.com/TransDecoder/TransDecoder/wiki) is used to identify coding regions with transcript sequences, based on the follow criteria:
- Minimum open reading frame (ORF) found in transcript sequence
- Log-likelihood score similar to what is computed by the GeneID software is > 0
- Above coding score is greatest when the ORF is scored in the 1st reading frame as compared to scores in the other 2 forward reading frames
- If a candidate ORF is found fully encapsulated by the coordinates of another candidate ORF, the longer one is reported. However, a single transcript can report multiple ORFs (allowing for operons, chimeras, etc)
- PSSM is built/trained/used to refine the start codon prediction
- Optional the putative peptide has a match to a Pfam domain above the noise cutoff score

Version used: 5.7.0

### Installation:
 > conda create transdecoder -c bioconda transdecoder
 
 > conda activate transdecoder

### Running transdecoder:
Input = predicted genes from stalk-eyed fly mitochondrial genome (final_annotation_NT.fasta)
All parameters are listed [here](https://github.com/TransDecoder/TransDecoder/blob/master/Changelog.txt).

Step 1: Extract long ORFs from predicted genes

  > TransDecoder.LongOrfs -t final_annotation_NT.fasta

Step 2: Predict gene structures using long ORFs

 > TransDecoder.Predict -t final_annotation_NT.fasta --no_refine_starts
