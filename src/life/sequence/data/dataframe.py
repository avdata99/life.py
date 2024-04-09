import pandas as pd


def gene_as_dataframe(gene):
    """ Convert the gene to a pandas dataframe """
    return pd.Series([str(nuc) for nuc in gene.nucleotides])
