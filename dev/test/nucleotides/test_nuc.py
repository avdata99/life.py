from unittest import TestCase
from life.exceptions import InvalidNuecleotide
from life.nucleotide import Nucleotide


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
