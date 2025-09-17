def proteins(strand):
    amino_acids_by_codons = {
        'AUG': 'Methionine',
        "UUU": 'Phenylalanine',
        "UUC": 'Phenylalanine',
        "UUA": 'Leucine',
        "UUG": 'Leucine',
        "UCU": 'Serine',
        "UCC": 'Serine',
        "UCA": 'Serine',
        "UCG": 'Serine',
        "UAU": 'Tyrosine',
        "UAC": 'Tyrosine',
        "UGU": 'Cysteine',
        "UGC": 'Cysteine',
        "UGG": 'Tryptophan'
    }

    STOP_CODONS = ['UAA', 'UAG', 'UGA']

    amino_acids_in_rna_sequence = []
    CODON_LENGTH = 3

    codon_start_position = 0
    codon_end_position = CODON_LENGTH

    while codon_end_position <= len(strand):
        codon_to_translate = strand[codon_start_position: codon_end_position]
        if codon_to_translate in STOP_CODONS:
            break;
        amino_acids_in_rna_sequence.append(amino_acids_by_codons[codon_to_translate])
        codon_start_position = codon_start_position + CODON_LENGTH
        codon_end_position = codon_end_position + CODON_LENGTH

    return amino_acids_in_rna_sequence

proteinTable = {
    'AUG': 'Methionine',
    'UUU': 'Phenylalanine',
    'UUC': 'Phenylalanine',
    'UUA': 'Leucine',
    'UUG': 'Leucine',
    'UCU': 'Serine',
    'UCC': 'Serine',
    'UCA': 'Serine',
    'UCG': 'Serine',
    'UAU': 'Tyrosine',
    'UAC': 'Tyrosine',
    'UGU': 'Cysteine',
    'UGC': 'Cysteine',
    'UGG': 'Tryptophan',
    'UAA': 'STOP',
    'UAG': 'STOP',
    'UGA': 'STOP'
}


def alternative_solution_proteins(strand):
    polypeptideList = []
    codonList = [(strand[i:i+3]) for i in range(0, len(strand), 3)]
    for codon in codonList:
        if proteinTable.get(codon) == 'STOP':
            return polypeptideList
        else:
            polypeptideList.append(proteinTable.get(codon))
    return polypeptideList
