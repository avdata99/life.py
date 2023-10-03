from life.nucleotide import Nucleotide


class Gene:
    """ Justa group of nucleotides """
    
    def __init__(self, nucleotides):
        self._nucleotides = [Nucleotide(nuc) for nuc in nucleotides]

    def __len__(self):
        return len(self._nucleotides)

    def __getitem__(self, index):
        return self._nucleotides[index]

    def __str__(self):
        return ''.join([str(nuc) for nuc in self._nucleotides])
