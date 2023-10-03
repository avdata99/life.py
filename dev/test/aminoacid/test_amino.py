from unittest import TestCase
from life.exceptions import InvalidAminoAcid
from life.aminoacid import Aminoacid, ARGININE


class TestAminoFromCode(TestCase):
    def setUp(self):
        self.amino = Aminoacid('A')

    def test_init(self):
        """ Test Gene init """
        self.assertIsNone(self.amino.codon)
        self.assertEqual(self.amino.name, 'Alanine')
        self.assertEqual(self.amino.code, 'A')

    def test_str(self):
        """ Test Gene init """
        self.assertEqual(str(self.amino), 'A')

    def test_eq(self):
        """ Test Gene init """
        self.assertEqual(self.amino, 'A')
        self.assertEqual(self.amino, Aminoacid('A'))

    def test_invalid(self):
        # assert we get a valuerror with unittest
        with self.assertRaises(InvalidAminoAcid):
            Aminoacid('X')

    def test_ro(self):
        with self.assertRaises(AttributeError):
            self.amino.code = 'S'

    def test_all_codons(self):
        self.assertEqual(self.amino.all_codons(), ['GCT', 'GCC', 'GCA', 'GCG'])


class TestAminoFromCodon(TestCase):
    def setUp(self):
        # 'C': {'name': 'Cysteine', 'codons': ['TGT', 'TGC']},
        self.amino = Aminoacid('TGC')

    def test_init(self):
        """ Test Gene init """
        self.assertEqual(self.amino.codon, 'TGC')
        self.assertEqual(self.amino.name, 'Cysteine')
        self.assertEqual(self.amino.code, 'C')

    def test_str(self):
        """ Test Gene init """
        self.assertEqual(str(self.amino), 'C')

    def test_eq(self):
        """ Test Gene init """
        self.assertEqual(self.amino, 'C')
        self.assertEqual(self.amino, Aminoacid('C'))

    def test_invalid(self):
        # assert we get a valuerror with unittest
        with self.assertRaises(InvalidAminoAcid):
            Aminoacid('ACX')

    def test_ro(self):
        with self.assertRaises(AttributeError):
            self.amino.code = 'A'

    def test_all_codons(self):
        self.assertEqual(self.amino.all_codons(), ['TGT', 'TGC'])


class TestConst(TestCase):
    def test_const(self):
        self.assertEqual(ARGININE, Aminoacid('R'))
