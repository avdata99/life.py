from life.files.base import GenFile
from life.files.enums import GenFileInternalType


DEFAULT_EXTENSION = 'life'


class BinGenFile(GenFile):
    """ Saving gen data to a bin file """

    def __init__(self, path=None):
        super().__init__()
        if path:
            self.open(path)

    def open(self, path):
        raise NotImplementedError('BinGenFile open not implemented')

    @staticmethod
    def get_extensions():
        """ Each file type has a list of possible extensions """
        return [DEFAULT_EXTENSION]

    @staticmethod
    def get_file_internal_type():
        """ Get the internal type of the file """
        return GenFileInternalType.BIN

    def save(self, gene, path):
        """ Save as binary """
        f = open(path, 'wb')
        f.write(bytes([nuc.value for nuc in gene.nucleotides]))
        f.close()
