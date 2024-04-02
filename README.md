# life.py

Learning Genetics with Python

## Installation

```bash
pip install lifepy
```

## Usage

### Nucleotide

```python
from life import Nucleotide

nuc_a = Nucleotide('A')
nuc_t = Nucleotide('T')

nucs = nuc_a + nuc_t
type(nucs)
<class 'life.gene.Gene'>
print(nucs)
AT
```

### Gene


```python
from life import Gene
sequence = (
    "ggtaagtcctctagtacaaacacccccaatattgtgatataattaaaattatattcatat"
    "tctgttgccagaaaaaacacttttaggctatattagagccatcttctttgaagcgttgtc"
    "ggtaagtgctctagtacaaacacccccaatattgtgatataattaaaattatattcatat"
    "tctgttgccagattttacacttttaggctatattagagccatcttctttgaagcgttgtc"
    "tatgcatcgatcgacgactg"
)
g = Gene(sequence)
g.description = 'Some sample description'
# save will discover your desired format
g.save('test.fasta')
"""
>Some sample description
GGTAAGTCCTCTAGTACAAACACCCCCAATATTGTGATATAATTAAAATTATATTCATATTCTGTTGCCAGAAAAAACAC
TTTTAGGCTATATTAGAGCCATCTTCTTTGAAGCGTTGTCGGTAAGTGCTCTAGTACAAACACCCCCAATATTGTGATAT
AATTAAAATTATATTCATATTCTGTTGCCAGATTTTACACTTTTAGGCTATATTAGAGCCATCTTCTTTGAAGCGTTGTC
TATGCATCGATCGACGACTG
"""
g.save('test.110.fasta', max_line_length=110)
"""
>Some sample description
GGTAAGTCCTCTAGTACAAACACCCCCAATATTGTGATATAATTAAAATTATATTCATATTCTGTTGCCAGAAAAAACACTTTTAGGCTATATTAGAGCCATCTTCTTTG
AAGCGTTGTCGGTAAGTGCTCTAGTACAAACACCCCCAATATTGTGATATAATTAAAATTATATTCATATTCTGTTGCCAGATTTTACACTTTTAGGCTATATTAGAGCC
ATCTTCTTTGAAGCGTTGTCTATGCATCGATCGACGACTG
"""
g.save('test.life')
# Binary custom content
```