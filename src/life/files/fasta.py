from life.files.base import GenFile
from life.files.enums import GenFileInternalType


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
        super().open(path, file_type=DEFAULT_EXTENSION)

    @staticmethod
    def get_extensions():
        """ Each file type has a list of possible extensions """
        return [DEFAULT_EXTENSION, 'fa']

    @staticmethod
    def get_file_internal_type():
        """ Get the internal type of the file """
        return GenFileInternalType.TEXT

    def save(self, gene, path):
        f = open(path, 'w')
        f.write(f'>{gene.description}\n')
        for i in range(0, len(gene), self._max_line_length):
            f.write(gene.code[i:i + self._max_line_length] + '\n')
        f.close()
