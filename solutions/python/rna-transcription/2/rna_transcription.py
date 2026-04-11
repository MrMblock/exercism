def to_rna(dna_strand):
    dna_strand = list(dna_strand)
    for i in range(len(dna_strand)):
        match dna_strand[i]:
            case "C":
                dna_strand[i] = "G"
            case "G":
                dna_strand[i] = "C"
            case "A":
                dna_strand[i] = "U"
            case "T":
                dna_strand[i] = "A"
                
    return ''.join(dna_strand)