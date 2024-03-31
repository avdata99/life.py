from life.files.bing import BinGenFile
from life.files.fasta import FastaFile

# TODO implement a plugin system with pkg_resources.iter_entry_points
ALL_FILE_CLASSES = [BinGenFile, FastaFile]
