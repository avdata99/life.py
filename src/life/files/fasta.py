from life.files.base import GenFile
from life.files.enums import GenFileInternalType


DEFAULT_EXTENSION = 'fasta'


class FastaFile(GenFile):
    """ Saving gen data to a bin file """

    def __init__(self, path=None):
        super().__init__()
        if path:
            self.open(path)

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
        pass
