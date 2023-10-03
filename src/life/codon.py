from life.exceptions import InvalidCodon, InvalidGene
from life.gene import Gene


class Codon(Gene):
    """ Is a Gene but with Only 3 Nucleotides """

    def __init__(self, nucleotides):
        if len(nucleotides) != 3:
            raise InvalidCodon(f'{nucleotides} is not a valid codon. We expect 3 nucleotides')
        try:
            super().__init__(nucleotides)
        except InvalidGene as e:
            raise InvalidCodon(f'{nucleotides} is not a valid codon') from e

    @property
    def is_start(self):
        return str(self) == 'ATG'

    @property
    def is_stop(self):
        return str(self) in ['TAA', 'TAG', 'TGA']
