from life.codon import Codon
from life.exceptions import InvalidAminoAcid, InvalidCodon
from life.extras.amino_from_code import amino_acids_from_code
from life.extras.amino_from_codons import amino_acids_from_codon


class Aminoacid:

    def __init__(self, code):
        """ Get an aminoacid from a single letter code
            or from a codon.
            A codon can be a Codon object or a string of 3
            valid nucleotides
        """
        # We can have a codon if come from a codon
        self._codon = None
        self._code = None
        self._name = None

        if isinstance(code, Codon):
            self._get_from_codon(code)
        elif isinstance(code, str):
            code = code.upper()
            if len(code) == 3:
                self._get_from_codon(code)
            elif len(code) == 1:
                self._get_from_code(code)
            else:
                raise InvalidAminoAcid(f'Invalid aminoacid length {code}')
        else:
            raise InvalidAminoAcid(f'Cannot get aminoacid from {code} :: <{type(code)}>')

    def _get_from_codon(self, codon):
        if isinstance(codon, Codon):
            self._codon = codon
        elif isinstance(codon, str):
            try:
                self._codon = Codon(codon)
            except InvalidCodon as e:
                raise InvalidAminoAcid(f'Cannot get aminoacid from codon {codon} :: {e}')
        else:
            raise InvalidAminoAcid(f'Cannot get aminoacid from type <{type(codon)}>')
        if str(self._codon) not in amino_acids_from_codon:
            raise InvalidAminoAcid(f'{self._codon} is not a valid aminoacid')
        elem = amino_acids_from_codon[str(self._codon)]
        self._name = elem['name']
        self._code = elem['code']

    def _get_from_code(self, code):
        if isinstance(code, str):
            elem = amino_acids_from_code.get(code)
        else:
            raise InvalidAminoAcid(f'Cannot get aminoacid from type <{type(code)}>')
        if elem is None:
            raise InvalidAminoAcid(f'{code} is not a valid aminoacid')
        self._code = code
        self._name = elem['name']

    @property
    def codon(self):
        return self._codon

    @property
    def name(self):
        return self._name

    @property
    def code(self):
        return self._code

    def __str__(self):
        return self._code

    def __repr__(self):
        return f'<Aminoacid {self._code} {self._name}>'

    def __eq__(self, other):
        if other is None:
            return False
        if isinstance(other, str):
            return self._code == other
        elif isinstance(other, Aminoacid):
            return self._code == other._code
        raise TypeError(f'Cannot compare aminoacid with type <{type(other)}>')

    def all_codons(self):
        """ Return a list of all codons for this aminoacid """
        return [Codon(c) for c in amino_acids_from_code[self._code]['codons']]


ALANINE = Aminoacid('A')
CYSSTEINE = Aminoacid('C')
ASPARTIC_ACID = Aminoacid('D')
GLUTAMIC_ACID = Aminoacid('E')
PHENYLALANINE = Aminoacid('F')
GLYCINE = Aminoacid('G')
HISTIDINE = Aminoacid('H')
ISOLEUCINE = Aminoacid('I')
LYSINE = Aminoacid('K')
LEUCINE = Aminoacid('L')
METHIONINE = Aminoacid('M')
ASPARAGINE = Aminoacid('N')
PYRROLYSINE = Aminoacid('O')
PROLINE = Aminoacid('P')
GLUTAMINE = Aminoacid('Q')
ARGININE = Aminoacid('R')
SERINE = Aminoacid('S')
THREONINE = Aminoacid('T')
SELENOCYSTEINE = Aminoacid('U')
VALINE = Aminoacid('V')
TRYPTOPHAN = Aminoacid('W')
TYROSINE = Aminoacid('Y')
