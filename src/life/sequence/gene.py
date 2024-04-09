import pandas as pd
import numpy as np

from life import Nucleotide
from life.exceptions import InvalidNuecleotide, InvalidGene
from life.files.base import GenFile


class Gene:
    """ Justa group of nucleotides """

    def __init__(self, nucleotides, load_from=None, load_to=None):
        """ Create a gene from a string of nucleotides
            Params:
             - nucleotides: str [mandatory] A string with the nucleotides
             - load_from: int [optional] Load the gene from this index in the string
             - load_to: int [optional] Load the gene to this index in the string
        """
        if not isinstance(nucleotides, str):
            raise InvalidGene(f'Gene must be a string, not {type(nucleotides)}')
        self.loaded_from_index = load_from
        self.loaded_to_index = load_to
        self._all_str = nucleotides[load_from:load_to].upper()
        try:
            self._nucleotides = [Nucleotide(nuc) for nuc in self._all_str]
        except InvalidNuecleotide as e:
            raise InvalidGene(f'{nucleotides} is not a valid gene') from e
        self._description = None

    @property
    def nucleotides(self):
        return self._nucleotides

    @property
    def nucleotides_str(self):
        return self._all_str

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

    def as_dataframe(self, from_=None, to=None):
        """ Convert the gene to a pandas dataframe
            Params:
             - from_: int [optional] Start from this index (inside the initial data loaded)
             - to: int [optional] End to this index (inside the initial data loaded)
        """
        if from_ is None:
            from_ = 0
        if to is None:
            to = len(self)
        serie_str = self._all_str[from_:to]
        return pd.Series(list(serie_str))

    def as_numpy_array(self, from_=None, to=None):
        """ Convert the gene to a numpy  array """
        if from_ is None:
            from_ = 0
        if to is None:
            to = len(self)
        serie_str = self._all_str[from_:to]
        return np.array(list(serie_str))
