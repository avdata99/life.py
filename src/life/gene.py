from life.exceptions import InvalidNuecleotide, InvalidGene
from life import Nucleotide


class Gene:
    """ Justa group of nucleotides """

    def __init__(self, nucleotides):
        try:
            self._nucleotides = [Nucleotide(nuc) for nuc in nucleotides]
        except InvalidNuecleotide as e:
            raise InvalidGene(f'{nucleotides} is not a valid gene') from e
        self._all_str = nucleotides

    @property
    def nucleotides(self):
        return self._nucleotides

    @property
    def code(self):
        return self._all_str

    def __len__(self):
        return len(self._nucleotides)

    def __getitem__(self, index):
        return self._nucleotides[index]

    def __str__(self):
        return self._all_str

    def __repr__(self):
        code = str(self)[:5]
        if len(self) > 5:
            code += '...'

        return f'<Gene {code}>'

    def __eq__(self, other):
        if isinstance(other, Gene):
            return self._nucleotides == other.nucleotides
        elif isinstance(other, str):
            return str(self) == other
        if other is None:
            return False

        raise TypeError(f'Cannot compare Gene to {type(other)}')

    def __add__(self, other):
        from life import Nucleotide
        if isinstance(other, Nucleotide):
            code = f'{self._all_str}{other.name}'
            return Gene(code)
        elif isinstance(other, Gene):
            code = f'{self._all_str}{other.code}'
            return Gene(code)
        elif isinstance(other, str):
            code = f'{self._all_str}{other.upper()}'
            return Gene(code)
        raise TypeError(f'Cannot add Gene to {type(other)}')

    def save_bin(self, path):
        """ Save as binary """
        f = open(path, 'wb')
        f.write(bytes([nuc.value for nuc in self._nucleotides]))
        f.close()
