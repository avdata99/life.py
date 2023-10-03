from life.codon import Codon


ALANINE = 'A'
CYSSTEINE = 'C'
ASPARTIC_ACID = 'D'
GLUTAMIC_ACID = 'E'
PHENYLALANINE = 'F'
GLYCINE = 'G'
HISTIDINE = 'H'
ISOLEUCINE = 'I'
LYSINE = 'K'
LEUCINE = 'L'
METHIONINE = 'M'
ASPARAGINE = 'N'
PROLINE = 'P'
GLUTAMINE = 'Q'
ARGININE = 'R'
SERINE = 'S'
THREONINE = 'T'
VALINE = 'V'
TRYPTOPHAN = 'W'
TYROSINE = 'Y'
SELENOCYSTEINE = 'U'
PYRROLYSINE = 'O'

amino_acids = {
    'TTT': PHENYLALANINE,
    'TTC': PHENYLALANINE,
    'TTA': LEUCINE,
    'TTG': LEUCINE,
    'CTT': LEUCINE,
    'CTC': LEUCINE,
    'CTA': LEUCINE,
    'CTG': LEUCINE,
    'ATT': ISOLEUCINE,
    'ATC': ISOLEUCINE,
    'ATA': ISOLEUCINE,
    'ATG': METHIONINE,
    'GTT': VALINE,
    'GTC': VALINE,
    'GTA': VALINE,
    'GTG': VALINE,
    'TCT': SERINE,
    'TCC': SERINE,
    'TCA': SERINE,
    'TCG': SERINE,
    'CCT': PROLINE,
    'CCC': PROLINE,
    'CCA': PROLINE,
    'CCG': PROLINE,
    'ACT': THREONINE,
    'ACC': THREONINE,
    'ACA': THREONINE,
    'ACG': THREONINE,
    'GCT': ALANINE,
    'GCC': ALANINE,
    'GCA': ALANINE,
    'GCG': ALANINE,
    'TAT': TYROSINE,
    'TAC': TYROSINE,
    'TAA': None,
    'TAG': None,
    'CAT': HISTIDINE,
    'CAC': HISTIDINE,
    'CAA': GLUTAMINE,
    'CAG': GLUTAMINE,
    'AAT': ASPARAGINE,
    'AAC': ASPARAGINE,
    'AAA': LYSINE,
    'AAG': LYSINE,
    'GAT': ASPARTIC_ACID,
    'GAC': ASPARTIC_ACID,
    'GAA': GLUTAMIC_ACID,
    'GAG': GLUTAMIC_ACID,
    'TGT': CYSSTEINE,
    'TGC': CYSSTEINE,
    'TGA': None,
    'TGG': TRYPTOPHAN,
    'CGT': ARGININE,
    'CGC': ARGININE,
    'CGA': ARGININE,
    'CGG': ARGININE,
    'AGT': SERINE,
    'AGC': SERINE,
    'AGA': ARGININE,
    'AGG': ARGININE,
    'GGT': GLYCINE,
    'GGC': GLYCINE,
    'GGA': GLYCINE,
    'GGG': GLYCINE,
}


class Aminoacid:
    def __init__(self, codon):
        """ Get an aminoacid from a codon.
            A codon can be a Codon object or a string of 3
            valid nucleotides
        """
        if isinstance(codon, Codon):
            self._codon = codon
        elif isinstance(codon, str):
            self._codon = Codon(codon)
        else:
            raise TypeError(f'Cannot get aminoacid from {type(codon)}')
        if str(self._codon) not in amino_acids:
            raise ValueError(f'{self._codon} is not a valid aminoacid')

        codon_str = str(self._codon)
        amino = amino_acids.get(codon_str)
        if amino is None:
            raise ValueError(f'{codon_str} is not a valid codon')
        self._aminoacid = amino_acids.get(codon_str)

    @property
    def codon(self):
        return self._codon

    @property
    def aminoacid(self):
        return self._aminoacid

    def __str__(self):
        return self._aminoacid
