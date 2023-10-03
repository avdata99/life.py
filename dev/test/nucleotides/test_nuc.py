import pytest
from life.nucleotide import Nucleotide


def test_simple_nuc():
    """ Test the Nucleotide class """
    nuc = Nucleotide('A')
    assert nuc.value == 0
    assert nuc.name == 'A'
    assert str(nuc) == 'A'
    assert repr(nuc) == '<NUCLEOTIDE "A">'

def test_nuc_eq():
    """ Test the Nucleotide class """
    nuc = Nucleotide('A')
    assert nuc == Nucleotide('A')
    assert nuc == 'A'
    assert nuc != Nucleotide('C')

def test_invalid_nuc():
    with pytest.raises(ValueError):
        Nucleotide('X')
