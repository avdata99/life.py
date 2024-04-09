import numpy as np


def gene_as_numpy_array(gene):
    """ Convert the gene to a numpy array """
    return np.array([nuc.value for nuc in gene.nucleotides])
