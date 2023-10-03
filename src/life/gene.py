from life.exceptions import InvalidNuecleotide, InvalidGene
from life.nucleotide import Nucleotide


class Gene:
    """ Justa group of nucleotides """

    def __init__(self, nucleotides):
        try:
            self._nucleotides = [Nucleotide(nuc) for nuc in nucleotides]
        except InvalidNuecleotide as e:
            raise InvalidGene(f'{nucleotides} is not a valid gene') from e

    @property
    def nucleotides(self):
        return self._nucleotides

    def __len__(self):
        return len(self._nucleotides)

    def __getitem__(self, index):
        return self._nucleotides[index]

    def __str__(self):
        return ''.join([str(nuc) for nuc in self._nucleotides])

    def __eq__(self, other):
        if isinstance(other, Gene):
            return self._nucleotides == other.nucleotides
        elif isinstance(other, str):
            return str(self) == other
        if other is None:
            return False

        raise TypeError(f'Cannot compare Gene to {type(other)}')

    def save_bin(self, path):
        """ Save as binary """
        f = open(path, 'wb')
        f.write(bytes([nuc.value for nuc in self._nucleotides]))
        f.close()
