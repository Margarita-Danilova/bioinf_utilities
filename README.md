# Bioinformatics utilities

A small collection of Python utilities for working with FASTQ, FASTA and BLAST output files.

## Requirements

Python 3. No external libraries are required.

## Usage

### FASTQ filtering

`filter_fastq` filters reads by GC content, sequence length and mean Phred33 quality.

```python
from bioinf_utilities import filter_fastq

filter_fastq(
    "input.fastq",
    "output.fastq",
    gc_bounds=(20, 80),
    length_bounds=(50, 150),
    quality_threshold=20
)
```

Filtered reads are saved to the `filtered` directory.

### Multiline FASTA conversion

`convert_multiline_fasta_to_oneline` converts sequences written on multiple lines to one-line FASTA format.

```python
from bioinf_utilities import convert_multiline_fasta_to_oneline

convert_multiline_fasta_to_oneline(
    "input.fasta",
    "output.fasta"
)
```

If the output file is not specified, the result is saved as `output.fasta`.

### BLAST output parsing

`parse_blast_output` extracts the first protein description for each BLAST query and saves the descriptions sorted alphabetically.

```python
from bioinf_utilities import parse_blast_output

parse_blast_output(
    "blast_results.txt",
    "proteins.txt"
)
```