from unittest import TestCase
from life.exceptions import InvalidNuecleotide
from life import Nucleotide, Gene


class TestNucleotide(TestCase):
    def test_simple_nuc(self):
        """ Test the Nucleotide class """
        nuc = Nucleotide('A')
        self.assertEqual(nuc.value, 0)
        self.assertEqual(nuc.name, 'A')
        self.assertEqual(str(nuc), 'A')
        self.assertEqual(repr(nuc), '<NUCLEOTIDE "A">')

    def test_nuc_eq(self):
        """ Test the Nucleotide class """
        nuc = Nucleotide('A')
        self.assertEqual(nuc, Nucleotide('A'))
        self.assertEqual(nuc, 'A')
        self.assertNotEqual(nuc, Nucleotide('C'))

    def test_invalid_nuc(self):
        with self.assertRaises(InvalidNuecleotide):
            Nucleotide('X')

    def test_ro_name(self):
        nuc = Nucleotide('A')
        with self.assertRaises(AttributeError):
            nuc.name = 'X'

    def test_ro_value(self):
        nuc = Nucleotide('A')
        with self.assertRaises(AttributeError):
            nuc.value = 1

    def test_add_nuc(self):
        nuc_a = Nucleotide('A')
        nuc_c = Nucleotide('C')
        nucs = nuc_a + nuc_c
        self.assertIsInstance(nucs, Gene)
        self.assertEqual(str(nucs), 'AC')
        self.assertEqual(nucs, Gene('AC'))

    def test_add_str(self):
        nuc_a = Nucleotide('A')
        nucs = nuc_a + 'c'
        self.assertIsInstance(nucs, Gene)
        self.assertEqual(str(nucs), 'AC')
        self.assertEqual(nucs, Gene('AC'))

    def test_add_gene(self):
        nuc_a = Nucleotide('A')
        gen_a = Gene('ACTGCA')
        nucs = nuc_a + gen_a
        self.assertIsInstance(nucs, Gene)
        self.assertEqual(str(nucs), 'AACTGCA')
        self.assertEqual(nucs, Gene('AACTGCA'))
