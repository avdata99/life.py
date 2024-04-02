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
        # a FASTA file can contain multiple sequences
        self.sequences = []
        # we use gene objects to load and validate them
        self.genes = []

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
        """ Open and load the file """
        # let the parent to open and do general checks
        super().open(path, file_type=DEFAULT_EXTENSION)
        logger.info(f'Opening fasta file {path}')
        content = self.file_obj.read()
        self.file_obj.close()
        # iterate all lines
        lines = content.split('\n')
        # check if the first line is a description
        if not lines[0].startswith('>'):
            # TODO read FASTA specs https://en.wikipedia.org/wiki/FASTA_format
            # maybe ";" is also allowed
            raise ValueError('The first line must start with ">"')

        self.sequences = []
        for line in lines:
            if line.startswith('>'):
                description = line[1:]
                description = description.strip()
                logger.info(f' - Sequence found "{description}"')
                seq = {'description': description, 'code': ''}
                self.sequences.append(seq)
            else:
                self.sequences[-1]['code'] += line.strip().upper()

        total_seq = len(self.sequences)
        logger.info(f'{total_seq} sequences found')
        # for seq in self.sequences:
        #     gene = Gene(seq['code'], description=seq['description'])
        #     self.genes.append(gene)
        # TODO continue

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
