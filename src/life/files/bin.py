class BinFile:
    """ Form a list of valid chars, create a bin file whit all of them with a code """

    def __init__(self):
        # test for FASTA file nucleotid codes
        self.valid_codes = [
            'A', 'C', 'G', 'T', 'U', 'i', 'R', 'Y', 'K', 'M',
            'S', 'W', 'B', 'D', 'H', 'V', 'N', '-',
        ]

    def calculate_required_bits(self):
        """ Calculate the required bits to store all the valid codes """
        return len(self.valid_codes).bit_length()
