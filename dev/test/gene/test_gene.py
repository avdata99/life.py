import os
from unittest import TestCase
from life.exceptions import InvalidGene
from life import Gene, Nucleotide


class TestGene(TestCase):
    def setUp(self):
        self.code = 'ACGTGCA'
        self.gene = Gene(self.code)

    def test_gene_init(self):
        """ Test Gene init """
        self.assertEqual(self.gene[2], Nucleotide('G'))

    def test_gene_nucs_prop(self):
        """ Test Gene init """
        expected = [
            Nucleotide('A'), Nucleotide('C'), Nucleotide('G'),
            Nucleotide('T'), Nucleotide('G'), Nucleotide('C'),
            Nucleotide('A')
        ]
        self.assertEqual(self.gene.nucleotides, expected)

    def test_gene_code_prop(self):
        """ Test Gene init """
        self.assertEqual(self.gene.code, self.code)

    def test_gene_len(self):
        """ Test Gene init """
        self.assertEqual(len(self.gene), 7)

    def test_gene_str(self):
        """ Test Gene init """
        self.assertEqual(str(self.gene), 'ACGTGCA')

    def test_gene_eq(self):
        """ Test Gene init """
        self.assertEqual(self.gene, 'ACGTGCA')

    def test_invalid_gene(self):
        # assert we get a valuerror with unittest
        with self.assertRaises(InvalidGene):
            Gene('ACGTXCA')

    def test_save_bin(self):
        self.gene.save_bin('test.bin')
        with open('test.bin', 'rb') as f:
            assert f.read() == b'\x00\x01\x02\x03\x02\x01\x00'
        os.remove('test.bin')

    def test_ro_nucleotides(self):
        with self.assertRaises(AttributeError):
            self.gene.nucleotides = [Nucleotide('A')]

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
