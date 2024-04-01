import os
from unittest import TestCase
from life import Codon, Nucleotide
from life.exceptions import InvalidCodon


class TestCodon(TestCase):
    def setUp(self):
        self.codon = Codon('ACG')

    def test_codon_init(self):
        """ Test codon init """
        self.assertEqual(self.codon[2], Nucleotide('G'))

    def test_codon_len(self):
        """ Test codon init """
        self.assertEqual(len(self.codon), 3)

    def test_codon_str(self):
        """ Test codon init """
        self.assertEqual(str(self.codon), 'ACG')

    def test_invalid_codon(self):
        """ Codon too long """
        with self.assertRaises(InvalidCodon):
            Codon('ACGT')

    def test_invalid_codon_nuc(self):
        """ Codon bad nuc """
        with self.assertRaises(InvalidCodon):
            Codon('XCA')

    def test_save(self):
        file_path = 'test.life'
        self.codon.save(file_path)
        with open(file_path, 'rb') as f:
            assert f.read() == b'\x00\x01\x02'
        os.remove(file_path)

    def test_is_start(self):
        self.assertTrue(Codon('ATG').is_start)
        self.assertFalse(Codon('TAA').is_start)

    def test_is_stop(self):
        self.assertTrue(Codon('TAA').is_stop)
        self.assertFalse(Codon('ATG').is_stop)
