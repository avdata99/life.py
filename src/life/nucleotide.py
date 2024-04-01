"""
Valid nucleotides
adenine (A), cytosine (C), guanine (G), and thymine (T).
"""
from life.exceptions import InvalidNuecleotide


VALID_NUCS = {'A': 0, 'C': 1, 'G': 2, 'T': 3}


class Nucleotide:
    """ Just a nucleotide """
    def __init__(self, nucleotide):
        nucleotide = nucleotide.upper()
        if nucleotide not in VALID_NUCS:
            raise InvalidNuecleotide(f'{nucleotide} is not a valid nucleotide')
        self._name = nucleotide
        self._value = VALID_NUCS[nucleotide]

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._value

    def __str__(self):
        return self._name

    def __repr__(self):
        return f'<NUCLEOTIDE "{self._name}">'

    def __eq__(self, other):

        if isinstance(other, Nucleotide):
            return self._name == other.name
        if isinstance(other, str):
            return self._name == other.upper()
        if other is None:
            return False

        raise TypeError(f'Cannot compare Nucleotide to {type(other)}')

    def __add__(self, other):
        from life import Gene
        if isinstance(other, Nucleotide):
            code = f'{self._name}{other.name}'
            return Gene(code)
        elif isinstance(other, Gene):
            code = f'{self._name}{other.code}'
            return Gene(code)
        elif isinstance(other, str):
            code = f'{self._name}{other.upper()}'
            return Gene(code)
        raise TypeError(f'Cannot add Nucleotide to {type(other)}')
