from life.files.enums import GenFileInternalType


class GenFile:
    """ Abstract class to inherit from for file generation. """

    def __init__(self):
        # The internal file object
        self.file_obj = None

    def get_all_extensions(self):
        """ A list of possible extensions for the file """
        # TODO implement a plugin system
        from life.files import ALL_FILE_CLASSES
        exts = {}  # extension: file_class
        for cls in ALL_FILE_CLASSES:
            for ext in cls.get_extensions():
                ext = ext.lower()
                if ext in exts:
                    raise ValueError(f'Extension "{ext}" is already in use')
                exts[ext] = cls
        return exts

    def get_class_from_file_extension(self, extension):
        """ Get the final file class from the extension """
        exts = self.get_all_extensions()
        return exts.get(extension)

    def get_class_from_path_or_type(self, path, file_type):
        if not file_type:
            file_type = path.lower().split('.')[-1]
        file_class = self.get_class_from_file_extension(file_type)
        return file_class

    def open(self, path, file_type=None):
        """
        Open a file
        params:
         - path: str [mandatory]
         - format: str [optional if path ends with a known extension]
        """
        file_class = self.get_class_from_path_or_type(path, file_type)
        if not file_class:
            raise ValueError(f'Unknown file format "{file_type}"')
        internal_type = file_class.get_file_internal_type()
        open_mode = 'r' if internal_type == GenFileInternalType.TEXT else 'rb'
        self.file_obj = open(path, open_mode)

    def get_extensions(self):
        """ A list of possible extensions for the file """
        raise NotImplementedError('get_extensions method not implemented')

    def get_file_internal_type(self):
        """
            Binary or text file?
            This must return life.files.enums.GenFileInternalType
        """
        raise NotImplementedError('get_file_internal_type method not implemented')

    def save(self, gene, path, file_type=None):
        """ Save gene data with the expected class """
        file_class = self.get_class_from_path_or_type(path, file_type)
        if not file_class:
            raise ValueError(f'Unknown file format "{file_type}"')

        # This class will know how to save the gene
        f = file_class()
        f.save(gene=gene, path=path)
