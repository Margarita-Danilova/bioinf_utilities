
def get_description(line: str, description_end: int) -> str:
    """
    Extracts the Description field from a BLAST result line.

    Arguments:
    line: BLAST result line
    description_end: position where the Description field ends

    Returns 
    protein description.
    """
    protein_name = line[:description_end].strip()
    return protein_name