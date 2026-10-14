

def check_length(sequence: str, length_bounds) -> bool:
    """
    Checks whether the sequence length is within the given bounds.

    Arguments:
    sequence: nucleotide sequence
    length_bounds: sequence length bounds

    Returns True if the sequence passes the length filter, otherwise False.
    """
    length = len(sequence)

    if type(length_bounds) == int or type(length_bounds) == float:
        lower = 0
        upper = length_bounds
    else:
        lower = length_bounds[0]
        upper = length_bounds[1]

    if length >= lower and length <= upper:
        return True
    else:
        return False



def check_gc(sequence: str, gc_bounds) -> bool:
    """
    Checks whether the GC content of a sequence is within the given bounds.

    Arguments:
    sequence: nucleotide sequence
    gc_bounds: GC content bounds in percent

    Returns True if the sequence passes the GC filter, otherwise False.
    """
    gc_count = sequence.count("G") + sequence.count("C")
    gc_percent = gc_count / len(sequence) * 100

    if type(gc_bounds) == int or type(gc_bounds) == float:
        lower_gc = 0
        upper_gc = gc_bounds
    else:
        lower_gc = gc_bounds[0]
        upper_gc = gc_bounds[1]

    if gc_percent >= lower_gc and gc_percent <= upper_gc:
        return True
    else:
        return False



def check_quality(quality: str, quality_threshold: float) -> bool:
    """
    Checks whether the mean read quality meets the threshold.

    Arguments:
    quality: FASTQ quality string
    quality_threshold: minimum mean quality

    Returns 
    True if the read passes the quality threshold, otherwise False.
    """
    total_quality = 0

    for symbol in quality:
        phred = ord(symbol) - 33
        total_quality = total_quality + phred

    average_quality = total_quality / len(quality)

    if average_quality >= quality_threshold:
        return True
    else:
        return False