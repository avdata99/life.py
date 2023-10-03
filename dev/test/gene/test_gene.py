import pytest
from life.gene import Gene
from life.nucleotide import Nucleotide


def test_gene_init():
    """ Test Gene init """
    gene = Gene('ACGTGCA')
    assert gene[2] == Nucleotide('G')

def test_gene_len():
    """ Test Gene init """
    gene = Gene('ACGTGCA')
    assert len(gene) == 7

def test_gene_str():
    """ Test Gene init """
    gene = Gene('ACGTGCA')
    assert str(gene) == 'ACGTGCA'

def test_invalid_gene():
    with pytest.raises(ValueError):
        Gene('ACGTXCA')
