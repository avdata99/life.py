class GenFile:
    """ Abstract class to inherit from for file generation. """

    def __init__(self, path=None):
        # The internal file object
        self.file_obj = None
        # prepare to up class
        self._up_class = None
        # this file can contain multiple sequences
        self.genes = []
        if path:
            self.open(path)

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

    @property
    def up_class(self):
        """ Get an object of the class that is being used to read/write the file """
        if self._up_class:
            return self._up_class
        raise ValueError('File not opened')

    def get_class_from_path_or_type(self, path, file_type):
        if not file_type:
            file_type = path.lower().split('.')[-1]
        up_class = self.get_class_from_file_extension(file_type)
        if not up_class:
            raise ValueError(f'Unknown file format "{file_type}"')
        return up_class

    def open(self, path, file_type=None):
        """
        Open a file
        params:
         - path: str [mandatory]
         - format: str [optional if path ends with a known extension]
        """
        file_class = self.get_class_from_path_or_type(path, file_type)
        # create an instance
        self._up_class = file_class()
        return self._up_class.open(path)

    def get_extensions(self):
        """ A list of possible extensions for the file """
        self.up_class.get_extensions()

    def get_file_internal_type(self):
        """
            Binary or text file?
            This must return life.files.enums.GenFileInternalType
        """
        self.up_class.get_file_internal_type()

    def save(self, gene, path, file_type=None, **kwargs):
        """ Save gene data with the expected class """
        file_class = self.get_class_from_path_or_type(path, file_type)

        # This class will know how to save the gene
        f = file_class()
        f.save(gene=gene, path=path, **kwargs)
