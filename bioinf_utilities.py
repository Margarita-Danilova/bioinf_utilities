import os
from helpers.fastq import process_fastq
from helpers.bio_files import get_description


def filter_fastq(
    input_fastq: str,
    output_fastq: str,
    gc_bounds=(0, 100),
    length_bounds=(0, 2**32),
    quality_threshold: float = 0
) -> None:
    """
    Filters FASTQ reads by GC content, length and mean quality.

    Arguments:
    input_fastq: path to the input FASTQ file
    output_fastq: name of the output FASTQ file
    gc_bounds: GC content bounds in percent
    length_bounds: read length bounds
    quality_threshold: minimum mean read quality

    Returns None.
    """ 
    if not os.path.exists("filtered"):
        os.mkdir("filtered")

    output_path = os.path.join("filtered", output_fastq)

    with open(input_fastq, mode="r") as input_file:
        with open(output_path, mode="w") as output_file:
            process_fastq(
                input_file,
                output_file,
                gc_bounds,
                length_bounds,
                quality_threshold
            )

def convert_multiline_fasta_to_oneline(
    input_fasta: str,
    output_fasta: str = "output.fasta"
) -> None:  
    """
    Converts a multiline FASTA file to a FASTA file with one-line sequences.

    Arguments:
    input_fasta: path to the input FASTA file
    output_fasta: name of the output FASTA file

    Returns None.
    """
    sequence = ""
    header = ""

    with open(input_fasta, mode="r") as input_file:
        with open(output_fasta, mode="w") as output_file:
            for line in input_file:
                if line[0] == ">":
                    if sequence:
                        output_file.write(header + "\n")
                        output_file.write(sequence + "\n")

                    header = line.strip()
                    sequence = ""
                else:
                    sequence = sequence + line.strip()

            if sequence:
                output_file.write(header + "\n")
                output_file.write(sequence + "\n")


def parse_blast_output(input_file: str, output_file: str) -> None:
    """
    Extracts the first protein description for each BLAST query and sorts the results.

    Arguments:
    input_file: path to the BLAST output file
    output_file: name of the output file

    Returns None.
    """
    protein_names = []

    with open(input_file, mode="r") as file:
        for line in file:
            if "Sequences producing significant alignments:" in line:
                header_line = file.readline()
                description_end = header_line.index("Scientific")

                file.readline()
                result_line = file.readline()

                protein_name = get_description(result_line, description_end)
                protein_names.append(protein_name)

    protein_names.sort()

    with open(output_file, mode="w") as file:
        for protein_name in protein_names:
            file.write(protein_name + "\n")
