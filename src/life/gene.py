from life import Nucleotide
from life.exceptions import InvalidNuecleotide, InvalidGene
from life.files.base import GenFile


class Gene:
    """ Justa group of nucleotides """

    def __init__(self, nucleotides):
        nucleotides = nucleotides.upper()
        try:
            self._nucleotides = [Nucleotide(nuc) for nuc in nucleotides]
        except InvalidNuecleotide as e:
            raise InvalidGene(f'{nucleotides} is not a valid gene') from e
        self._all_str = nucleotides
        self._description = None

    @property
    def nucleotides(self):
        return self._nucleotides

    @property
    def code(self):
        return self._all_str

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        """ Define or update the description of the secuence """
        if not isinstance(value, str):
            raise TypeError(f'Description must be a string, not {type(value)}')
        self._description = value

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

    def save(self, path, file_type=None, **kwargs):
        """ Save gene data
            params:
             - path: str [mandatory]
             - file_type: str [optional] life | fasta | fa | others by plugins
               If the path ends with an known extension we can omit this parameter
             - kwargs: dict [optional] extra parameters for the file class
        """
        gf = GenFile()
        gf.save(gene=self, path=path, file_type=file_type, **kwargs)
