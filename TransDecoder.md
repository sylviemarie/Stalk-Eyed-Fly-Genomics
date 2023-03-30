### [TransDecoder software](https://github.com/TransDecoder/TransDecoder/wiki)

TransDecoder is used to identify cpdiing regions with transcript sequences, based on the follow criteria:
- Minimum open reading frame (ORF) found in transcript sequence
- Log-likelihood score similar to what is computed by the GeneID software is > 0
- Above coding score is greatest when the ORF is scored in the 1st reading frame as compared to scores in the other 2 forward reading frames
- if a candidate ORF is found fully encapsulated by the coordinates of another candidate ORF, the longer one is reported. However, a single transcript can report multiple ORFs (allowing for operons, chimeras, etc)
- PSSM is built/trained/used to refine the start codon prediction
- Optional the putative peptide has a match to a Pfam domain above the noise cutoff score
