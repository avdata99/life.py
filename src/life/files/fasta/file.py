"""
Fasta file processing
Continue from here:
https://en.wikipedia.org/wiki/FASTA_format
"""
import logging
from life.files.base import GenFile
from life.files.enums import GenFileInternalType


logger = logging.getLogger(__name__)
DEFAULT_EXTENSION = 'fasta'


class FastaFile(GenFile):
    """ Saving gen data to a bin file """

    def __init__(self, path=None, max_line_length=80):
        super().__init__()
        if path:
            self.open(path)
        self._max_line_length = max_line_length

    @property
    def max_line_length(self):
        return self._max_line_length

    @max_line_length.setter
    def max_line_length(self, value):
        if not isinstance(value, int):
            raise TypeError(f'Max line length must be an integer, not {type(value)}')
        if value < 1:
            raise ValueError('Max line length must be greater than 0')
        self._max_line_length = value

    def open(self, path):
        """ Read the whole file and store the genes in memory """
        from life import Gene
        f = open(path, 'r')
        self.file_content = f.read()
        f.close()
        current_gene = None
        for line in self.file_content.split('\n'):
            if line.startswith('>'):
                if current_gene:
                    g = Gene(current_gene['code'])
                    g.description = current_gene['description']
                    self.genes.append(g)
                current_gene = {'description': line[1:], 'code': ''}
            else:
                current_gene['code'] += line.strip()

        if not current_gene:
            raise ValueError('No genes found in the file')

        # load the last gene
        g = Gene(current_gene['code'])
        g.description = current_gene['description']
        self.genes.append(g)

    @staticmethod
    def get_extensions():
        """ Each file type has a list of possible extensions """
        return [DEFAULT_EXTENSION, 'fa']

    @staticmethod
    def get_file_internal_type():
        """ Get the internal type of the file """
        return GenFileInternalType.TEXT

    def save(self, gene, path, **kwargs):
        """ Save as fasta """
        max_line_length = self._max_line_length
        for k, v in kwargs.items():
            if k == 'max_line_length':
                max_line_length = v
            else:  # raise on unexpected kwargs
                raise TypeError(f'Unexpected argument {k}')
        logger.debug(f'Saving gene as fasta [{max_line_length}] to {path}')
        f = open(path, 'w')
        f.write(f'>{gene.description}\n')
        for i in range(0, len(gene), max_line_length):
            f.write(gene.code[i:i + max_line_length] + '\n')
        f.close()
